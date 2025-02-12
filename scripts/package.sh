#!/usr/bin/env sh

rm -rf ../package && mkdir ../package
pip install -r ../requirements.txt -t ../package
cp -r ../lambda/* ../package/