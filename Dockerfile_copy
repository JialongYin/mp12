FROM python:3.8
COPY . /mp12
RUN \
  apt-get update -y && \
  pip3 install -r /mp12/requirements.txt --no-cache-dir && \
  pip3 install --no-cache-dir torch==1.4.0 torchvision==0.5.0
CMD /bin/bash
