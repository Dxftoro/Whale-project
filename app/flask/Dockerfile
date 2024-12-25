FROM python:latest

WORKDIR /flask/

# Add main files
ADD app.py /flask/
ADD users.html /flask/
ADD flask.html /flask/
ADD dir.html /flask/
ADD requirements.txt /flask/

# Add 'static' directory that contains stylesheets and scripts for flask pages
RUN mkdir /flask/static
COPY static/ /flask/static/

# Run additional packages installation
RUN pip install -r requirements.txt
