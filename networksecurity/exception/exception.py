import sys  # Importing system-specific parameters and functions
from networksecurity.logging import logger  # Importing logger for logging purposes

# Custom exception class for handling network security-related exceptions
class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        """
        Initializes the custom exception with error message and details.
        
        Parameters:
        error_message (str): The error message describing the exception.
        error_details (sys): System module used to extract traceback details.
        """
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()  # Extract exception traceback details
        
        # Extracting the line number where the exception occurred
        self.lineno = exc_tb.tb_lineno
        # Extracting the file name where the exception occurred
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        
    def __str__(self):
        """
        Returns a formatted error message with script name, line number, and error details.
        """
        return "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, self.error_message
        )

# Main block to execute the script
if __name__ == '__main__':
    try:
        logger.logging.info("Entered the try block ")  # Logging entry into the try block
        a = 1 / 0  # This will cause a ZeroDivisionError
        print("This will not be printed", a)  # This line will never execute due to the above error
    except Exception as e:
        # Raising the custom exception with the original exception details
        raise NetworkSecurityException(e, sys)
