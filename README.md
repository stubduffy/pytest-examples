# rasa challenge - CLI and API tests

Repo showcasing the testing of Taskwarrior and fakestoreapi.

## Setup environment
The tests require a prior installation of the Taskwarrior application.

Set the env variable `TASKW_PATH` to the path location where the task executable lives on your machine.
E.g. `export TASKW_PATH=/opt/homebrew/bin`

Install the python dependencies:
`pip3 install -r requirements.txt`

## Run the tests
Run the Taskwarrior tests:
`pytest ./teststest_taskwarrior -s -v`


## Future Improvements
 - Test more of the Taskwarrior functionality, we're only scratching the surface of what it does here.
 - Figure out how to test features requiring confirmation (e.g. delete), i.e. not setting `confirmation=no`.