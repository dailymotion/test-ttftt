FROM golang:1.11

RUN go get github.com/aktau/github-release

LABEL "name"="github-release"
LABEL "maintainer"="Stan Chollet <stanislas.chollet@gmail.com>"
LABEL "version"="1.0.0"

LABEL "com.github.actions.name"="Github Release"
LABEL "com.github.actions.description"="Create a release on github"
LABEL "com.github.actions.icon"="upload"
LABEL "com.github.actions.color"="green"

COPY "entrypoint.sh" "/entrypoint.sh"

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD [""]
