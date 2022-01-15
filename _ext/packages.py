packages = {
    "fenics": {
        "title": "FEniCS",
        "installation": """
try:
    import dolfin
except ImportError:
    !wget "https://fem-on-colab.github.io/releases/fenics-install.sh" -O "/tmp/fenics-install.sh" && bash "/tmp/fenics-install.sh"
    import dolfin
""",
        "installation_suffixes": [""],
        "tests": {
            "dolfin": "fenics/test-dolfin.ipynb",
            "mshr": "fenics/test-mshr.ipynb",
            "multiphenics": "fenics/test-multiphenics.ipynb",
            "RBniCS": "fenics/test-rbnics.ipynb",
        },
    },

    "fenicsx": {
        "title": "FEniCSx",
        "installation": """
try:
    import dolfinx
except ImportError:
    !wget "https://fem-on-colab.github.io/releases/fenicsx-install-SUFFIX.sh" -O "/tmp/fenicsx-install.sh" && bash "/tmp/fenicsx-install.sh"
    import dolfinx
""",
        "installation_suffixes": ["real", "complex"],
        "tests": {
            "dolfinx": "fenicsx/test-dolfinx.ipynb",
            "multiphenicsx (with pyvista)": "fenicsx/test-multiphenicsx.ipynb",
        },
    },

    "firedrake": {
        "title": "firedrake",
        "installation": """
try:
    import firedrake
except ImportError:
    !wget "https://fem-on-colab.github.io/releases/firedrake-install-SUFFIX.sh" -O "/tmp/firedrake-install.sh" && bash "/tmp/firedrake-install.sh"
    import firedrake
""",
        "installation_suffixes": ["real", "complex"],
        "tests": {
            "firedrake": "firedrake/test-firedrake.ipynb",
            "fireshape": "firedrake/test-fireshape.ipynb",
        },
    },

    "gmsh": {
        "title": "gmsh",
        "installation": """
try:
    import gmsh
except ImportError:
    !wget "https://fem-on-colab.github.io/releases/gmsh-install.sh" -O "/tmp/gmsh-install.sh" && bash "/tmp/gmsh-install.sh"
    import gmsh
""",
        "installation_suffixes": [""],
        "tests": {
            "gmsh": "gmsh/test.ipynb",
        },
    },

    "ngsolve": {
        "title": "ngsolve & ngsxfem",
        "installation": """
try:
    import ngsolve
except ImportError:
    !wget "https://fem-on-colab.github.io/releases/ngsolve-install.sh" -O "/tmp/ngsolve-install.sh" && bash "/tmp/ngsolve-install.sh"
    import ngsolve
""",
        "installation_suffixes": [""],
        "tests": {
            "ngsolve": "ngsolve/test-ngsolve.ipynb",
            "ngsolve (extras)": "ngsolve/test-ngsolve-extras.ipynb",
            "ngsxfem": "ngsolve/test-ngsxfem.ipynb",
        },
    },
}
extra_packages = {
    "boost": {
        "installation_suffixes": [""],
    },
    "gcc": {
        "installation_suffixes": [""],
    },
    "h5py": {
        "installation_suffixes": [""],
    },
    "mock": {
        "installation_suffixes": [""],
    },
    "mpi4py": {
        "installation_suffixes": [""],
    },
    "occ": {
        "installation_suffixes": [""],
    },
    "petsc4py": {
        "installation_suffixes": ["real", "complex"],
    },
    "pybind11": {
        "installation_suffixes": [""],
    },
    "slepc4py": {
        "installation_suffixes": ["real", "complex"],
    },
}
