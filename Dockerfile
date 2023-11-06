# Version of Python
FROM python:3.9

# Setup Working Directory
WORKDIR /recyco

# Copy requirement.txt into working directory 
COPY ./requirements.txt /recyco/requirements.txt

# Install all the dependency
RUN pip install --no-cache-dir --upgrade -r /recyco/requirements.txt 

# Copy code into working directory
COPY ./app /recyco/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]