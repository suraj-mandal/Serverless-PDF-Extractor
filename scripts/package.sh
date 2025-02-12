#!/usr/bin/env sh

rm -rf ./terraform/package && mkdir ./terraform/package
pip install -r requirements.txt -t ./terraform/package
cp -r lambda/* ./terraform/package/