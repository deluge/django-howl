.PHONY: clean tests cov docs release-tag

VERSION = $(shell python -c "print(__import__('howl').__version__)")

clean:
	rm -fr docs/_build build/ dist/
	make -C docs clean

auto-black-isort:
	black examples howl tests
	isort examples howl tests --recursive

tests: clean
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
