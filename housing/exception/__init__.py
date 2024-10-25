import os
import sys

class HousingException(Exception): #defining custom exception and Exception is the parent class #every class has an __init__ function.

    def __init__(self, error_message: Exception, error_detail:sys): #ie. error_message would be the object of the Exception class. 
        # sys module will tell which line or file has created the exception it will be captured over there. 
        
        super().__init__(error_message) #this errormsg would be passed to exception class #this is equivalent to : Exception(error_message)

        self.error_message = HousingException.get_detailed_error_message(error_message=error_message,
                                                                       error_detail=error_detail
                                                                        )


    @staticmethod #this is that method/function inside a class that can be called without creating the object of the class. 
    def get_detailed_error_message(error_message: Exception, error_detail:sys)-> str: #this function will return a string.

        """
        error_message: Exception object
        error_detail: object of sys module

        """

        _,_,exec_tb = error_detail.exc_info() #ie. execution information #first two  values not required hence used _, need third variable info hence used traceback information. 

        exception_block_line_number = exec_tb.tb_frame.f_lineno
        try_block_line_number = exec_tb.tb_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename

        error_message = f"""
        Error occured in script: 
        [ {file_name} ] at 
        try block line number: [{try_block_line_number}] and exception block line number: [{exception_block_line_number}] 
        error message: [{error_message}]
        """

        return error_message
    

    def __str__(self): #dunder method #when an object of the class is made. then when you print that object you will see the output of this fucntion. 
        return self.error_message  # error_message is the attribute of the class.
    

    def __repr__(self) -> str:
        return HousingException.__name__.str() #same as __str__ just prints.
    

    






