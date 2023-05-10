from setuptools import setup, PEP420PackageFinder

# Only include packages under the 'aizwei' namespace. Do not include tests,
# benchmarks, etc.
packages = [
    package
    for package in PEP420PackageFinder.find()
    if package.startswith("aizwei")
]

setup(
    name='aizwei',
    version='0.1.0',
    description='AI Zwei SDK',
    url='',
    author='AI Zwei',
    author_email='support@aizwei.com',
    license="Apache 2.0",
    packages=packages,
    install_requires=['requests',
                      ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)