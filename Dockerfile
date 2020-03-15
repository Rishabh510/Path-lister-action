FROM python:3-slim AS build-env
ADD . /app
WORKDIR /app

# Setting for publish
LABEL "com.github.actions.name"="Path lister"
LABEL "com.github.actions.description"="List specific file paths in project"
LABEL "com.github.actions.icon"="list"
LABEL "com.github.actions.color"="red"

LABEL "repository"="https://github.com/Rishabh510/Path-lister-action.git"
LABEL "homepage"="https://github.com/Rishabh510/Path-lister-action.git"
LABEL "maintainer"="Rishabh Raizada <rishabhraizada5102000@gmail.com>"

# We are installing a dependency here directly into our app source dir
# RUN pip install --target=/app yamllint

# A distroless container image with Python and some basics like SSL certificates
# https://github.com/GoogleContainerTools/distroless
FROM gcr.io/distroless/python3-debian10
COPY --from=build-env /app /app
WORKDIR /app
ENV PYTHONPATH /app
CMD ["/app/main.py"]
