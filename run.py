# Importing the necessary modules
import logging
import http.server
import socketserver
import getpass

# Defining a custom class that inherits from SimpleHTTPRequestHandler
class MyHTTPHandler(http.server.SimpleHTTPRequestHandler):
    # Overriding the log_message method to customize request logging
    def log_message(self, format, *args):
        # Logging the messages in a custom format using the logging module
        logging.info("%s - - [%s] %s\n"% (
            self.client_address[0],                   # Client IP address
            self.log_date_time_string(),               # Request date and time
            format % args                              # Formatted message with additional arguments
        ))

# Basic configuration for the logging module
logging.basicConfig(
    filename='/log/http-server.log',                  # File where logs will be stored
    format='%(asctime)s - %(levelname)s - %(message)s', # Log message format
    level=logging.INFO                                 # Logging level (only INFO level and above messages will be logged)
)

# Adding a StreamHandler to log messages to the console as well
logging.getLogger().addHandler(logging.StreamHandler())

# Logging a message to indicate that the server is initializing
logging.info('Initializing...')

# Setting up the port on which the server will listen for requests
PORT = 8000

# Creating an instance of the TCP server that will handle requests using the MyHTTPHandler class
httpd = socketserver.TCPServer(("", PORT), MyHTTPHandler)

# Logging a message to indicate the port on which the server is listening
logging.info('Listening on port: %s', PORT)

# Logging the current username for informational purposes
logging.info('User: %s', getpass.getuser())

# Starting the server, which will run indefinitely (serving requests) until interrupted
httpd.serve_forever()
