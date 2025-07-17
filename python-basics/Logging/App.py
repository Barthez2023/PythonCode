import logging

## logging setting
## configuring the logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app.log1"),
        logging.StreamHandler()
    ],
    force=True,
)

logger=logging.getLogger("ArithmeticApp")
logger.setLevel(logging.DEBUG)

def add(a,b):
    result=a+b
    logger.debug(f"Adding {a}+{b} is ={result}")
    return result

def subtract(a,b):
    result=a-b
    logger.debug(f"Subtracting {a}-{b} is ={result}")  
    return result  


def multiply(a,b):
    result=a*b
    logger.debug(f"Multiplyting {a}*{b} is ={result}")  
    return result  

def divide(a,b):
    try:
        result=a/b
        logger.debug(f"Dividing {a}/{b} is ={result}")  
        return result  
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None


add(10,15)
subtract(15,10)
multiply(10,15)
divide(20,0)