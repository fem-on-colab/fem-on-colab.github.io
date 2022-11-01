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
        # Introduction to packages
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
        # Introduction to extra packages
        extra_intro = f"""
<input type="checkbox" name="extra-packages-toggle" id="extra-packages-toggle" class="extra-packages-toggle">
<label for="extra-packages-toggle" class="extra-packages-toggle-title">Package dependencies</label>
<div class="extra-packages-content">
<p>
A complete list of all dependencies is reported below. Users should typically not install any such dependency, since <b>FEM on Colab</b> automatically downloads and installs any required dependency of the aforementioned packages.
</p>
"""
        output.append(nodes.raw(text=extra_intro, format="html"))
        # Extra packages
        for package in extra_packages.keys():
            data = extra_packages[package]
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
        # Conclusion to extra packages
        output.append(nodes.raw(text="</div>", format="html"))
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
                colab_url = f"https://colab.research.google.com/github/fem-on-colab/fem-on-colab.github.io/blob/gh-pages/tests/{url}"
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
        if library == "boost":
            logo = "_static/images/boost-logo.png"
        elif library in ("dolfin", "dolfinx", "fenics", "fenicsx", "mshr") or library.startswith("dolfin ("):
            logo = "_static/images/fenics-logo.png"
        elif library in ("firedrake", "fireshape", "ROL"):
            logo = "_static/images/firedrake-logo.png"
        elif library == "gcc":
            logo = "_static/images/gcc-logo.png"
        elif library == "gmsh":
            logo = "_static/images/gmsh-logo.png"
        elif library == "h5py":
            logo = "_static/images/h5py-logo.png"
        elif library in ("itk", "itkwidgets"):
            logo = "_static/images/itk-logo.png"
        elif library == "mock":
            logo = "_static/images/mock-logo.png"
        elif library == "mpi4py":
            logo = "_static/images/mpi4py-logo.png"
        elif library == "multiphenics":
            logo = "_static/images/multiphenics-logo.png"
        elif library == "multiphenicsx" or library.startswith("multiphenicsx ("):
            logo = "_static/images/multiphenicsx-logo.png"
        elif library in ("ngsolve", "ngsxfem") or library.startswith("ngsolve ("):
            logo = "_static/images/ngsolve-logo.png"
        elif library == "occ":
            logo = "_static/images/occ-logo.png"
        elif library == "petsc4py":
            logo = "_static/images/petsc4py-logo.png"
        elif library == "pybind11" or library.startswith("pybind11 ("):
            logo = "_static/images/pybind11-logo.png"
        elif library == "RBniCS":
            logo = "_static/images/rbnics-logo.png"
        elif library == "slepc4py":
            logo = "_static/images/slepc4py-logo.png"
        elif library in ("vtk", "pyvista", "pythreejs"):
            logo = "_static/images/vtk-logo.png"
        else:
            raise RuntimeError("Invalid type " + library)
        return f'<img src="{logo}" style="vertical-align: middle; width: 25px">'

class Stats(Directive):

    def run(self):
        # Get release download stats from file, and convert it to a plot
        stats = pd.read_csv("_stats/stats.csv")
        first_day = None
        week_to_headers = dict()
        for header in stats.columns:
            if header.startswith("count_"):
                day = datetime.strptime(header.replace("count_", "").replace("_", "/"), "%Y/%m/%d")
                if first_day is None:
                    first_day = day
                else:
                    first_day = min(first_day, day)
                week = day.strftime("%Y-%U")
                if week not in week_to_headers:
                    week_to_headers[week] = list()
                week_to_headers[week].append(header)
        weeks = pd.date_range(
            start=first_day - timedelta(days=first_day.weekday()), end=datetime.now(), freq="W-MON")
        weeks = [week.strftime("%Y-%U") for week in weeks.tolist()[:-1]]
        weekly_stats = pd.DataFrame(0, columns=list(packages.keys()), index=weeks)
        for package in weekly_stats.columns:
            condition = stats.package.str.fullmatch(package)
            if sum(condition) > 0:
                stats_package = stats[condition].sum(axis=0)
                for (week, headers) in week_to_headers.items():
                    weekly_stats.loc[week, package] = max(stats_package[header] for header in headers)
        if len(weeks) > 1:
            fig = go.Figure()
            for package in weekly_stats.columns:
                weekly_stats_package = weekly_stats[package]
                fig.add_scatter(
                    x=weeks[1:], y=np.diff(weekly_stats_package), mode="lines+markers",
                    name=packages[package]["title"])
            if len(weeks) > 13:
                fig.update_xaxes(range=[len(weeks) - 13.5, len(weeks) - 1])
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
        # Get package installation scripts and test notebooks from git
        releases_dir = os.path.join(app.outdir, "releases")
        tests_dir = os.path.join(app.outdir, "tests")
        all_packages = packages.copy()
        all_packages.update(extra_packages)
        all_packages_files = dict()
        for package in list(all_packages.keys()):
            installation_suffixes = all_packages[package]["installation_suffixes"]
            if len(installation_suffixes) > 1:
                installation_suffixes += [""]
            else:
                assert installation_suffixes[0] == ""
            for suffix in installation_suffixes:
                for extension in (".sh", ".docker"):
                    if suffix == "":
                        package_install_name = package + "-install" + extension
                    else:
                        package_install_name = package + "-install-" + suffix + extension
                    package_install_git = os.path.join("releases", package_install_name)
                    package_install = os.path.join(releases_dir, package_install_name)
                    assert package_install not in all_packages_files
                    all_packages_files[package_install] = package_install_git
            for (_, test_notebook_name) in all_packages[package]["tests"].items():
                if not test_notebook_name.startswith("https://colab.research.google.com"):
                    test_notebook_git = os.path.join("tests", test_notebook_name)
                    test_notebook = os.path.join(tests_dir, test_notebook_name)
                    assert test_notebook not in all_packages_files
                    all_packages_files[test_notebook] = test_notebook_git
        for (package_file, package_file_git) in all_packages_files.items():
            os.makedirs(os.path.dirname(package_file), exist_ok=True)
            is_link_process = subprocess.run(
                "git ls-tree origin/gh-pages " + package_file_git,
                shell=True, capture_output=True)
            if is_link_process.returncode != 0:
                raise RuntimeError(
                    "Failed link checking for " + package_file_git + "\n"
                    + "stdout contains " + is_link_process.stdout.decode() + "\n"
                    + "stderr contains " + is_link_process.stderr.decode() + "\n")
            is_link = is_link_process.stdout.decode().startswith("120000")
            if not is_link:
                copy_file = subprocess.run(
                    "git show origin/gh-pages:" + package_file_git + "> " + package_file,
                    shell=True, capture_output=True)
                if copy_file.returncode != 0:
                    raise RuntimeError(
                        "Package file " + package_file_git + " not found\n"
                        + "stdout contains " + copy_file.stdout.decode() + "\n"
                        + "stderr contains " + copy_file.stderr.decode() + "\n")
                copy_file = subprocess.run(
                    "git show origin/gh-pages:" + package_file_git + "> " + package_file,
                    shell=True, capture_output=True)
            else:
                assert package_file.startswith(releases_dir)
                get_link_path = subprocess.run(
                    "git show origin/gh-pages:" + package_file_git,
                    shell=True, capture_output=True)
                if get_link_path.returncode != 0:
                    raise RuntimeError(
                        "Failed getting link path for " + package_file_git + "\n"
                        + "stdout contains " + get_link_path.stdout.decode() + "\n"
                        + "stderr contains " + get_link_path.stderr.decode() + "\n")
                create_link = subprocess.run(
                    "cd " + releases_dir + " && ln -fs " + " " + get_link_path.stdout.decode()
                    + " " + os.path.relpath(package_file, releases_dir),
                    shell=True, capture_output=True)
                if create_link.returncode != 0:
                    raise RuntimeError(
                        "Failed creating link for " + package_file_git + "\n"
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
