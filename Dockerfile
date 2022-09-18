FROM python:3
ADD . /
RUN pip install discord
CMD [ "python", "./bontabot.py" ]