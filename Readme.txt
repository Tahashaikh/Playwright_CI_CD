Create Docker agent in Jenkins

Open Docker container and execute command.

docker run -p 3375:2375 -v /var/run/docker.sock:/var/run/docker.sock -d shipyard/docker-proxy