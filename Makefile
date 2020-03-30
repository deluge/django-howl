.PHONY: clean format-python-code tests cov apidoc docs release-tag

VERSION = $(shell python -c "print(__import__('howl').__version__)")

clean:
	rm -fr docs/_build build/ dist/
	make -C docs clean

format-python-code:
	isort -rc .
	black -q .

tests:
	py.test

cov: tests
	coverage html
	@echo open htmlcov/index.html

apidoc: clean
	make -C docs apidoc

docs: clean
	make -C docs linkcheck html
	@echo open docs/_build/html/index.html

release-tag:
	@echo About to release ${VERSION}
	@echo [ENTER] to continue; read
	git tag -a "v${VERSION}" -m "Version v${VERSION}" && git push --follow-tags
