## About
The Docker container is used for the development and test and for production. The development and test is done on a Docker for Windows, while the production Docker is ran on a Centos 7.


## How to start
### Build container
Step into this folder and run `docker build . --tag=text-similarity-image`

### Create image
Since Windows is the development environment the Flask server is not ran in the background, hence no `entrypoint` flag.

#### On Windows (development)
`docker run -itd --rm -p5000:5000 --name text-similarity --hostname text-similarity -v C:\marko\GitHub\text-similarity-web:/local-git text-similarity-image`

#### On Centos (production)
`docker run --entrypoint "/bin/bash" -itd --rm -p5000:5000 --name text-similarity --hostname text-similarity -v /home/centos/text-similarity-web:/local-git text-similarity-image /run_start.sh`

### Run container
`docker exec -it text-similarity bash`
If running the container for development, the Flask service should be started manually by executing `flask run --host=0.0.0.0` once in the container.

### Stop container
In case of recreating the image
`docker stop text-similarity`
