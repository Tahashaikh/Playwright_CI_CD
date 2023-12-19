# Use the official Playwright Docker image as the base image
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

# Set the working directory in the container
WORKDIR /usr/src/app

# Clone the Git repository into the container
RUN git clone https://github.com/Tahashaikh/Playwright_CI_CD.git .

# Display the contents of the repository for debugging
RUN ls -al

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Display the installed packages for debugging
RUN pip list

# Define the command to run when the container starts
RUN pytest
