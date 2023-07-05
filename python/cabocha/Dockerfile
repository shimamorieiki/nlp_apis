FROM python:3.11-bullseye

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

WORKDIR /code
ADD requirements.txt /code/

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Mecab
RUN apt-get update && apt-get upgrade -y &&\
    apt-get install -y apt-utils mecab libmecab-dev mecab-ipadic-utf8 git curl xz-utils file sudo
# # neologd辞書
# RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git && \
#     cd mecab-ipadic-neologd && \
#     ./bin/install-mecab-ipadic-neologd -n -y && \
#     echo dicdir = `mecab-config --dicdir`"/mecab-ipadic-neologd">/etc/mecabrc && \
#     sudo cp /etc/mecabrc /usr/local/etc && \
#     cd ..

# CRF++ (Cabochaで必要)
# wget で取得できないのでローカルにファイルを置いて妥協
COPY CRF++-0.58.tar.gz /tmp
RUN tar xvf /tmp/CRF++-0.58.tar.gz && \
    cd CRF++-0.58 && \
    ./configure && \
    make && \
    make install

# Cabocha
RUN cd /tmp && DOWNLOAD_URL="`curl -c cookies.txt \
    'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7SDd1Q1dUQkZQaUU' \
    | sed -r 's/"/\n/g' |grep id=0B4y35FiV1wh7SDd1Q1dUQkZQaUU |grep confirm |sed 's/&amp;/\&/g'`" \
    && curl -L -b cookies.txt -o /tmp/cabocha-0.69.tar.bz2 "$DOWNLOAD_URL" \
    && tar jxf /tmp/cabocha-0.69.tar.bz2
RUN cd /tmp/cabocha-0.69 \
    && ./configure --with-mecab-config=`which mecab-config` --with-charset=utf8 \
    && ldconfig \
    && make \
    && make install \
    && ldconfig \
    && cd python \
    && python3 setup.py build \
    && python3 setup.py install

WORKDIR /code/python/cabocha
SHELL ["/bin/bash", "-c"]