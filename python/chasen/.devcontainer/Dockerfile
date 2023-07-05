FROM ghcr.io/shimamorieiki/devcontainer/python3_11:latest

WORKDIR /root

ENV DEBIAN_FRONTEND noninteractive

USER root
RUN apt-get update &&\
    apt-get install -y apt-utils dialog

RUN apt-get upgrade -y&&\
    apt-get install -y libboost-dev google-perftools libgoogle-perftools-dev gcc g++ make wget bzip2 chasen

# to use Japanese
RUN apt-get install -y -f locales

RUN locale-gen ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LC_CTYPE ja_JP.UTF-8
RUN localedef -f UTF-8 -i ja_JP ja_JP.utf8

# 作成したユーザーに切り替える
USER docker

WORKDIR /code
ADD requirements.txt /code/

USER root

RUN pip install --upgrade pip &&\
    pip install -r requirements.txt &&\
    # faseapiのインストール
    pip install "fastapi[all]"

# 作成したユーザーに切り替える
USER docker
ADD . /code/
USER root
RUN chown -hR docker:docker /code
USER docker

SHELL ["/bin/bash", "-c"]