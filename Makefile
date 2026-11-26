# Run `make help` to list targets. Everything uses Python 3 with no extra packages.

.PHONY: help check test next work questions index external overlap

help: ## Show available targets
	@grep -E '^[a-z-]+:.*## ' $(MAKEFILE_LIST) | sed -E 's/:.*## /\t/'

check: ## Validate links, IDs, front matter, indexes, quotation lengths and the secrets scan (run before every commit)
	python3 tools/docs.py check

test: ## Run the checker's unit tests
	python3 -m unittest discover -s tools -p 'test_*.py'

next: ## Show the next free problem and decision IDs
	python3 tools/docs.py next

work: ## List unclaimed problems in roadmap order
	python3 tools/docs.py work

questions: ## List every open question with its ID
	python3 tools/docs.py questions

index: ## Print a JSON map of problems and decisions (handy for agents)
	python3 tools/docs.py index

.PHONY: visuals
visuals: ## Make the visual summary for a pull request or issue: make visuals BRIEF=brief.md [ARGS="--offline"] (needs Chrome or Chromium)
	python3 tools/visuals.py "$(BRIEF)" $(ARGS)

external: ## Check external links (needs network; not run in CI)
	python3 tools/docs.py external

overlap: ## Find text shared word for word with a saved source page: make overlap SOURCE=page.html [FILES="docs/x.md"]
	python3 tools/docs.py overlap $(SOURCE) $(if $(FILES),--in $(FILES),)
