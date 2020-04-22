#!/usr/bin/env python
import os

from string import Template


def read_file(filename):
    with open(filename, "r") as infile:
        data = infile.read()
    return data


def build_concourse_build_url(atc_external_url,
                              built_team_name,
                              build_pipeline_name,
                              build_job_name,
                              build_name):
    return f"{atc_external_url}/teams/{build_team_name}/pipelines/{build_pipeline_name}/jobs/{build_job_name}/builds/{build_name}"


message_template = """:female-detective: A new version of chromedriver $version has been detected. 
Check $build_url for status.
"""

template = Template(message_template)

chromedriver_version = read_file("./chromedriver-latest/version")

# Read in all the concourse build meta into variables
atc_external_url = read_file("./meta/atc-external-url")
build_team_name = read_file("./meta/build-team-name")
build_pipeline_name = read_file("./meta/build-pipeline-name")
build_job_name = read_file("./meta/build-job-name")
build_name = read_file("./meta/build-name")

print(
    template.substitute(
        version=chromedriver_version,
        build_url=build_concourse_build_url(atc_external_url, 
                                            build_team_name, 
                                            build_pipeline_name,
                                            build_job_name,
                                            build_name)
    )
)
