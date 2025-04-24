from setuptools import find_packages, setup

setup(
    name="virtualhome",
    version="2.2.4.dev1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "certifi",
        "chardet",
        "idna",
        "numpy==2.2.4",
        "opencv-python==4.11.0.86",
        "Pillow",
        "requests",
        "termcolor",
        "tqdm",
        "urllib3",
        "plotly",
        "networkx",
    ],  # And any other dependencies required
)
