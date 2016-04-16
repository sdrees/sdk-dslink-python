from setuptools import setup

setup(
    name="dslink",
    version="0.7.0-rc1",
    description="DSLink SDK for Python",
    url="http://github.com/IOT-DSA/sdk-dslink-python",
    author="Logan Gorence",
    author_email="l.gorence@dglogik.com",
    license="Apache 2.0",
    packages=[
        "dslink"
    ],
    install_requires=[
        "autobahn == 0.12.1",
        "pyelliptic == 1.5.7",
        "requests == 2.9.1",
        "twisted == 16.1.1",
        "zope.interface == 4.1.3"
    ],
    use_2to3=True
)
