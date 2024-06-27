
import logging

class EstrellioLogger:
    def __init__(self, log_to_file=True, show_plots=True, img_to_file=False, uniform_logging_level=True, desired_level=logging.DEBUG,logger_level=logging.DEBUG,ch_level=logging.INFO,fh_level=logging.DEBUG,log_file_name="logfile.log"):
        """
        Initialize the logger with specified settings.

        Parameters:
        - log_to_file (bool): Enables logging to a file.
        - show_plots (bool): This flag is reserved for future plotting functionalities.
        - img_to_file (bool): This flag is reserved for future functionalities where images might be saved.
        - uniform_logging_level (bool): When True, applies a uniform logging level across all handlers.
        - desired_level (logging level): The logging level applied if uniform_logging_level is True.
        """
        self.log_to_file = log_to_file
        self.show_plots = show_plots
        self.img_to_file = img_to_file
        self.uniform_logging_level = uniform_logging_level
        self.desired_level = desired_level
        
        self.logger_level=logger_level
        self.ch_level=ch_level
        self.fh_level=fh_level
        self.log_file_name=log_file_name
        self.logger = self.setup_logger()

    def setup_logger(self):
        """Setup and return a configured logger."""
        logger = logging.getLogger('estrellio_logger')
        logger.setLevel(self.desired_level if self.uniform_logging_level else self.logger_level)

        ch = logging.StreamHandler()
        ch.setLevel(self.desired_level if self.uniform_logging_level else self.ch_level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        if self.log_to_file:
            fh = logging.FileHandler(self.log_file_name)
            fh.setLevel(self.desired_level if self.uniform_logging_level else self.fh_level)
            fh.setFormatter(formatter)
            logger.addHandler(fh)

        return logger
    # def log_message(self, level, message):
    #     if level.lower() == 'debug':
    #         self.logger.debug(message)
    #     elif level.lower() == 'info':
    #         self.logger.info(message)
    #     elif level.lower() == 'warning':
    #         self.logger.warning(message)
    #     elif level.lower() == 'error':
    #         self.logger.error(message)
    def log_message(self, level, message):
        """Log a message at the given level."""
        getattr(self.logger, level.lower(), self.logger.error)(message)
        'todo, what is getattr'
def main():
    # Example usage in another file
    from estrellio_logging_lib import EstrellioLogger
    import matplotlib.pyplot as plt
    logger = EstrellioLogger(log_to_file=True, show_plots=True, img_to_file=False, uniform_logging_level=True, desired_level=logging.DEBUG,logger_level=logging.DEBUG,ch_level=logging.INFO,fh_level=logging.DEBUG,log_file_name="logfile.log")
    logger = EstrellioLogger()
    logger.log_message('info', 'This is an info message.')
    if logger.show_plots or logger.img_to_file:
        data=[1, 2, 3, 4]
        plot_title='Sample Plot'
        plt.figure()
        plt.plot(data)
        plt.title(plot_title)
    if logger.show_plots:
        plt.show()
    if logger.img_to_file:
        plt.savefig('plot.png')
if __name__ == '__main__':
    main()