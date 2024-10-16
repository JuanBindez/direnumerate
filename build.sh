#!/bin/bash

VERSION=4
PATCHLEVEL=1
SUBLEVEL=
EXTRAVERSION="-rc4"

BRANCH="dev"
MESSAGE="update test"

FULL_VERSION="$VERSION.$PATCHLEVEL.$SUBLEVEL$EXTRAVERSION"

git add .
git commit -m "Direnumerate $FULL_VERSION $MESSAGE"
git push -u origin $BRANCH
git tag v$FULL_VERSION
git push --tags
make clean
make upload

echo "Build $FULL_VERSION completed successfully!"