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

### Preparing Docker
#### Setup the repository:
1. Install required packages: `sudo yum install -y yum-utils device-mapper-persistent-data lvm2`
2. Set up the stable repository: `sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo`
3. Install Docker: `sudo yum install -y docker-ce docker-ce-cli containerd.io`
4. Start Docker: `sudo systemctl start docker`
5. Give current user access the docker engine: `sudo usermod -a -G docker $USER`

### Install Git
`sudo yum install -y git`
