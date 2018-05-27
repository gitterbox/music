#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

import sys, os
from PIL import Image

class Mp3Tools:

    def verifyCover(self, myfile):
        pass


# get workdir from first arg or use current dir 
if (len(sys.argv) > 1):
    rootDir = sys.argv[1]
else:
    rootDir = os.path.abspath(os.path.dirname(sys.argv[0]))

#result_filenames = [os.path.join(dp, f) for dp, dn, filenames in os.walk(rootDir) for f in filenames if os.path.splitext(f)[1] == '.mp3']

def resize_image(infile, size):
    try:
        image = Image.open(infile)
        image.save(infile+"_orig", "JPEG")
        image.thumbnail(size, Image.ANTIALIAS)
        image.save(infile, "JPEG")
    except IOError:
        print("cannot create thumbnail for '%s'" % infile)

def image_size(infile):
    #import pdb; pdb.set_trace()
    try:
        imagesize = Image.open(infile).size
        return imagesize
    except IOError:
        print("Error during image open")


# main
for dirName, subdirList, fileList in os.walk(rootDir):
    foundFolderJpg=False
    for fname in fileList:
        if fname.lower() == "folder.jpg":
            foundFolderJpg=True
            print("OK directory {} {}".format(dirName, image_size(dirName+"/"+fname)))

    if not foundFolderJpg and dirName is not rootDir: print("NOT OK directory {} folder.jpg:{} ".format(dirName, foundFolderJpg))
