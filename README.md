# Text similarity project
The project calculates similarity between 2 or more sentences. A Web User Interface is used to upload the file with sentences. It is also possible to do a small test by manually entering two sentences.

## Technology stack
* Docker
* Powershell
* Anaconda
* Python
* Flask
* Jupyter
* Centos 7
* AWS EC2

Centos 7 is the chosen operating system for development, test and production.  
Docker is used to create a container in Windows 10 for local development and test. The plan is to add another Docker project which will run on Amazon's EC2 and serve as an environment for production.  
Powershell is used for creating Docker image and running the container.  
Anaconda is used to install and maintain Python environment and Jupyter notebooks.  
Python is the language of choice of the algorithm behind text similarity project.  
Flask is the framework of choice to build Python flavoured websites.  
AWS (Amazon Web Services) is the public cloud service provider of choice for running the project publicly.  

## Preparing production server
Operating system: Centos 7 on Amazon's EC2

### Install Git
`sudo yum install -y git`

### Clone repository
git clone https://github.com/markokole/text-similarity-web

### Step into directory
cd text-similarity-web

### install and setup Docker
. prepare_docker.sh

### Build Docker image
Login to the instance again, step into the directory `text-similarity-web/docker_production` and build the image: `docker build . --tag=text-similarity-image`

### Start container
`docker run -itd --rm -p5000:5000 --name text-similarity --hostname text-similarity -v /home/centos/text-similarity-web:/local-git text-similarity-image`

### Go into the container
`docker exec -it text-similarity bash`
