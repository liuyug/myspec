#!/bin/sh

RPMBUILD=$HOME/rpmbuild

cd $RPMBUILD/SOURCES
if [ -d "$RPMBUILD/SOURCES/codeblocks" ]; then
    cd codeblocks
    svn update
else
    svn checkout http://svn.code.sf.net/p/codeblocks/code/trunk codeblocks
    cd codeblocks
fi

VERSION=12.11_svn`svn info| grep Revision | cut -d' ' -f2`

rpmbuild --define "version $VERSION" -bb $RPMBUILD/SPECS/codeblocks.spec

