# Use the official Playwright Docker image as the base image
FROM mcr.microsoft.com/playwright

# Set the working directory in the container
WORKDIR /usr/src/app

# Clone the Git repository into the container
RUN git clone https://github.com/Tahashaikh/Playwright_CI_CD.git .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run when the container starts
CMD ["pytest", "test_file.py"]
