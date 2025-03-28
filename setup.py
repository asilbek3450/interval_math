from setuptools import setup, find_packages

setup(
    name="interval_math",
    version="0.1.1",
    packages=find_packages(),
    author="Asilbek Mirolimov",
    author_email="asilbekmirolimov@example.com",
    description="Intervallar bilan matematik amallarni bajaruvchi kutubxona",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/asilbek3450/interval_math",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
