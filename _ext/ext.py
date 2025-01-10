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
from outage import issues
import sphinx_material

class Packages(Directive):

    def run(self):
        output = list()
        # Introduction to packages
        if len(issues) > 0:
            intro = f"""
<div class="package-card" style="background-color: #dc143c; box-shadow: 0 4px 8px 0 #f8b5c2;">
  <div class="package-logo">
    <img src="_static/images/outage.png" style="vertical-align: middle; width: 100px">
  </div>
  <div class="package-content">
    <h3 class="package-title">
      A temporary outage may be affecting package availability
    </h3>
    See {", ".join([self._issue_link(issue) for issue in issues])} for more details.
  </div>
</div>
"""
        else:
            intro = ""
        intro += f"""
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
        # Test downloads
        test_downloads = f"""
<input type="checkbox" name="test-downloads-toggle" id="test-downloads-toggle" class="test-downloads-toggle">
<label for="test-downloads-toggle" class="test-downloads-toggle-title">All tests</label>
<div class="test-downloads-content">
<p>
For convenience, text files containing links to all <b>FEM on Colab</b> tests can be downloaded below:
<ul>
    <li><a href="tests_packages.txt">Tests for end user packages</a></li>
    <li><a href="tests_extra_packages.txt">Tests for extra packages</a></li>
</ul>
</p>
</div>
"""
        output.append(nodes.raw(text=test_downloads, format="html"))
        return output

    @classmethod
    def _card(cls, package, title, installation, installation_suffixes, buttons):
        if len(installation_suffixes) == 1:
            assert installation_suffixes[0] in ("", "real"), (
                f"Invalid suffix {installation_suffixes[0]}, expected blank or real")
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
            dropdown += f"""
        <li><a href="{cls._colab_url(url)}" target="_blank">{cls._library_image(library)} {library}</a></li>
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
    def _colab_url(url):
        if not url.startswith("https://colab.research.google.com"):
            return f"https://colab.research.google.com/github/fem-on-colab/fem-on-colab.github.io/blob/gh-pages/tests/{url}"
        else:
            return url

    @staticmethod
    def _issue_link(issue):
        return f'<a href="https://github.com/fem-on-colab/fem-on-colab/issues/{issue}" target="_blank" style="color: white">issue #{issue}</a>'

    @staticmethod
    def _library_image(library):
        if library == "boost":
            logo = "_static/images/boost-logo.png"
        elif library in ("dolfin", "dolfinx", "fenics", "fenicsx", "mshr") or library.startswith("dolfin ("):
            logo = "_static/images/fenics-logo.png"
        elif library in ("firedrake", "fireshape", "irksome", "ROL"):
            logo = "_static/images/firedrake-logo.png"
        elif library == "gcc":
            logo = "_static/images/gcc-logo.png"
        elif library == "gmsh":
            logo = "_static/images/gmsh-logo.png"
        elif library == "h5py":
            logo = "_static/images/h5py-logo.png"
        elif library == "mock":
            logo = "_static/images/mock-logo.png"
        elif library == "mpi4py":
            logo = "_static/images/mpi4py-logo.png"
        elif library == "multiphenics":
            logo = "_static/images/multiphenics-logo.png"
        elif library == "multiphenicsx" or library.startswith("multiphenicsx ("):
            logo = "_static/images/multiphenicsx-logo.png"
        elif library in ("netgen", "ngsolve", "ngsxfem", "ngspetsc") or library.startswith("ngsolve ("):
            logo = "_static/images/ngsolve-logo.png"
        elif library == "occ":
            logo = "_static/images/occ-logo.png"
        elif library == "petsc4py":
            logo = "_static/images/petsc4py-logo.png"
        elif library == "pybind11" or library.startswith("pybind11 & nanobind ("):
            logo = "_static/images/pybind11-logo.png"
        elif library == "RBniCS":
            logo = "_static/images/rbnics-logo.png"
        elif library == "slepc4py":
            logo = "_static/images/slepc4py-logo.png"
        elif library in ("vtk", "pyvista", "adios2"):
            logo = "_static/images/vtk-logo.png"
        else:
            raise RuntimeError("Invalid type " + library)
        return f'<img src="{logo}" style="vertical-align: middle; width: 25px">'

class Stats(Directive):

    def run(self):
        def get_week_representation(day: datetime.date) -> str:
            """
            Get the week representation year-week number.

            Uses day.isocalendar() rather than day.strftime("%Y-%W") to prevent
            wrong identification of the (week number, year) pair on the first week
            of the year, see the documentation of datetime.date.isocalendar().
            """
            isocalendar_tuple = day.isocalendar()
            return f"{isocalendar_tuple.year}-{isocalendar_tuple.week}"

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
                week = get_week_representation(day)
                if week not in week_to_headers:
                    week_to_headers[week] = list()
                week_to_headers[week].append(header)
        weeks = pd.date_range(
            start=first_day - timedelta(days=first_day.weekday()), end=datetime.now(), freq="W-MON").tolist()[:-1]
        weeks_str = [get_week_representation(week) for week in weeks]
        weekly_stats = pd.DataFrame(0, columns=list(packages.keys()), index=weeks_str)
        for package in weekly_stats.columns:
            condition = stats.package.str.fullmatch(package)
            if sum(condition) > 0:
                stats_package = stats[condition].sum(axis=0)
                for (week, headers) in week_to_headers.items():
                    weekly_stats.loc[week, package] = max(stats_package[header] for header in headers)
        if len(weeks) > 1:
            fig = go.Figure()
            max_downloads = 0
            for package in weekly_stats.columns:
                weekly_stats_package = weekly_stats[package]
                weekly_stats_package_diff = weekly_stats_package.diff().to_numpy()
                fig.add_scatter(
                    x=weeks[1:], y=weekly_stats_package_diff, mode="lines+markers",
                    name=packages[package]["title"])
                if len(weeks) > 13:
                    max_downloads = max(max_downloads, np.max(weekly_stats_package_diff[-14:]))
                else:
                    max_downloads = max(max_downloads, np.max(weekly_stats_package_diff))
            milliseconds_in_one_week = 604800000
            fig.update_xaxes(tickformat="%Y-%W", dtick=milliseconds_in_one_week)
            if len(weeks) > 13:
                fig.update_xaxes(
                    tick0=weeks[-14], range=[weeks[-14] - timedelta(days=3), weeks[-1] + timedelta(days=3)])
            else:
                fig.update_xaxes(tick0=weeks[0])
            fig.update_yaxes(tick0=- 0.1 * max_downloads, range=[- 0.1 * max_downloads, 1.1 * max_downloads])
            html_buffer = io.StringIO()
            fig.write_html(html_buffer, full_html=False)
            return [nodes.raw(text=html_buffer.getvalue(), format="html")]
        else:
            return [nodes.raw(text="Stats not available", format="html")]

def on_build_finished(app, exc):
    if exc is None and app.builder.format == "html":
        # Unescape at symbol
        subprocess.run(
            "find " + str(app.outdir) + r" -type f -not -path '*/\.git/*' -exec sed -i 's/%40/@/g' {} +",
            shell=True)
        subprocess.run(  # undo incorrect escape in plotly js
            "sed -i 's/t@0=/t%400=/g' " + str(app.outdir) + "/packages.html",
            shell=True)
        # Mark current page as active
        subprocess.run(
            "find " + str(app.outdir) + r" -type f -not -path '*/\.git/*' -exec sed -i 's/"
            + '<li class="md-tabs__item"><a href="#" class="md-tabs__link">'
            + "/"
            + '<li class="md-tabs__item md-tabs__item_current"><a href="#" class="md-tabs__link">'
            + "/g' {} +",
            shell=True)
        # Disable going to submenus on mobile
        subprocess.run(
            "find " + str(app.outdir) + r" -type f -not -path '*/\.git/*' -exec sed -i 's/"
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
  "description": "FEM on Colab is a collection of packages that allows to easily install several finite element libraries on Google Colab. FEM on Colab is currently developed at Università Cattolica del Sacro Cuore by Prof. Francesco Ballarin.",
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
<meta property="og:description" content="FEM on Colab is a collection of packages that allows to easily install several finite element libraries on Google Colab. FEM on Colab is currently developed at Università Cattolica del Sacro Cuore by Prof. Francesco Ballarin." />
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
            if len(installation_suffixes) == 1:
                assert installation_suffixes[0] in ("", "real"), (
                    f"Invalid suffix {installation_suffixes[0]}, expected blank or real")
            for suffix in installation_suffixes:
                for extension in (".sh", ".docker"):
                    if suffix == "":
                        package_install_name = package + "-install" + extension
                    else:
                        package_install_name = package + "-install-" + suffix + extension
                    package_install_git = os.path.join("releases", package_install_name)
                    package_install = os.path.join(releases_dir, package_install_name)
                    assert package_install not in all_packages_files, f"Could not find {package_install}"
                    all_packages_files[package_install] = package_install_git
            for (_, test_notebook_name) in all_packages[package]["tests"].items():
                if not test_notebook_name.startswith("https://colab.research.google.com"):
                    test_notebook_git = os.path.join("tests", test_notebook_name)
                    test_notebook = os.path.join(tests_dir, test_notebook_name)
                    assert test_notebook not in all_packages_files, f"Could not find {test_notebook}"
                    all_packages_files[test_notebook] = test_notebook_git
        for (package_file, package_file_git) in all_packages_files.items():
            os.makedirs(os.path.dirname(package_file), exist_ok=True)
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
        # Write out helper text files containing links to all test notebooks
        for (packages_dict, packages_filename) in zip((packages, extra_packages), ("packages", "extra_packages")):
            with open(os.path.join(app.outdir, "tests_" + packages_filename + ".txt"), "w") as f:
                for package in packages_dict.keys():
                    f.write("=" * (len(package) + 12) + "\n")
                    f.write("----- " + package + " -----\n")
                    data = packages_dict[package]
                    for (_, url) in data["tests"].items():
                        f.write(Packages._colab_url(url) + "?authuser=0\n")
                    f.write("=" * (len(package) + 12) + "\n")
                    f.write("\n")


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
