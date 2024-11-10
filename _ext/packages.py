packages = {
    "fenics": {
        "title": "FEniCS",
        "installation": """
try:
    import dolfin
except ImportError:
    !wget "https://fem-on-colab.github.io/releases/fenics-install-real.sh" -O "/tmp/fenics-install.sh" && bash "/tmp/fenics-install.sh"
    import dolfin
""",
        "installation_suffixes": ["real"],
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
            "irksome": "firedrake/test-irksome.ipynb",
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
        "title": "netgen, ngsolve, ngsxfem & ngsPETSc",
        "installation": """
try:
    import ngsolve
except ImportError:
    !wget "https://fem-on-colab.github.io/releases/ngsolve-install-SUFFIX.sh" -O "/tmp/ngsolve-install.sh" && bash "/tmp/ngsolve-install.sh"
    import ngsolve
""",
        "installation_suffixes": ["real", "complex"],
        "tests": {
            "ngsolve": "ngsolve/test-ngsolve.ipynb",
            "ngsolve (extras)": "ngsolve/test-ngsolve-extras.ipynb",
            "ngsxfem": "ngsolve/test-ngsxfem.ipynb",
            "ngspetsc": "ngsolve/test-ngspetsc.ipynb",
        },
    },
}
extra_packages = {
    "boost": {
        "title": "Boost",
        "installation": """
!wget "https://fem-on-colab.github.io/releases/boost-install.sh" -O "/tmp/boost-install.sh" && bash "/tmp/boost-install.sh"
""",
        "installation_suffixes": [""],
        "tests": {
            "boost": "boost/test.ipynb",
        },
    },
    "gcc": {
        "title": "GCC",
        "installation": """
!wget "https://fem-on-colab.github.io/releases/gcc-install.sh" -O "/tmp/gcc-install.sh" && bash "/tmp/gcc-install.sh"
""",
        "installation_suffixes": [""],
        "tests": {
            "gcc": "gcc/test.ipynb",
        },
    },
    "h5py": {
        "title": "HDF5 & h5py",
        "installation": """
!wget "https://fem-on-colab.github.io/releases/h5py-install.sh" -O "/tmp/h5py-install.sh" && bash "/tmp/h5py-install.sh"
import h5py
""",
        "installation_suffixes": [""],
        "tests": {
            "h5py": "h5py/test.ipynb",
        },
    },
    "mock": {
        "title": "Mock package",
        "installation": """
!wget "https://fem-on-colab.github.io/releases/mock-install.sh" -O "/tmp/mock-install.sh" && bash "/tmp/mock-install.sh"
import mock
""",
        "installation_suffixes": [""],
        "tests": {
            "mock": "mock/test.ipynb",
        },
    },
    "mpi4py": {
        "title": "openmpi & mpi4py",
        "installation": """
try:
    import mpi4py
except ImportError:
    !wget "https://fem-on-colab.github.io/releases/mpi4py-install.sh" -O "/tmp/mpi4py-install.sh" && bash "/tmp/mpi4py-install.sh"
    import mpi4py
""",
        "installation_suffixes": [""],
        "tests": {
            "mpi4py": "mpi4py/test.ipynb",
        },
    },
    "occ": {
        "title": "Open CASCADE Technology",
        "installation": """
!wget "https://fem-on-colab.github.io/releases/occ-install.sh" -O "/tmp/occ-install.sh" && bash "/tmp/occ-install.sh"
""",
        "installation_suffixes": [""],
        "tests": {
            "occ": "occ/test.ipynb",
        },
    },
    "petsc4py": {
        "title": "PETSc & petsc4py",
        "installation": """
try:
    import petsc4py
except ImportError:
    !wget "https://fem-on-colab.github.io/releases/petsc4py-install-SUFFIX.sh" -O "/tmp/petsc4py-install.sh" && bash "/tmp/petsc4py-install.sh"
    import petsc4py
""",
        "installation_suffixes": ["real", "complex"],
        "tests": {
            "petsc4py": "petsc4py/test.ipynb",
        },
    },
    "pybind11": {
        "title": "pybind11 & nanobind",
        "installation": """
!wget "https://fem-on-colab.github.io/releases/pybind11-install.sh" -O "/tmp/pybind11-install.sh" && bash "/tmp/pybind11-install.sh"
import pybind11
""",
        "installation_suffixes": [""],
        "tests": {
            "pybind11 & nanobind (with default compiler)": "pybind11/test-none.ipynb",
            "pybind11 & nanobind (exporting g++ compiler)": "pybind11/test-gpp.ipynb",
            "pybind11 & nanobind (exporting mpicxx compiler)": "pybind11/test-mpicxx.ipynb",
        },
    },
    "slepc4py": {
        "title": "SLEPc & slepc4py",
        "installation": """
try:
    import slepc4py
except ImportError:
    !wget "https://fem-on-colab.github.io/releases/slepc4py-install-SUFFIX.sh" -O "/tmp/slepc4py-install.sh" && bash "/tmp/slepc4py-install.sh"
    import slepc4py
""",
        "installation_suffixes": ["real", "complex"],
        "tests": {
            "slepc4py": "slepc4py/test.ipynb",
        },
    },
    "vtk": {
        "title": "VTK & pyvista",
        "installation": """
try:
    import vtk
except ImportError:
    !wget "https://fem-on-colab.github.io/releases/vtk-install.sh" -O "/tmp/vtk-install.sh" && bash "/tmp/vtk-install.sh"
    import vtk
""",
        "installation_suffixes": [""],
        "tests": {
            "vtk": "vtk/test-vtk.ipynb",
            "pyvista": "vtk/test-pyvista.ipynb",
            "adios2": "vtk/test-adios2.ipynb",
        },
    },
}
