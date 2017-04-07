FROM python:3.5-slim
ADD configuration /pilifana/configuration
ADD pilifana /pilifana/pilifana
ADD setup.py /pilifana
ADD README.md /pilifana
RUN apt-get update && \
    apt-get -y install pandoc && \
    python3 --version && \
    pip3 install --upgrade /pilifana

CMD [ "pilifana" ]