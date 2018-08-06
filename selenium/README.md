# OpenStax QA Selenium Docker images

These images are heavy influenced by [SeleniumHQ][SeleniumHQ] docker images. However, there are some differences.

## Differences between our images and SeleniumHQ

The base image for the SeleniumHQ images are `ubuntu:16.04` and have selenium-server installed. We have based our images on `python:3.7.0-stretch` and do not have selenium-server installed. At this current time we run the tests locally so do not need to run a remote webdriver.

We also like to keep our Python version up-to-date as possible, hence the use of Python 3.7. The use of Debian stretch/jessie is consistent with other docker builds utilized by other OpenStax teams.

The SeleniumHQ docker build files are licensed under APLv2 which is included in our license file.

[SeleniumHQ]: https://github.com/SeleniumHQ/docker-selenium
