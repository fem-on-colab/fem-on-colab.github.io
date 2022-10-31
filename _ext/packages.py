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
            "dolfin (checkpointing capabilities)": "fenics/test-dolfin-checkpoint.ipynb",
            "dolfin (catching C++ errors)": "fenics/test-dolfin-cpp-error.ipynb",
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
            "multiphenicsx (with plotly)": "https://colab.research.google.com/github/multiphenics/multiphenics.github.io/blob/open-in-colab-multiphenicsx/tutorials/01_block_poisson/tutorial_block_poisson.ipynb",
            "multiphenicsx (with pyvista)": "https://colab.research.google.com/github/multiphenics/multiphenics.github.io/blob/open-in-colab-multiphenicsx/tutorials/03_lagrange_multipliers/tutorial_lagrange_multipliers_interface.ipynb"
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
            "ROL": "firedrake/test-rol.ipynb",
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
        "tests": {
            "boost": "boost/test.ipynb",
        },
    },
    "gcc": {
        "installation_suffixes": [""],
        "tests": {
            "gcc": "gcc/test.ipynb",
        },
    },
    "h5py": {
        "installation_suffixes": [""],
        "tests": {
            "h5py": "h5py/test.ipynb",
        },
    },
    "itk": {
        "installation_suffixes": [""],
        "tests": {
            "itk": "itk/test-itk.ipynb",
            "itkwidgets": "itk/test-itkwidgets.ipynb",
        },
    },
    "mock": {
        "installation_suffixes": [""],
        "tests": {
            "mock": "mock/test.ipynb",
        },
    },
    "mpi4py": {
        "installation_suffixes": [""],
        "tests": {
            "mpi4py": "mpi4py/test.ipynb",
        },
    },
    "occ": {
        "installation_suffixes": [""],
        "tests": {
            "occ": "occ/test.ipynb",
        },
    },
    "petsc4py": {
        "installation_suffixes": ["real", "complex"],
        "tests": {
            "petsc4py": "petsc4py/test.ipynb",
        },
    },
    "pybind11": {
        "installation_suffixes": [""],
        "tests": {
            "pybind11 (with default compiler)": "pybind11/test-none.ipynb",
            "pybind11 (exporting g++ compiler)": "pybind11/test-gpp.ipynb",
            "pybind11 (exporting mpicxx compiler)": "pybind11/test-mpicxx.ipynb",
        },
    },
    "slepc4py": {
        "installation_suffixes": ["real", "complex"],
        "tests": {
            "slepc4py": "slepc4py/test.ipynb",
        },
    },
    "vtk": {
        "installation_suffixes": [""],
        "tests": {
            "vtk": "vtk/test-vtk.ipynb",
            "pyvista": "vtk/test-pyvista.ipynb",
            "pythreejs": "vtk/test-pythreejs.ipynb",
        },
    },
}
