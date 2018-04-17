#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Camera import Camera

from PIL import Image
import os, subprocess

class CameraGphoto2CommandLine(Camera):

    def __init__(self):

        super().__init__()

        self.hasPreview = False
        self.hasIdle = False

        if os.access('/dev/shm', os.W_OK):
            self._tmp_filename = '/dev/shm/photobooth.jpg'
        else:
            self._tmp_filename = '/tmp/photobooth.jpg'

        self.setActive()


    def setActive(self):

        print(self._callGphoto('-a', '/dev/null'))


    def getPicture(self):
        
        self._callGphoto('--capture-image-and-download', self._tmp_filename)
        return Image.open(self._tmp_filename)


    def _callGphoto(self, action, filename):

        cmd = 'gphoto2 --force-overwrite --quiet ' + action + ' --filename ' + filename
        return subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)