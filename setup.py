import sys
from setuptools import setup

setup(
    name = "socket-project",        # what you want to call the archive/egg
    version = "0.1",
    packages=[
        "client",
        "server",
        "common"
    ],    # top-level python modules you can import like
                                #   'import foo'
    dependency_links = [],      # custom links to a specific project
    install_requires=[],
    extras_require={},      # optional features that other packages can require
                            #   like 'helloworld[foo]'
    package_data = {},
    author="Yuval Saraf",
    author_email = "unimonkiez@gmail.com",
    description = "The familiar example program in Python",
    license = "BSD",
    keywords= "socket project university",
    url = "http://github.com/unimonkiez/socket-project",
    entry_points = {
        "console_scripts": [        # command-line executables to expose
            "client = client.main:main",
            "server = server.main:main",
        ],
        "gui_scripts": []       # GUI executables (creates pyw on Windows)
    }
)
