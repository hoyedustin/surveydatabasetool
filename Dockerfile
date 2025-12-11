# Step 1: Base image
FROM python:3.11-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Install system dependencies (for MySQL, build tools, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Step 4: Copy requirements.txt
COPY requirements.txt .

# Step 5: Upgrade pip and install Python dependencies
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Copy application code
COPY . .

# Step 7: Expose the port the app runs on
EXPOSE 8080

# Step 8: Command to run the app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
