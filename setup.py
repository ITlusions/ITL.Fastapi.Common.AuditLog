from setuptools import setup, find_packages

setup(
    name="fastapi-auditlog",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi",
    ],
    author="Niels Weistra - ITlusions",
    author_email="n.weistra@itlusions.nl",
    description="Een FastAPI-middleware voor audit logging",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/itlusions/ITL.FastApi.Common.AuditLog",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)