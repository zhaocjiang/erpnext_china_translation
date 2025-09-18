from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="erpnext_china_translation",
    version="0.0.1",
    description="ERPNext China Translation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Gemini",
    packages=find_packages(),
    include_package_data=True,
)
