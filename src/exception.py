import sys
import logging

from logger import *

def error_message_detail(error, error_details: sys):
    _, _, tb = error_details.exc_info()
    file_name = tb.tb_frame.f_code.co_filename
    line_number = tb.tb_lineno
    error_message = f"In {file_name} at line {line_number}:\n {str(error)}"
    
    return error_message
    
class CustomException(Exception):
    def __init__(self, message, error_details: sys):
        super().__init__(message)
        self.error_message = error_message_detail(message, error_details)
        
    def __str__(self):
        return self.error_message
    
if __name__ == "__main__":
    try:
        b = 1/0
    except Exception as e:
        logging.info("Divide By Zero")
        raise CustomException(e, sys)
    