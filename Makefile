DEFAULT_GOAL := all

.PHONY: all
all: setup_requirements

.PHONY: help
help: ## Displays this help
	@echo "This make file installs molecule requirements for role development."
	@echo "Targets:"
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' Makefile | \
		sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: setup-requirements
setup_requirements: ## Installs Python requirements for molecule
	-python3 -m venv .venv; \
	source .venv/bin/activate; \
	pip install -r molecule/requirements.txt; \

.PHONY: clean
clean: ## Removes the virtual env
	@echo "Cleaning up..."
	@rm -r -f tmp/ .venv
	@echo "All Done"
