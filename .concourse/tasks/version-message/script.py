#!/usr/bin/env python
import json
import os

from string import Template

ATC_EXTERNAL_URL = os.environ.get("ATC_EXTERNAL_URL")
BUILD_TEAM_NAME = os.environ.get("BUILD_TEAM_NAME")
BUILD_PIPELINE_NAME = os.environ.get("BUILD_PIPELINE_NAME")
BUILD_JOB_NAME = os.environ.get("BUILD_JOB_NAME")
BUILD_NAME = os.environ.get("BUILD_NAME")

def build_concourse_url():
    return f"{ATC_EXTERNAL_URL}/teams/{BUILD_TEAM_NAME}/pipelines/" \
           f"{BUILD_PIPELINE_NAME}/jobs/{BUILD_JOB_NAME}/builds/" \
           f"{BUILD_NAME or BUILD_PIPELINE_NAME or BUILD_JOB_NAME}"


message_template = """:female-detective: A new version of chromedriver $version 
has been detected. Builds have been started in Concourse. Watch the build status
here: $build_url
"""

template = Template(message_template)

with open("./chromedriver-latest/version", "r") as infile:
    chromedriver_version = infile.read()

print(
    template.substitute(
        version=chromedriver_version,
        build_url=build_concourse_url(),
    )
)
