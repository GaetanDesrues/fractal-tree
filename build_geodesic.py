from setuptools import setup
from Cython.Build import cythonize

setup(
    name="FractalTree_geo",
    setup_requires=["cython", "numpy"],
    install_requires=["numpy"],
    ext_modules=cythonize(
        "FractalTree/geodesic_.pyx",
        compiler_directives={"language_level": "3"},
    ),
)

# Run `python build_geodesic.py build_ext --inplace`