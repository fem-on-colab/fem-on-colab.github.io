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
        "tests": {
            "dolfin": "fenics/test-dolfin.ipynb",
            "mshr": "fenics/test-mshr.ipynb",
            "multiphenics": "fenics/test-multiphenics.ipynb",
            "RBniCS": "fenics/xtest-rbnics.ipynb",
        },
    },

    "fenicsx": {
        "title": "FEniCSx",
        "installation": """
try:
    import dolfinx
except ImportError:
    !wget "https://fem-on-colab.github.io/releases/fenicsx-install.sh" -O "/tmp/fenicsx-install.sh" && bash "/tmp/fenicsx-install.sh"
    import dolfinx
""",
        "tests": {
            "dolfinx": "fenicsx/test-dolfinx.ipynb",
            "dolfinx with pyvista": "fenicsx/test-dolfinx-pyvista.ipynb",
            "multiphenicsx": "fenicsx/test-multiphenicsx.ipynb",
        },
    },

    "firedrake": {
        "title": "firedrake",
        "installation": """
try:
    import firedrake
except ImportError:
    !wget "https://fem-on-colab.github.io/releases/firedrake-install.sh" -O "/tmp/firedrake-install.sh" && bash "/tmp/firedrake-install.sh"
    import firedrake
""",
        "tests": {
            "firedrake": "firedrake/test-firedrake.ipynb",
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
        "tests": {
            "ngsolve": "ngsolve/test-ngsolve.ipynb",
        },
    },
}
extra_packages = [
    "boost",
    "gcc",
    "h5py",
    "mock",
    "mpi4py",
    "petsc4py",
    "pybind11",
    "slepc4py",
]
