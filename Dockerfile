# Python interpreter as a parent image 
FROM python:3.11.7 

# set the working dir inside the container 
WORKDIR /usr/src/app

# Copy the current dir contents into the container
COPY requirements.txt .
COPY ./datasets /usr/src/app/datasets
COPY ./datasets /usr/src/app/Scripts

# Install any needed packages specified in req.txt
RUN pip install --no-cache-dir -r requirements.txt

# port 5000 to outside 
ENV NAME Ultimate-DataEngineering-BigData.

# run the app
ENTRYPOINT [ "python" ]


