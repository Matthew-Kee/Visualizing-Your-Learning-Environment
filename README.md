# Using Docker #
The `Dockerfile` does everything! 
## Building a docker image ##
`docker build -t [IMAGE NAME] .`
ex: `docker build -t interactive-docker .`
## Creating docker container ##
`docker run -it [IMAGE NAME] bash`
ex: `docker run -it interactive-docker bash`