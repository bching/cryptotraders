from setuptools import setup, find_packages

setup(
    name='cryptotraders',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'Flask',
    ],
)
