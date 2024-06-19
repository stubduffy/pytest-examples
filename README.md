# pytest-examples

Repo showcasing the use of pytest in testing of Taskwarrior and fakestoreapi.

## Setup dependencies

Install a recent python version. Everything has been verified with 3.10, so that would be a decent choice.

Install all python dependencies:
`pip3 install -r requirements.txt`

### Taskwarrior
The Taskwarrior tests require a prior installation of the Taskwarrior application, and setting the env variable `TASKW_PATH` to the path location where the task executable lives on your machine.
E.g. `export TASKW_PATH=/opt/homebrew/bin`

### FakeStoreAPI
No additional setup needed here.

## Running the tests locally

### Taskwarrior
`pytest ./tests/taskwarrior/test_taskwarrior.py -s -v`

### FakeStoreAPI
`pytest ./tests/fakestoreapi/test_fakestoreapi.py -s -v`


## CI

Tests are running in Github Actions, on pull requests against `main`, or pushes to `main.`

### Taskwarrior
The `test_taskwarrior` workflow checks out the latest Taskwarrior code from their repo and builds it locally, unless found in the cache, in which case it will simply restore this and run with it. The cache key is looking at the file containing the release version so any update to the version should result in a cache miss and therefore a full rebuild. 

It then installs all python dependencies and runs the relevant tests.

### FakeStoreAPI
The `test_fakestoreapi` workflow simply installs all python dependencies and runs the relevant tests.

