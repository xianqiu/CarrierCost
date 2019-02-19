from distutils.core import setup


setup(
    name='carriercost',
    version=__import__('carriercost').__version__,
    description="Calculate carrier cost.",
    author='qx3501332',
    author_email='x.qiu@qq.com',
    license="MIT License",
    packages=['carriercost'],
    install_requires=['addlib'],
    include_package_date=True,
    zip_safe=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)