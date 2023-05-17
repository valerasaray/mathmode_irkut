FROM python:3.10.6

WORKDIR /a
COPY requirements.txt requirements.txt
RUN apt-get install --reinstall libpq-dev
RUN pip3 install -U pip
RUN pip3 install -U -r requirements.txt --use-pep517
COPY . /a
# RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.edgedb.com | sh
# RUN chmod +x ./edgedb.sh

ENV ALEMBIC_CONFIG="/a/app/alembic.ini"

RUN mkdir -p /usr/local/share/keyrings && \
 curl --proto '=https' --tlsv1.2 -sSf \
  -o /usr/local/share/keyrings/edgedb-keyring.gpg \
  https://packages.edgedb.com/keys/edgedb-keyring.gpg

RUN echo deb [signed-by=/usr/local/share/keyrings/edgedb-keyring.gpg]\
  https://packages.edgedb.com/apt \
  $(grep "VERSION_CODENAME=" /etc/os-release | cut -d= -f2) main \
  | tee /etc/apt/sources.list.d/edgedb.list

RUN apt-get update -y && apt-get install edgedb-2 -y

EXPOSE 8000
