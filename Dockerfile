FROM python:3.8.10-slim

RUN mkdir -p /home/py-app


# Copy the requirements file to the working directory
COPY requirements.txt .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/py-app

CMD ["python" , "/home/app/app.py"]
