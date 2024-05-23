# rasa challenge - CLI and API tests

Repo showcasing the testing of Taskwarrior and fakestoreapi.

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


## Future Improvements
 - TaskWarrior
   - Test more of the Taskwarrior functionality, we're only scratching the surface of what it does here.
   - Figure out how to test features requiring confirmation (e.g. delete), i.e. not setting `confirmation=no`.
 - FakeStoreApi
   - Refactor to make some duplicated code more reusable
   - Could look a bit closer into the details of what's returned and that it makes sense, e.g. check no products are repeated etc