#!/bin/sh

SPECS_DIR=~/rpmbuild/SPECS
SRC_DIR=~/Projects/aircrack-ng

cd $SRC_DIR
svn update
VERSION=1.1_svn`svn info| grep Revision | cut -d' ' -f2`

rm -f ~/rpmbuild/SOURCES/aircrack-ng-*
tar  -jcvf ~/rpmbuild/SOURCES/aircrack-ng-$VERSION.tar.bz2 -C ~/Projects aircrack-ng

cd $SPECS_DIR
rpmbuild --define "version $VERSION" -bb aircrack-ng.spec

