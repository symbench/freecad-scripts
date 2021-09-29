#!/usr/bin/env python3
# Copyright (C) 2021, Miklos Maroti
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup

setup(
    name='freecad-scripts',
    version='0.1',
    packages=['freecad_scripts'],
    license='GPL 3',
    description="FreeCAD scripting and analysis",
    python_requires='>3.6',
    # do not list standard packages
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'freecad-scripts = freecad_scripts.__main__:run'
        ]
    }
)
