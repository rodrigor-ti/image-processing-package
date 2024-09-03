from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt", "r") as f:

    requirementes = f.read().splitlines()

setup(
    name="image_processing_package",
    version="0.0.1",
    author="rodrigor-ti",
    author_email="rodrigo.oliveira.rodrigues@gmail.com",
    description="image_processing_package",
    long_description=page_description,
    long_description_content_type='text/markdown',
    url="https://github.com/rodrigor-ti/image-processing-package",
    packages=find_packages(),
    install_requires=requirementes,
    python_requires='>=3.8',
)