FROM python:3-bullseye

WORKDIR /root

ENV DEBIAN_FRONTEND noninteractive

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

# フォルダを作る
RUN mkdir -p /code

WORKDIR /code
ADD requirements.txt /code/

RUN pip install --upgrade pip &&\
    pip install -r requirements.txt &&\
    # faseapiのインストール
    pip install "fastapi[all]"

ADD . /code/

CMD /bin/bash