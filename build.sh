#!/bin/bash

git add .
git commit -m 'direnumerate 4.1-rc3'
git push -u origin dev
git tag v4.1-rc3
git push --tag
make clean
make upload
