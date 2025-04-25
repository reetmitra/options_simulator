from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="options_simulator",
    version="0.1.0",
    author="Reet Mitra",
    author_email="reetmitra@u.nus.edu",
    description="A Python package for options pricing and analysis using the Black-Scholes model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/reetmitra/options_simulator",
    packages=find_packages(where="."),
    package_dir={"": "."},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial :: Investment",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
) 
