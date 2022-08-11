import io
import os
import subprocess
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from datetime import datetime, timedelta
from docutils import nodes
from docutils.parsers.rst import Directive
from packages import extra_packages, packages
import sphinx_material

class Packages(Directive):

    def run(self):
        output = list()
        # General text
        intro = f"""
<p>
You can install one of the packages provided by <b>FEM on Colab</b> by adding the following cell at the top of your notebook.
</p>
"""
        output.append(nodes.raw(text=intro, format="html"))
        # Packages
        for package in packages.keys():
            data = packages[package]
            buttons = self._dropdown("Our tests", data["tests"])
            card_num = self._card(
                package=package,
                title=data["title"],
                installation=data["installation"],
                installation_suffixes=data["installation_suffixes"],
                buttons=buttons
            )
            if "hide" not in data or not data["hide"]:
                output.append(nodes.raw(text=card_num, format="html"))
        return output

    @classmethod
    def _card(cls, package, title, installation, installation_suffixes, buttons):
        if len(installation_suffixes) == 1:
            assert installation_suffixes[0] == ""
            package_installation = "<div class=\"package-installation\">" + installation.lstrip().rstrip() + "</div>"
        else:
            package_installation_template = installation.lstrip().rstrip()
            package_installation = ""
            for suffix in installation_suffixes:
                suffix_title = suffix.capitalize() + " mode"
                toggle_open = " checked" if suffix == "real" else ""
                div_class = "package-installation-real" if suffix == "real" else "package-installation-complex"
                package_installation += (
                    f"<input type=\"checkbox\" name=\"installation-toggle-{package}-{suffix}\" id=\"installation-toggle-{package}-{suffix}\" class=\"installation-toggle\"{toggle_open}>"
                    + f"<label for=\"installation-toggle-{package}-{suffix}\" class=\"installation-toggle-title\">{suffix_title}</label>"
                    + f"<div class=\"{div_class}\">"
                    + package_installation_template.replace("SUFFIX", suffix) + "</div>")
        return f"""
<div class="package-card">
  <div class="package-logo">
    {cls._library_image(package)}
  </div>
  <div class="package-content">
    <h3 class="package-title">
      {title}
    </h3>
    {package_installation}
    <div class="package-buttons">
      {buttons}
    </div>
  </div>
</div>
"""

    @classmethod
    def _dropdown(cls, title, libraries_urls):
        dropdown = f"""
<div id="package-dropdown-{cls._dropdown_id}" class="jq-dropdown jq-dropdown-tip">
    <ul class="jq-dropdown-menu">
"""
        for (library, url) in libraries_urls.items():
            if not url.startswith("https://colab.research.google.com"):
                colab_url = f"https://colab.research.google.com/github/fem-on-colab/fem-on-colab/blob/main/{url}"
            else:
                colab_url = url
            dropdown += f"""
        <li><a href="{colab_url}" target="_blank">{cls._library_image(library)} {library}</a></li>
"""
        dropdown += f"""
    </ul>
</div>
<div class="package-button" data-jq-dropdown="#package-dropdown-{cls._dropdown_id}">{title}</div>
"""
        cls._dropdown_id += 1
        return dropdown

    _dropdown_id = 1

    @staticmethod
    def _library_image(library):
        if library in ("dolfin", "dolfinx", "fenics", "fenicsx", "mshr"):
            logo = "_static/images/fenics-logo.png"
        elif library in ("firedrake", "fireshape"):
            logo = "_static/images/firedrake-logo.png"
        elif library == "gmsh":
            logo = "_static/images/gmsh-logo.png"
        elif library == "multiphenics":
            logo = "_static/images/multiphenics-logo.png"
        elif library in ("multiphenicsx", "multiphenicsx (with plotly)", "multiphenicsx (with pyvista)"):
            logo = "_static/images/multiphenicsx-logo.png"
        elif library in ("ngsolve", "ngsolve (extras)", "ngsxfem"):
            logo = "_static/images/ngsolve-logo.png"
        elif library == "RBniCS":
            logo = "_static/images/rbnics-logo.png"
        else:
            raise RuntimeError("Invalid type " + library)
        return f'<img src="{logo}" style="vertical-align: middle; width: 25px">'

class Stats(Directive):

    def run(self):
        # Get release download stats from file, and convert it to a plot
        stats = pd.read_csv("_stats/stats.csv")
        week_to_headers = dict()
        for header in stats.columns:
            if header.startswith("count_"):
                day = header.replace("count_", "").replace("_", "/")
                week = datetime.strptime(day, "%Y/%m/%d").strftime("%Y-%U")
                if week not in week_to_headers:
                    week_to_headers[week] = list()
                week_to_headers[week].append(header)
        last_weeks = pd.date_range(
            start=max(datetime(2022, 7, 29), datetime.now() + timedelta(weeks=-13)), end=datetime.now(), freq="W")
        last_weeks = [week.strftime("%Y-%U") for week in last_weeks.tolist()]
        weekly_stats = pd.DataFrame(0, columns=list(packages.keys()), index=last_weeks)
        for package in weekly_stats.columns:
            condition = stats.package.str.fullmatch(package)
            if sum(condition) > 0:
                stats_package = stats[condition].sum(axis=0)
                for (week, headers) in week_to_headers.items():
                    weekly_stats.loc[week, package] = max(stats_package[header] for header in headers)
        if len(last_weeks) > 1:
            fig = go.Figure()
            for package in weekly_stats.columns:
                weekly_stats_package = weekly_stats[package]
                fig.add_scatter(
                    x=last_weeks[1:], y=np.diff(weekly_stats_package), mode="lines+markers",
                    name=packages[package]["title"])
            html_buffer = io.StringIO()
            fig.write_html(html_buffer, full_html=False)
            return [nodes.raw(text=html_buffer.getvalue(), format="html")]
        else:
            return [nodes.raw(text="Stats not available", format="html")]

def on_build_finished(app, exc):
    if exc is None and app.builder.format == "html":
        # Unescape at symbol
        subprocess.run(
            "find " + app.outdir + " -type f -not -path '*/\.git/*' -exec sed -i 's/%40/@/g' {} +",
            shell=True)
        subprocess.run(  # undo incorrect escape in plotly js
            "sed -i 's/t@0=/t%400=/g' " + app.outdir + "/packages.html",
            shell=True)
        # Mark current page as active
        subprocess.run(
            "find " + app.outdir + " -type f -not -path '*/\.git/*' -exec sed -i 's/"
            + '<li class="md-tabs__item"><a href="#" class="md-tabs__link">'
            + "/"
            + '<li class="md-tabs__item md-tabs__item_current"><a href="#" class="md-tabs__link">'
            + "/g' {} +",
            shell=True)
        # Disable going to submenus on mobile
        subprocess.run(
            "find " + app.outdir + " -type f -not -path '*/\.git/*' -exec sed -i 's/"
            + 'id="__toc"'
            + "/"
            + 'id="__toc_disabled"'
            + "/g' {} +",
            shell=True)
        # Add further SEO tags
        seo_head = """
<script type="application/ld+json">
{
  "@context": "http://schema.org",
  "@type": "SoftwareApplication",
  "name": "FEM on Colab",
  "description": "FEM on Colab is a collection of packages that allows to easily install several finite element libraries on Google Colab. FEM on Colab is currently developed at Università Cattolica del Sacro Cuore by Dr. Francesco Ballarin.",
  "keywords": "fem-on-colab, Colab, finite element, jupyter",
  "softwareHelp": "https://fem-on-colab.github.io/",
  "operatingSystem": "Linux",
  "applicationCategory": "Simulation",
  "inLanguage": "en",
  "license": "https://opensource.org/licenses/MIT",
  "url": "https://github.com/fem-on-colab"
}
</script>

<meta property="og:title" content="FEM on Colab" />
<meta property="og:description" content="FEM on Colab is a collection of packages that allows to easily install several finite element libraries on Google Colab. FEM on Colab is currently developed at Università Cattolica del Sacro Cuore by Dr. Francesco Ballarin." />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="FEM on Colab" />
<meta property="og:url" content="https://fem-on-colab.github.io/" />
<meta property="og:image" content="https://fem-on-colab.github.io/_images/fem-on-colab-logo.png" />
"""
        index = os.path.join(app.outdir, "index.html")
        with open(index, "r") as f:
            index_content = f.read()
        index_content = index_content.replace("<head>", "<head>\n" + seo_head)
        with open(index, "w") as f:
            f.write(index_content)
        # Get package installation scripts from git
        releases_dir = os.path.join(app.outdir, "releases")
        os.makedirs(releases_dir, exist_ok=True)
        all_packages = packages.copy()
        all_packages.update(extra_packages)
        for package in list(all_packages.keys()):
            installation_suffixes = all_packages[package]["installation_suffixes"]
            if len(installation_suffixes) > 1:
                installation_suffixes += [""]
            else:
                assert installation_suffixes[0] == ""
            for suffix in installation_suffixes:
                if suffix == "":
                    package_install_name = package + "-install.sh"
                else:
                    package_install_name = package + "-install-" + suffix + ".sh"
                package_install_git = os.path.join("releases", package_install_name)
                package_install = os.path.join(releases_dir, package_install_name)
                is_link_process = subprocess.run(
                    "git ls-tree origin/gh-pages " + package_install_git,
                    shell=True, capture_output=True)
                if is_link_process.returncode != 0:
                    raise RuntimeError(
                        "Failed link checking for " + package + " at " + package_install_git + "\n"
                        + "stdout contains " + is_link_process.stdout.decode() + "\n"
                        + "stderr contains " + is_link_process.stderr.decode() + "\n")
                is_link = is_link_process.stdout.decode().startswith("120000")
                if not is_link:
                    install_copied = subprocess.run(
                        "git show origin/gh-pages:" + package_install_git + "> " + package_install,
                        shell=True, capture_output=True)
                    if install_copied.returncode != 0:
                        raise RuntimeError(
                            "Installation of " + package + " not found at " + package_install_git + "\n"
                            + "stdout contains " + install_copied.stdout.decode() + "\n"
                            + "stderr contains " + install_copied.stderr.decode() + "\n")
                    install_copied = subprocess.run(
                        "git show origin/gh-pages:" + package_install_git + "> " + package_install,
                        shell=True, capture_output=True)
                else:
                    get_link_path = subprocess.run(
                        "git show origin/gh-pages:" + package_install_git,
                        shell=True, capture_output=True)
                    if get_link_path.returncode != 0:
                        raise RuntimeError(
                            "Failed getting link path for " + package + " at " + package_install_git + "\n"
                            + "stdout contains " + get_link_path.stdout.decode() + "\n"
                            + "stderr contains " + get_link_path.stderr.decode() + "\n")
                    create_link = subprocess.run(
                        "cd " + releases_dir + " && ln -fs " + " " + get_link_path.stdout.decode()
                        + " " + os.path.relpath(package_install, releases_dir),
                        shell=True, capture_output=True)
                    if create_link.returncode != 0:
                        raise RuntimeError(
                            "Failed creating link for " + package + " at " + package_install_git + "\n"
                            + "stdout contains " + create_link.stdout.decode() + "\n"
                            + "stderr contains " + create_link.stderr.decode() + "\n")


create_sitemap_bak = sphinx_material.create_sitemap
def create_sitemap(app, exc):
    create_sitemap_bak(app, exc)
    if exc is None and app.builder.format == "html":
        # Add version and encoding to the top of sitemap.xml
        subprocess.run(
            "sed -i '1s/^/<?xml version=\"1.0\" encoding=\"UTF-8\"?>/' " + os.path.join(app.outdir, "sitemap.xml"),
            shell=True)
        # Remove trailing index.html from sitemap.xml
        subprocess.run(
            "sed -i 's|/index.html||g' " + os.path.join(app.outdir, "sitemap.xml"),
            shell=True)
        # Write robots.txt file
        with open(os.path.join(app.outdir, "robots.txt"), "w") as f:
            f.write("""Sitemap: https://fem-on-colab.github.io/sitemap.xml

User-agent: *
Disallow:
Allow: /
""")
sphinx_material.create_sitemap = create_sitemap


def setup(app):
    app.add_directive("packages", Packages)
    app.add_directive("stats", Stats)
    app.connect("build-finished", on_build_finished)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": False,
    }
