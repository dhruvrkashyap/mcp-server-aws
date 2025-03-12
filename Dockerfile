FROM python:3.10-slim

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


# Copy project files
COPY pyproject.toml requirements.txt README.md ./
COPY ./src ./src

# Install dependencies and project
RUN pip install -r requirements.txt
RUN pip install -e .

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV AWS_REGION=ap-south-1

# Create directory for .env file
# RUN mkdir -p /app/config

# Expose any necessary ports (if needed in the future)
# EXPOSE 8080

# Set the entrypoint to run the MCP server
CMD ["uv", "run", "mcp-server-aws"]