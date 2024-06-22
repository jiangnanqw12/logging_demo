import logging
import matplotlib.pyplot as plt

# Control variables
log_to_file = True
show_plots = True
img_to_file = False
# Create a logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)  # Set the minimum log level

# Create a console handler and set its level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Optionally: Create a file handler if log_to_file is True
if log_to_file:
    fh = logging.FileHandler('logfile.log')
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

# Create a log format and add it to the console handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

# Test logging
logger.info('This is an info message.')

# Plotting with matplotlib
plt.figure()
plt.plot([1, 2, 3], [4, 5, 6])
plt.title('Test Plot')


if show_plots:
    plt.show()
if img_to_file:
    plt.savefig('plot.png')  

# Continue logging
logger.debug('Debugging information here.')
logger.error('An error occurred!')