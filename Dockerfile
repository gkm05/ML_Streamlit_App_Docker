FROM python:3.10-alpine

RUN mkdir -p /home/app


# Copy the requirements file to the working directory
COPY requirements.txt .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/app

CMD ["python", "/home/app/app.py"]
