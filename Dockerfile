FROM python:3.10-slim

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m -u 1000 mcp

# Copy project files
COPY pyproject.toml README.md ./
COPY ./src ./src

# Install dependencies and project
RUN pip install --no-cache-dir -e .

# Switch to non-root user
USER mcp

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV AWS_REGION=ap-south-1

# Create directory for .env file
# RUN mkdir -p /app/config

# Expose any necessary ports (if needed in the future)
# EXPOSE 8080

# Set the entrypoint to run the MCP server
ENTRYPOINT ["python", "-m", "mcp_server_aws.server"]