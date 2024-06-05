
.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  dev        Create a Python virtual environment"
	@echo "  clean       Remove the virtual environment"
	@echo "  help        Display this help message"

.PHONY: dev
dev:
	rm -rf .venv
	python3.11 -m venv .venv --upgrade-deps
	.venv/bin/pip3 install -r requirements.txt
	@echo "Virtual environment installed!"

.PHONY: clean
clean:
	rm -rf .venv
	@echo "Virtual environment removed!"
