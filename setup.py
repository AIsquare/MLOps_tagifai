from pathlib import Path

from setuptools import find_namespace_packages, setup

BASE_DIR = Path(__file__).parent
print(BASE_DIR)
with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]

# docs_packages = ["mkdocs==1.3.0", "mkdocstrings==0.18.1"]

style_packages = ["black==22.3.0", "flake8==3.9.2", "isort==5.10.1"]
# setup.py
docs_packages = ["mkdocs==1.3.0", "mkdocstrings==0.18.1"]
test_packages = [
    "pytest==7.1.2",
    "pytest-cov==2.10.1"
]

setup(
    name="tagifai",
    version=0.1,
    description="Classify machine learning projects",
    author="Aamir Iqbal",
    author_email="aamir@aisquare.com",
    url="https://aamiriqbal.com",
    python_requires=">=3.7",
    install_requires=[required_packages],
    extras_require={
        "dev": docs_packages + style_packages,
        "docs": docs_packages,
        "test": test_packages,
    },
)
