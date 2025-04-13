# Use Python as the base image
FROM python:3.12.10-bookworm

# Set environment variables to avoid user prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists and install PostgreSQL and pgAgent
RUN apt update
RUN apt install curl ca-certificates
RUN curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
RUN echo "deb http://apt.postgresql.org/pub/repos/apt bookworm-pgdg main" | tee /etc/apt/sources.list.d/pgdg.list
RUN apt-get update
RUN apt-get update && \
    apt-get install -y vim postgresql-client-17 postgresql-contrib-17 pgagent && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the default command to run when starting the container
CMD ["bash", "-c", "while true; do sleep 1; done"]
