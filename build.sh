#!/usr/bin/env bash

RELEASE_VERSION=$1
COMMIT_ID=$2

PROJECT_NAME=q-e

GIT_URI=https://gitlab.com/QEF/q-e.git

TMP_DIR=tmp
WORKING_DIR=$TMP_DIR/${PROJECT_NAME}-${COMMIT_ID}
BUILD_DIR=tmp/build-$RELEASE_VERSION

mkdir -p $TMP_DIR

cd $TMP_DIR
wget https://gitlab.com/QEF/q-e/-/archive/${COMMIT_ID}/q-e-${COMMIT_ID}.tar.gz
tar xzvf q-e-${COMMIT_ID}.tar.gz
cd q-e-${COMMIT_ID}
wget http://www-k3.ijs.si/kokalj/pwgui/download/PWgui-6.1.tgz
tar xzvf PWgui-6.1.tgz
./configure
make doc
cd ..
cd ..

cd qe-docset
./generate.sh -v ../$RELEASE_VERSION -i ../$WORKING_DIR
mv build ../$BUILD_DIR
cd -

mkdir -p build/version/$RELEASE_VERSION
cp $BUILD_DIR/QuantumESPRESSO.tgz build/version/$RELEASE_VERSION/

rm -r $TMP_DIR/q-e-${COMMIT_ID}
rm -r $TMP_DIR/q-e-${COMMIT_ID}.tar.gz