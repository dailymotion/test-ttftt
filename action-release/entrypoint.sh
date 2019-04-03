#!/bin/sh

cd /github/workspace

# Copy all files to USER Home, so that they are available for later actions
echo "we are going to deploy the $VERSION"

if [ -f changelogs/${VERSION} ]; then
    echo "Deploy with changelog"
    desc=$(cat changelogs/${VERSION}.md)
    github-release release \
        --user $USERNAME \
        --repo $REPOSITORY \
        --tag $VERSION \
        --name $VERSION \
        --description "${desc}"
else
    echo "Deploy without changelog"
    github-release release \
        --user $USERNAME \
        --repo $REPOSITORY \
        --tag $VERSION \
        --name $VERSION
fi