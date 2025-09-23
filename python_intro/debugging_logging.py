# better than `print` for debugging
# + Use a print() call, only if user should see the messages
# + logging levels; DEBUG, INFO, WARNING, ERROR, CRITICAL

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
# logging.disable(logging.CRITICAL) # suppress all log messages
logging.debug('Start of program')


def factorial(n):
    logging.debug('Start of factorial(' + str(n) + ')')
    total = 1
    # for i in range(n + 1): # found by `logging.debug`
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(' + str(n) + ')')
    return total

print(factorial(5))
logging.debug('End of program')


