format:
	pipenv run black src tests

lint:
	pipenv run pylint src

test:
	pipenv run pytest -s

test_watch: test
	pipenv run watchmedo shell-command \
 		--patterns="*.py" \
 		--recursive \
 		--command='make test' \
 		.