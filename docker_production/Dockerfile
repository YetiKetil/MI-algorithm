FROM centos:latest
MAINTAINER marko

USER root

RUN yum install -y epel-release \
    yum -y update

RUN yum install -y \
        python-pip \
        git \
        wget \
        unzip \
        bzip2

# Upgrade pip
RUN pip install --upgrade pip

RUN wget https://repo.continuum.io/archive/Anaconda3-2018.12-Linux-x86_64.sh -O /tmp/Anaconda.sh
RUN bash /tmp/Anaconda.sh -b -p /usr/lib/Anaconda
RUN export PATH="/usr/lib/Anaconda/bin:$PATH"

RUN mkdir /var/log/text-similiarity

VOLUME /local-git

ENV PATH="/usr/lib/Anaconda/bin:${PATH}"

RUN conda install -y -c anaconda flask flask-wtf
RUN conda install -y -c conda-forge flask-sqlalchemy flask-migrate

ENV FLASK_APP="/local-git/text_sim.py"

# copy files to container
COPY copy_files/run_start.sh ./
RUN chmod 700 *.sh

# start services at container start
ENTRYPOINT ["/bin/bash", "/run_start.sh"]
