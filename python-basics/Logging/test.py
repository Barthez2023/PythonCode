from Logger import logging

def add(a,b):
    logging.debug("The addition operation is taking palce")
    return a+b

logging.debug("The addition function is  called")
add(10,20)