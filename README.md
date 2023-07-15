# Docker-pythonServer
<p>This repository contains a simple Python application that serves as a web server to host a static HTML page. The primary advantage of this repository is that it comes with a pre-configured Dockerfile, allowing you to easily create a Docker container to run the application.</p>

## Usage
Follow the instructions below to build and run the Docker container for the Python web server:

1.**Clone the repository**:
```
git clone https://github.com/seu-usuario/Docker-pythonServer.git
cd Docker-pythonServer
```

2.**Build the Docker image**:
```
docker build -t build-py-server .
```
3.**Run the Docker container**:
```
docker run -p 8000:8000 build-py-server
````
In my case, I prefer to use port 80, so I used the following command:
```
docker container run -it -p 80:8000 --name python-server build-py-server
```

#### 4 Access the web server:

Open your web browser and go to 
``` 
http://localhost:8000
```
to view the static HTML page served by the Python web server.

## Python Code
The Python code inside the run.py file sets up a basic HTTP server using the built-in http.server module. It serves the static HTML page and customizes the logging of incoming requests. The server will run indefinitely and listen on port 8000 inside the Docker container.

## Dockerfile
The provided Dockerfile uses the official Python 3.6 image as the base and follows these steps:

- Creates a new user named "www" and sets up the directories /app and /log.
- Sets the default user inside the container to "www" for improved security.
- Defines a volume for the /log directory to optionally share data with the host system.
- Copies all files from the host's current directory to the /app directory inside the container.
- Sets the working directory to /app.
- Exposes port 8000 to enable communication with the Python web server.
- Specifies the entrypoint command as the Python interpreter.
- Defines the default arguments for the entrypoint command as run.py, which is the Python script to start the server.

## Customization
Feel free to customize the index.html file to display any content you desire on the served webpage. Additionally, you can modify the Python code inside run.py or add more features to the web server to suit your specific requirements.

**For any questions or suggestions, please open an issue in this repository. Happy coding!**
