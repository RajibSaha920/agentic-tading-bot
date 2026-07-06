import os
import sys


class TradingBotException(Exception):
    """Custom exception for the Trading Bot."""

    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)

        _, _, exc_tb = error_details.exc_info()

        self.error_message = error_message

        if exc_tb:
            self.line_no = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename
        else:
            self.line_no = None
            self.file_name = None

    def __str__(self):
        return (
            f"Error occurred in script: [{self.file_name}] "
            f"at line number: [{self.line_no}] "
            f"error message: [{self.error_message}]"
        )
if __name__ == '__main__':
        try:
            a =1/0
            print("This will not be printed", a)
        except Exception as e:
            raise TradingBotException(e,sys)
