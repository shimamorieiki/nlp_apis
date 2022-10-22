FROM python:3-bullseye

WORKDIR /root

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update &&\
    apt-get install -y apt-utils dialog

RUN apt-get upgrade -y&&\
    apt-get install -y libboost-dev google-perftools libgoogle-perftools-dev gcc g++ make wget bzip2


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