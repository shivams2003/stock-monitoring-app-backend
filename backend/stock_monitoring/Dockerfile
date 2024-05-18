# Use the official Python image from the Docker Hub
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /usr/src/app/

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "stock_monitoring.wsgi:application"]
