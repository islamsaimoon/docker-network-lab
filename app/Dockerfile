FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements to leverage Docker cache during pip install
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py ./

# Expose the application's port
EXPOSE 5000

# Run the application when the container starts
CMD ["python", "app.py"]
