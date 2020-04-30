# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import simplekml

kml=simplekml.Kml()
kml.newpoint(name="Sample", coords=[(10,10)])
kml.newpoint(name="Sample", coords=[(15,15)])

kml.save("C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\Extracted\\out\\points.kml")

