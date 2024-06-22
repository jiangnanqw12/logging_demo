# File: logging_lib.py
import logging


class MyLogger:
    def __init__(self, log_to_file=True, show_plots=True, img_to_file=False, uniform_logging_level=True, desired_level=logging.DEBUG):
        self.log_to_file = log_to_file
        self.show_plots = show_plots
        self.img_to_file = img_to_file
        self.uniform_logging_level = uniform_logging_level
        self.desired_level = desired_level
        self.logger = self.setup_logger()

    def setup_logger(self):
        logger = logging.getLogger('my_custom_logger')
        logger.setLevel(logging.DEBUG if self.uniform_logging_level else logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(self.desired_level if self.uniform_logging_level else logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        if self.log_to_file:
            fh = logging.FileHandler('logfile.log')
            fh.setLevel(self.desired_level if self.uniform_logging_level else logging.DEBUG)
            fh.setFormatter(formatter)
            logger.addHandler(fh)

        return logger

    def log_message(self, level, message):
        if level.lower() == 'info':
            self.logger.info(message)
        elif level.lower() == 'debug':
            self.logger.debug(message)
        elif level.lower() == 'warning':
            self.logger.warning(message)
        elif level.lower() == 'error':
            self.logger.error(message)


def main():
    # Example usage in another file
    from logging_lib import MyLogger
    import matplotlib.pyplot as plt
    logger = MyLogger()
    logger.log_message('info', 'This is an info message.')
    
    data=[1, 2, 3, 4]
    plot_title='Sample Plot'
    plt.figure()
    plt.plot(data)
    plt.title(plot_title)
    if logger.show_plots:
        plt.show()
    if logger.img_to_file:
        plt.savefig('plot.png')
if __name__=='__main__':
    main()