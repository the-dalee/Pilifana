FROM python:slim
ADD configuration /pilifana/configuration
ADD pilifana /pilifana/pilifana
ADD setup.py /pilifana
ADD README.md /pilifana
RUN apt-get update && \
    apt-get -y install pandoc && \
    cd /pilifana && \
    python3 setup.py install

CMD [ "pilifana" ]