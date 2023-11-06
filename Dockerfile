# Version of Python
FROM python:3.9
ADD main.py .

# Setup Working Directory
WORKDIR /recyco

# Copy requirement.txt into working directory 
COPY ./requirements.txt ./

# Install all the dependency
RUN pip install --no-cache-dir -r requirements.txt

# Copy code into working directory
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]