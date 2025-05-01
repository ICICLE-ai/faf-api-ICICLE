FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the Django app runs on
EXPOSE 8000

# Define environment variables for the MySQL connection
#ENV DB_HOST=172.19.0.1
ENV DB_PORT=3306
ENV DB_NAME=faf
ENV DB_USER=fafuser
ENV DB_PASSWORD=FQ^2t73Ava

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
