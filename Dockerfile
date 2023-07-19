FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev

# Set the working directory in the container
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
COPY ./runserver.sh .
RUN chmod +x runserver.sh

# Expose the port that Django runs on (default is 8000)
EXPOSE 8000

# Run Django development server
CMD ["python", "manage.py", "runserver"]