# Use Python base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy requirement files and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY ./app ./app

# Run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
