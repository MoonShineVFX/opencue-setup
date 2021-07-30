#!/bin/bash
VER=0.8.8
wget https://github.com/AcademySoftwareFoundation/OpenCue/archive/refs/tags/v$VER.zip
unzip v$VER.zip &&  rm v$VER.zip
mv OpenCue-$VER opencue-source
