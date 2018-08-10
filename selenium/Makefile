# File is based on Makefile in SeleniumHQ/selenium-docker GitHub repo
ORG_NAME := openstax
VERSION := $(or $(VERSION),$(VERSION),1.0.0)
NAMESPACE := $(or $(NAMESPACE),$(NAMESPACE),selenium)
AUTHORS := $(or $(AUTHORS),$(AUTHORS),OpenStaxQA)
PLATFORM := $(shell uname -s)
BUILD_ARGS := $(BUILD_ARGS)
MAJOR := $(word 1,$(subst ., ,$(VERSION)))
MINOR := $(word 2,$(subst ., ,$(VERSION)))
MAJOR_MINOR_PATCH := $(word 1,$(subst -, ,$(VERSION)))

all: chrome

build: all

base:
	cd ./base && docker build $(BUILD_ARGS) -t $(ORG_NAME)/$(NAMESPACE)-base:$(VERSION) .

chrome: base generate_chrome
	cd ./chrome && docker build $(BUILD_ARGS) -t $(ORG_NAME)/$(NAMESPACE)-chrome:$(VERSION) .

generate_chrome:
	cd ./chrome && ./generate.sh chrome $(VERSION) $(ORG_NAME) $(NAMESPACE) $(AUTHORS)

tag_latest:
	docker tag $(ORG_NAME)/$(NAMESPACE)-base:$(VERSION) $(ORG_NAME)/$(NAMESPACE)-base:latest
	docker tag $(ORG_NAME)/$(NAMESPACE)-chrome:$(VERSION) $(ORG_NAME)/$(NAMESPACE)-chrome:latest

release_latest:
	docker push $(ORG_NAME)/$(NAMESPACE)-base:latest
	docker push $(ORG_NAME)/$(NAMESPACE)-chrome:latest

tag_major_minor:
	docker tag $(ORG_NAME)/$(NAMESPACE)-base:$(VERSION) $(ORG_NAME)/$(NAMESPACE)-base:$(MAJOR)
	docker tag $(ORG_NAME)/$(NAMESPACE)-base:$(VERSION) $(ORG_NAME)/$(NAMESPACE)-base:$(MAJOR).$(MINOR)
	docker tag $(ORG_NAME)/$(NAMESPACE)-base:$(VERSION) $(ORG_NAME)/$(NAMESPACE)-base:$(MAJOR_MINOR_PATCH)
	docker tag $(ORG_NAME)/$(NAMESPACE)-base:$(VERSION) $(ORG_NAME)/$(NAMESPACE)-chrome:$(MAJOR)
	docker tag $(ORG_NAME)/$(NAMESPACE)-base:$(VERSION) $(ORG_NAME)/$(NAMESPACE)-chrome:$(MAJOR).$(MINOR)
	docker tag $(ORG_NAME)/$(NAMESPACE)-base:$(VERSION) $(ORG_NAME)/$(NAMESPACE)-chrome:$(MAJOR_MINOR_PATCH)

release: tag_major_minor
	@if ! docker images $(ORG_NAME)/$(NAMESPACE)-base | awk '{ print $$2 }' | grep -q -F $(VERSION); then echo "$(ORG_NAME)/$(NAMESPACE)-base version $(VERSION) is not yet built. Please run 'make build'"; false; fi
	@if ! docker images $(ORG_NAME)/$(NAMESPACE)-chrome | awk '{ print $$2 }' | grep -q -F $(VERSION); then echo "$(ORG_NAME)/$(NAMESPACE)-base version $(VERSION) is not yet built. Please run 'make build'"; false; fi
	docker push $(ORG_NAME)/$(NAMESPACE)-base:$(VERSION)
	docker push $(ORG_NAME)/$(NAMESPACE)-base:$(MAJOR)
	docker push $(ORG_NAME)/$(NAMESPACE)-base:$(MAJOR).$(MINOR)
	docker push $(ORG_NAME)/$(NAMESPACE)-base:$(MAJOR_MINOR_PATCH)
	docker push $(ORG_NAME)/$(NAMESPACE)-chrome:$(VERSION)
	docker push $(ORG_NAME)/$(NAMESPACE)-chrome:$(MAJOR)
	docker push $(ORG_NAME)/$(NAMESPACE)-chrome:$(MAJOR).$(MINOR)
	docker push $(ORG_NAME)/$(NAMESPACE)-chrome:$(MAJOR_MINOR_PATCH)

.PHONY: \
	all \
	base \
	chrome \
