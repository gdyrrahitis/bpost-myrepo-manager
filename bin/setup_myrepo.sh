#!/bin/sh

cwdir="$( dirname -- "$0"; )"

echo "cloning submodules"
git submodule update --init --recursive

echo "setup dev resources"
/bin/sh $cwdir/setup.sh "$cwdir/../lib/myrepo" "myrepo"
