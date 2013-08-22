        # -*- coding: utf-8 -*-
"""
Setuptools script for nozama-cloudsearch-data (nozama.cloudsearch.data)

"""

from setuptools import setup, find_packages

# Get the version from the source or the cached egg version:
import json
import ConfigParser
cp = ConfigParser.ConfigParser()
try:
    cp.read('../eggs_version.ini')
    version = dict(cp.items('default'))['version']
except:
    # inside and egg, read the cache version instead.
    with file("cached_version.json", "r") as fd:
        version = json.loads(fd.read())['egg_version']
else:
    # write out the version so its cached for in egg use:
    with file("cached_version.json", "w") as fd:
        fd.write(json.dumps(dict(egg_version=version)))


Name = 'nozama-cloudsearch-data'
ProjectUrl = ""
Version = version
Author = ''
AuthorEmail = 'everyone at body dot co dot uk'
Maintainer = ''
Summary = ' nozama-cloudsearch-data '
License = ''
Description = Summary
ShortDescription = Summary

needed = [
    'evasion-common==1.0.1',
    'requests==0.14',
    'cmdln',
    'pymongo',
]

test_needed = [
]

test_suite = 'nozama.cloudsearch.data.tests'

EagerResources = [
    'nozama',
]

ProjectScripts = [
]

PackageData = {
    '': ['*.*'],
}

EntryPoints = {
}


setup(
    url=ProjectUrl,
    name=Name,
    zip_safe=False,
    version=Version,
    author=Author,
    author_email=AuthorEmail,
    description=ShortDescription,
    long_description=Description,
    classifiers=[
        "Programming Language :: Python",
    ],
    license=License,
    scripts=ProjectScripts,
    install_requires=needed,
    tests_require=test_needed,
    test_suite=test_suite,
    include_package_data=True,
    packages=find_packages(),
    package_data=PackageData,
    eager_resources=EagerResources,
    entry_points=EntryPoints,
    namespace_packages=['nozama', 'nozama.cloudsearch'],
)