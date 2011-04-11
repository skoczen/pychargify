from setuptools import setup, find_packages

VERSION = (1, 0, 0)

# Dynamically calculate the version based on VERSION tuple
if len(VERSION)>2 and VERSION[2] is not None:
    str_version = "%d.%d_%s" % VERSION[:3]
else:
    str_version = "%d.%d" % VERSION[:2]

version= str_version

setup(
    name = 'pychargify',
    version = version,
    description = "pychargify",
    long_description = """This is a generic SDK for hooking up with the Chargify API""",
    author = 'David Gay i tello',
    author_email = 'david.gaytello@gmail.com',
    url = 'http://github.com/davidgit/pychargify',
    license = 'GNU General Public License',
    platforms = ['any'],
    classifiers = ['Development Status :: Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'],
    packages = find_packages(),
    include_package_data = True,
)
