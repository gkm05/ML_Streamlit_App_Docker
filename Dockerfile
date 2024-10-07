FROM python:3.8.10-slim

RUN mkdir /home/app

WORKDIR /home/app
# Copy the requirements file to the working directory
COPY requirements.txt .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/app

CMD ["python" , "/home/app/app.py"]
