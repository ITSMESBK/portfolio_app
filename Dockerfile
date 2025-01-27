# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR ./portfolio_app/webapp

# Copy the current directory contents into the container at /app 
ADD . /portfolio_app

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# run the command to start uWSGI
#CMD ["uwsgi", "./app.ini"]
CMD [ "python", "manage.py" ,"runserver", "0.0.0.0:8080" ]

