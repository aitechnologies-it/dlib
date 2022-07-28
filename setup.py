import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydlib", # Replace with your own username
    version="0.2.0",
    author="Luigi Di Sotto, Diego Giorgini",
    author_email="l.disotto@gmail.com, diego.giorgini@icloud.com",
    description="The Dictionary Library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aitechnologies-it/dlib",
    project_urls={
        "Bug Tracker": "https://github.com/aitechnologies-it/dlib/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
       "flatten-dict",
   ],
)
