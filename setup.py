import os
from distutils.core import setup

version = '0.1.1'

setup(
    name="tornadomail",
    version=version,
    keywords=["tornado", "mail", "tornadomail", "asyncmail"],
    long_description=open(os.path.join(os.path.dirname(__file__),"README.md"), "r").read(),
    description="Asynchronous email sending library for Tornado. Port of django.mail.",
    author="Anton Agafonov",
    author_email="anton.agafonov@gmail.com",
    url="http://github.com/equeny/tornadomail",
    license="Apache Software License",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
    ],
    packages=['tornadomail', 'tornadomail.backends'],
    install_requires=['tornado>=2.1'],
    requires=['tornado (>=2.1)'],
    download_url="http://github.com/downloads/equeny/tornadomail/tornadomail-%s.tar.gz" % version,
)
