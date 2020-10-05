# Molecule parser

This is a technical test I had make at home.

## Requirement

Project use [Pipenv](https://docs.pipenv.org/) to manage your virtualenv, packages and python version

## Install

* With dev dependencies
```bash
$ pipenv install --dev
```

* Without dev dependencies
```bash
$ pipenv install
```

### Configuration

Copy `.env.sample` to `.env`, and custom it.

In development, the pylint is not able to import sub package so I had to add the export `PYTHONPATH` with the `src` extra entry.

In production, `.env` is forbidden and we should use a Dockerfile, to set this properly inside.

## Test
```bash
# run test once
make test

# watch tests
make test_watch
```
