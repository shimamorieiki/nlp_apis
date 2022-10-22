FROM python:3-buster

WORKDIR /root

ENV DEBIAN_FRONTEND noninteractive

# JUMAN KNP Version
ENV JUMANPP_VERSION 1.02
ENV JUMAN_VERSION 7.01
ENV KNP_VERSION 4.19

RUN apt-get update &&\
    apt-get install -y apt-utils dialog
RUN apt-get upgrade -y &&\
    apt-get install -y libboost-dev google-perftools libgoogle-perftools-dev gcc g++ make wget bzip2

# install JUMANPP
RUN wget http://lotus.kuee.kyoto-u.ac.jp/nl-resource/jumanpp/jumanpp-${JUMANPP_VERSION}.tar.xz -O /tmp/jumanpp.tar.xz &&\
    tar xJvf /tmp/jumanpp.tar.xz -C /tmp &&\
    cd /tmp/jumanpp-${JUMANPP_VERSION} &&\
    ./configure --prefix=/usr/local/ && make && make install &&\
    rm -rf /tmp/* &&\
    rm -rf /var/cache/apk/*

# install JUMAN
RUN wget http://nlp.ist.i.kyoto-u.ac.jp/nl-resource/juman/juman-${JUMAN_VERSION}.tar.bz2 -O /tmp/juman.tar.bz2 &&\ 
    tar xf /tmp/juman.tar.bz2 -C /tmp &&\
    cd /tmp/juman-${JUMAN_VERSION} &&\ 
    ./configure --prefix=/usr/local/ && make && make install &&\
    rm -rf /tmp/* &&\
    rm -rf /var/cache/apk/* &&\
    apt-get update && apt-get install -y --fix-missing libjuman4

# install KNP
RUN apt-get install -y --fix-missing zlib1g-dev &&\
    wget http://nlp.ist.i.kyoto-u.ac.jp/nl-resource/knp/knp-${KNP_VERSION}.tar.bz2 -O /tmp/knp.tar.bz2 &&\
    tar xf /tmp/knp.tar.bz2 -C /tmp &&\
    cd /tmp/knp-${KNP_VERSION} / &&\
    ./configure --prefix=/usr/local/ --with-juman-prefix=/usr/local/ && make && make install &&\
    rm -rf /tmp/* &&\
    rm -rf /var/cache/apk/*

# to use Japanese
RUN apt-get install -y -f locales
RUN locale-gen ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LC_CTYPE ja_JP.UTF-8
RUN localedef -f UTF-8 -i ja_JP ja_JP.utf8

# clean up all temporary files 
RUN apt-get clean &&\
    apt-get autoclean -y &&\
    apt-get autoremove -y &&\
    apt-get clean &&\
    rm -rf /tmp/* /var/tmp/* &&\
    rm -rf /var/lib/apt/lists/* &&\    
    rm -f /etc/ssh/ssh_host_*

# ユーザーを作成
ARG UID=1000
RUN useradd -m -u ${UID} docker

# フォルダを作る
RUN mkdir -p /code
RUN chown docker /code

# 作成したユーザーに切り替える
USER ${UID}

WORKDIR /code
ADD requirements.txt /code/

USER root

RUN pip install --upgrade pip &&\
    pip install -r requirements.txt &&\
    # faseapiのインストール
    pip install "fastapi[all]"

# 作成したユーザーに切り替える
USER ${UID}
ADD . /code/
USER root
RUN chown -hR docker:docker /code
USER ${UID}
CMD /bin/bash