.PHONY: clean format-python-code tests cov apidoc docs release-tag

VERSION = $(shell python -c "print(__import__('howl').__version__)")

clean:
	rm -fr docs/_build docs/api build/ dist/

format-python-code:
	isort .
	black -q .

tests:
	py.test

cov: tests
	coverage html
	@echo open htmlcov/index.html

apidoc:
	make -C docs clean apidoc

docs:
	make -C docs clean linkcheck html
	@echo open docs/_build/html/index.html

release-tag:
	@echo About to release ${VERSION}
	@echo [ENTER] to continue; read
	git tag -a "v${VERSION}" -m "Version v${VERSION}" && git push --follow-tags
