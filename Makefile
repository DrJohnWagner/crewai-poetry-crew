# Project configuration
PROJECT_NAME := crewai-poetry-crew
PYTHON := python3
VENV_DIR := .venv
PIP := uv pip
PYTHON_VENV := $(VENV_DIR)/bin/python
PYTEST := $(VENV_DIR)/bin/pytest

# File patterns and directories
PYTHON_FILES := src/**/*.py tests/**/*.py
TEST_FILES := tests/**/*.py
BACKUPS_DIR := backups/
CACHE_DIRS := __pycache__/ .pytest_cache/ src/**/__pycache__/ tests/**/__pycache__/
LOG_FILES := *.log log.txt

# Build artifacts and outputs
BUILD_DIR := build/
DIST_DIR := dist/

# Colors for output
GREEN := \033[0;32m
YELLOW := \033[1;33m
RED := \033[0;31m
NC := \033[0m # No Color

# Default target
.PHONY: help
help: ## Show this help message
	@echo "$(GREEN)📝 CrewAI Poetry Crew - Available Make Targets$(NC)"
	@echo "=================================================="
	@echo "$(YELLOW)🚀 Quick Start: make start$(NC) - Complete initial setup"
	@echo "$(YELLOW)🧪 Quick Test: make test$(NC)"
	@echo "$(YELLOW)▶️  Run Crew: make run$(NC)"
	@echo "$(YELLOW)💾 Backup: make backup$(NC) - Backup src directory"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "$(YELLOW)%-20s$(NC) %s\n", $$1, $$2}'

# =============================================================================
# SETUP AND ENVIRONMENT
# =============================================================================

.PHONY: start
start: ## Complete initial setup - create venv and install all dependencies
	@echo "$(GREEN)🚀 Starting complete project setup...$(NC)"
	@echo "$(YELLOW)Creating virtual environment...$(NC)"
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "$(GREEN)📚 Installing project dependencies...$(NC)"
	$(PIP) install -e .
	@echo "$(GREEN)🧪 Installing development dependencies...$(NC)"
	$(PIP) install pytest
	@echo "$(GREEN)✅ Validating installation...$(NC)"
	$(PYTHON_VENV) --version
	$(PIP) list | grep -E "(crewai|pytest)" || echo "$(YELLOW)⚠️  Some packages may not be installed$(NC)"
	@echo "$(GREEN)🎉 Setup complete!$(NC)"
	@echo "$(YELLOW)Next steps:$(NC)"
	@echo "  1. Activate environment: source $(VENV_DIR)/bin/activate"
	@echo "  2. Run tests: make test"
	@echo "  3. Run crew: make run"
	@echo "  4. View all targets: make help"

.PHONY: venv
venv: ## Create virtual environment (basic version)
	@echo "$(GREEN)Creating virtual environment...$(NC)"
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "$(GREEN)Virtual environment created. Activate with: source $(VENV_DIR)/bin/activate$(NC)"

.PHONY: install
install: venv ## Install dependencies
	@echo "$(GREEN)Installing dependencies...$(NC)"
	$(PIP) install -e .
	@echo "$(GREEN)Dependencies installed successfully$(NC)"

.PHONY: install-dev
install-dev: install ## Install development dependencies
	@echo "$(GREEN)Installing development dependencies...$(NC)"
	$(PIP) install pytest
	@echo "$(GREEN)Development dependencies installed$(NC)"

# =============================================================================
# TESTING
# =============================================================================

.PHONY: test
test: ## Run all tests
	@echo "$(GREEN)Running all tests...$(NC)"
	rm -rf $(CACHE_DIRS)
	@if [ ! -f $(PYTEST) ]; then \
		echo "$(RED)pytest not found. Run 'make install-dev' first.$(NC)"; \
		exit 1; \
	fi
	$(PYTEST) tests/ -v
	@echo "$(GREEN)All tests completed$(NC)"

.PHONY: test-fast
test-fast: ## Run tests with minimal output
	@echo "$(GREEN)Running fast tests...$(NC)"
	rm -rf $(CACHE_DIRS)
	$(PYTEST) tests/ -q

.PHONY: test-verbose
test-verbose: ## Run tests with maximum verbosity
	@echo "$(GREEN)Running verbose tests...$(NC)"
	rm -rf $(CACHE_DIRS)
	$(PYTEST) tests/ -vv --tb=long

# =============================================================================
# CREW EXECUTION
# =============================================================================

.PHONY: run
run: ## Run the CrewAI poetry crew
	@echo "$(GREEN)Running CrewAI poetry crew...$(NC)"
	$(PYTHON_VENV) -m crewai run
	@echo "$(GREEN)Crew execution completed$(NC)"

# =============================================================================
# CLEANING
# =============================================================================

.PHONY: clean
clean: ## Clean build artifacts and cache files
	@echo "$(GREEN)Cleaning build artifacts and cache files...$(NC)"
	rm -rf $(CACHE_DIRS)
	rm -rf $(BUILD_DIR)
	rm -f $(LOG_FILES)
	rm -f input_data.zip
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@echo "$(GREEN)Cache and build artifacts cleaned$(NC)"

.PHONY: clean-test
clean-test: ## Clean test artifacts and cache
	@echo "$(GREEN)Cleaning test artifacts...$(NC)"
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -f coverage.xml
	rm -f test-results.xml
	find . -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@echo "$(GREEN)Test artifacts cleaned$(NC)"

.PHONY: clean-notebooks
clean-notebooks: ## Clean notebook output and checkpoints (no-op for this project)
	@echo "$(GREEN)No notebooks to clean in this project$(NC)"

.PHONY: clean-dist
clean-dist: ## Clean distribution files
	@echo "$(GREEN)Cleaning distribution files...$(NC)"
	rm -rf $(DIST_DIR)
	@echo "$(GREEN)Distribution files cleaned$(NC)"

.PHONY: clean-all
clean-all: clean clean-test clean-notebooks clean-dist ## Clean everything (build, test, notebooks, dist)
	@echo "$(GREEN)Full cleanup completed$(NC)"

# =============================================================================
# BACKUP AND DISTRIBUTION
# =============================================================================

.PHONY: backup
backup: ## Create a backup of the src directory
	@echo "$(GREEN)Creating backup of src directory...$(NC)"
	mkdir -p $(BACKUPS_DIR)
	cp -r src/ $(BACKUPS_DIR)backup-src-$(shell date +%Y%m%d-%H%M%S)/
	@echo "$(GREEN)Backup created in $(BACKUPS_DIR)backup-src-$(shell date +%Y%m%d-%H%M%S)$(NC)"

.PHONY: zip-data
zip-data: ## Create zip archive of input data in root directory
	@echo "$(GREEN)Creating input data zip archive...$(NC)"
	@if [ ! -d input_data ]; then \
		echo "$(RED)❌ input_data directory not found$(NC)"; \
		exit 1; \
	fi
	cd input_data && zip -r ../input_data.zip .
	@echo "$(GREEN)✅ Created input_data.zip$(NC)"
	@ls -lh input_data.zip

.PHONY: dist
dist: ## Create complete distribution package with all files
	@echo "$(GREEN)Creating complete distribution package...$(NC)"
	@echo "$(YELLOW)Including: source code, tests, config, documentation$(NC)"
	@mkdir -p $(DIST_DIR)
	@zip -r $(DIST_DIR)$(PROJECT_NAME)-$(shell date +%Y%m%d-%H%M%S).zip \
		src/ tests/ pyproject.toml README.md Makefile \
		knowledge/ publications/ \
		--exclude="*.pyc" "__pycache__/*" ".pytest_cache/*" \
		"$(BACKUPS_DIR)*" ".venv/*" "*.zip" "$(DIST_DIR)*" \
		"*.log" "log.txt" \
		2>/dev/null || true
	@echo "$(GREEN)✅ Distribution package created$(NC)"
	@ls -lh $(DIST_DIR)$(PROJECT_NAME)-*.zip 2>/dev/null || true

# =============================================================================
# QUALITY ASSURANCE
# =============================================================================

.PHONY: validate
validate: ## Validate project structure and requirements
	@echo "$(GREEN)Validating project structure...$(NC)"
	@echo "📁 Checking required files..."
	@test -f pyproject.toml && echo "✅ pyproject.toml found" || echo "❌ pyproject.toml missing"
	@test -d src/crewai_poetry_crew/ && echo "✅ src/crewai_poetry_crew/ found" || echo "❌ src/crewai_poetry_crew/ missing"
	@test -d tests/ && echo "✅ tests/ directory found" || echo "❌ tests/ directory missing"
	@test -f README.md && echo "✅ README.md found" || echo "❌ README.md missing"
	@test -d knowledge/ && echo "✅ knowledge/ directory found" || echo "❌ knowledge/ directory missing"
	@test -d publications/ && echo "✅ publications/ directory found" || echo "❌ publications/ directory missing"
	@echo "$(GREEN)Validation completed$(NC)"

.PHONY: check
check: validate test-config ## Run basic checks (validation + config tests)
	@echo "$(GREEN)Basic checks completed successfully$(NC)"

# =============================================================================
# DEVELOPMENT WORKFLOW
# =============================================================================

.PHONY: dev-setup
dev-setup: install-dev validate ## Complete development setup (use 'make start' for fresh setup)
	@echo "$(GREEN)Development environment ready!$(NC)"
	@echo "$(YELLOW)Next steps:$(NC)"
	@echo "  1. Run tests: make test"
	@echo "  2. Run crew: make run"
	@echo "  3. Create backup: make backup"

.PHONY: ci
ci: clean install-dev test validate ## Continuous integration pipeline
	@echo "$(GREEN)CI pipeline completed successfully$(NC)"

.PHONY: pre-commit
pre-commit: clean-test test validate ## Pre-commit validation
	@echo "$(GREEN)Pre-commit checks passed$(NC)"

# =============================================================================
# STATUS AND MONITORING
# =============================================================================

.PHONY: status
status: ## Show project status
	@echo "$(GREEN)CrewAI Poetry Crew - Project Status$(NC)"
	@echo "======================================"
	@echo "📁 Project Directory: $(PWD)"
	@echo "🐍 Python: $(shell $(PYTHON) --version 2>/dev/null || echo 'Not found')"
	@echo "📦 Virtual Environment: $(if $(wildcard $(VENV_DIR)),✅ Active,❌ Not created)"
	@echo "🧪 Tests: $(shell find tests/ -name '*.py' 2>/dev/null | wc -l | tr -d ' ') test files"
	@echo "📝 Source Files: $(shell find src/ -name '*.py' 2>/dev/null | wc -l | tr -d ' ') Python files"
	@echo "📚 Knowledge Files: $(shell find knowledge/ -name '*' 2>/dev/null | wc -l | tr -d ' ') files in knowledge/"
	@echo "📄 Publications: $(shell find publications/ -name '*.md' 2>/dev/null | wc -l | tr -d ' ') published poems"
	@echo "💾 Backup Files: $(shell find $(BACKUPS_DIR) -name '*' 2>/dev/null | wc -l | tr -d ' ') files in $(BACKUPS_DIR)"
	@echo ""
	@echo "$(YELLOW)Recent Activity:$(NC)"
	@echo "  Last log update: $(shell ls -t log.txt 2>/dev/null | head -1 || echo 'No log.txt')"
	@echo "  Last publication: $(shell ls -t publications/*.md 2>/dev/null | head -1 || echo 'No publications')"

.PHONY: info
info: ## Show detailed project information
	@echo "$(GREEN)Detailed Project Information$(NC)"
	@echo "============================"
	@echo ""
	@make status
	@echo ""
	@echo "$(YELLOW)Available Make Targets:$(NC)"
	@make help

# =============================================================================
# SPECIAL TARGETS
# =============================================================================

.DEFAULT_GOAL := help

# Ensure intermediate files aren't deleted
.PRECIOUS: $(VENV_DIR) pyproject.toml

# Mark all phony targets
.PHONY: all clean install test help