# Use the official Python image as the base
FROM python:3.6

# Maintainer information
LABEL maintainer="João Francisco <joaofrancisco.monteiro11@gmail.com>"

# Create the "www" user and create directories "/app" and "/log"
RUN useradd www && \
    mkdir /app && \
    mkdir /log && \
    chown www /log

# Set the default user to "www"
USER www

# Define a volume for the directory "/log" (optional, allows sharing data with the host)
VOLUME /log

# Copy all files to the "/app" directory: Copy all files from the hosts current directory to the /app directory inside the container
COPY * /app                      

# Set the working directory to "/app"
WORKDIR /app

# Expose port 8000, where the Python server will be listening (not mandatory, but useful for documentation)
EXPOSE 8000

# Define the entrypoint command for the Python interpreter
ENTRYPOINT ["/usr/local/bin/python"]

# Define the default arguments for the entrypoint command (can be overridden when running the container)
CMD ["run.py"]
