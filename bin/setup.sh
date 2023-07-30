#!/bin/sh

# Usage: ./bin/setup.sh <path-to-git-repo> <name-of-bare>

cwdir="$( dirname -- "$0"; )"

REPO=$1
TARGET=$2
mkdir -p $cwdir/../_dev/git-server
mkdir -p $cwdir/../_dev/git-server/keys
mkdir -p $cwdir/../_dev/git-server/repos

# cloning bare repo to git-server/repos volume
git clone --bare $REPO $cwdir/../_dev/git-server/repos/$TARGET.git

# copying public key to git-server/keys volume
cp ~/.ssh/id_rsa.pub $cwdir/../_dev/git-server/keys