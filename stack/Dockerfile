# Use Python as the base image
FROM python:3.12.10-bookworm

# Set environment variables to avoid user prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists and install PostgreSQL and pgAgent
RUN apt-get update && \
    apt-get install -y vim postgresql-client pgagent && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the default command to run when starting the container
CMD ["bash", "-c", "while true; do sleep 1; done"]
