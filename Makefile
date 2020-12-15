test:
	cd ./tests/spec & pipenv run test
	yarn --cwd ./tests/typescript run test
	cd ./tests/python & pipenv run test
docs:
	cd ./scripts/mk-docs & pipenv run build
lint-deps:
	cd ./tests/spec & pipenv install -d
lint:
	cd ./tests/spec & pipenv run test
