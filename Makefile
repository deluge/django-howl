.PHONY: clean tests cov docs release

VERSION = $(shell pipenv run python -c "print(__import__('howl').__version__)")

clean:
	rm -fr docs/_build build/ dist/
	pipenv run make -C docs clean

tests:
	pipenv run py.test --cov

cov: tests
	pipenv run coverage html
	@echo open htmlcov/index.html

apidoc:
	pipenv run make -C docs apidoc

docs:
	pipenv run make -C docs linkcheck html
	@echo open docs/_build/html/index.html

release-tag: clean
	@echo About to release ${VERSION}
	git tag -a "v${VERSION}" -m "Version v${VERSION}" && git push --follow-tags
