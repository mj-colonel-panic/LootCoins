# lootcoins
## Selenium Project to claim monthly reward for Dragonrealms subscribers
This project will ultimately be run using the `python:alpine` docker image, in conjunction with `selenium/standalone-chrome` to create an automated, headless run.

## Configure this project to run automatically
#### Schedule a cron to execute monthly
To schedule this job to run on a recurring schedule, navigate to CI / CD -> Schedules.  I use a custom cron that runs on the 5th of the month at 7am UTC, but this would work with the standard monthly option also.

To provide the credentials for the job to run, configure the variables section to mount a `file` (not variable) named `list` which contains a new-line seperated set of `username:password` key/value pairs.  Once saved, the job will run on the set schedule.  See the image for example.

![CronExample](images/cron1.png)

