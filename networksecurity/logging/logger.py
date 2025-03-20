import logging  # Importing the logging module for logging events
import os  # Importing OS module for interacting with the file system
from datetime import datetime  # Importing datetime module to generate timestamped log filenames

# Generating a log file name with the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Defining the logs directory path inside the current working directory
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Creating the logs directory if it does not already exist
os.makedirs(logs_path, exist_ok=True)

# Full path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configuring logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Setting the log file path
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Log format
    level=logging.INFO,  # Setting the logging level to INFO
)
