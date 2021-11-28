import os
import subprocess
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
                buttons=buttons
            )
            if "hide" not in data or not data["hide"]:
                output.append(nodes.raw(text=card_num, format="html"))
        return output

    @classmethod
    def _card(cls, package, title, installation, buttons):
        return f"""
<div class="package-card">
  <div class="package-logo">
    {cls._library_image(package)}
  </div>
  <div class="package-content">
    <h3 class="package-title">
      {title}
    </h3>
    <div class="package-installation">
{installation.lstrip().rstrip()}
    </div>
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
        <li><a href="https://colab.research.google.com/github/fem-on-colab/fem-on-colab/blob/main/{url}" target="_blank">{cls._library_image(library)} {library}</a></li>
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
        elif library == "firedrake":
            logo = "_static/images/firedrake-logo.png"
        elif library == "gmsh":
            logo = "_static/images/gmsh-logo.png"
        elif library == "multiphenics":
            logo = "_static/images/multiphenics-logo.png"
        elif library == "multiphenicsx":
            logo = "_static/images/multiphenicsx-logo.png"
        elif library == "ngsolve":
            logo = "_static/images/ngsolve-logo.png"
        elif library == "RBniCS":
            logo = "_static/images/rbnics-logo.png"
        else:
            raise RuntimeError("Invalid type " + library)
        return f'<img src="{logo}" style="vertical-align: middle; width: 25px">'

def on_build_finished(app, exc):
    if exc is None and app.builder.format == "html":
        # Unescape at symbol
        subprocess.run(
            "find " + app.outdir + " -type f -exec sed -i 's/%40/@/g' {} +",
            shell=True)
        # Mark current page as active
        subprocess.run(
            "find " + app.outdir + " -type f -exec sed -i 's/"
            + '<li class="md-tabs__item"><a href="#" class="md-tabs__link">'
            + "/"
            + '<li class="md-tabs__item md-tabs__item_current"><a href="#" class="md-tabs__link">'
            + "/g' {} +",
            shell=True)
        # Disable going to submenus on mobile
        subprocess.run(
            "find " + app.outdir + " -type f -exec sed -i 's/"
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
  "description": "FEM on Colab is a collection of packages that allows to easily install several finite element libraries on Google Colab. FEM on Colab is currently developed at Catholic University of the Sacred Heart by Dr. Francesco Ballarin.",
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
<meta property="og:description" content="FEM on Colab is a collection of packages that allows to easily install several finite element libraries on Google Colab. FEM on Colab is currently developed at Catholic University of the Sacred Heart by Dr. Francesco Ballarin." />
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
        for package in list(packages.keys()) + extra_packages:
            package_install_git = os.path.join("releases", package + "-install.sh")
            package_install = os.path.join(releases_dir, package + "-install.sh")
            install_copied = subprocess.call(
                "git show origin/gh-pages:" + package_install_git + "> " + package_install,
                shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            assert install_copied == 0, "Installation of " + package + " not found at " + package_install_git


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
sphinx_material.create_sitemap = create_sitemap


def setup(app):
    app.add_directive("packages", Packages)
    app.connect("build-finished", on_build_finished)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": False,
    }
