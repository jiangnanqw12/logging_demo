import logging

class EstrellioLogger:
    def __init__(self, log_to_file=True, show_plots=True, img_to_file=False, uniform_logging_level=True, desired_level=logging.DEBUG, logger_level=logging.DEBUG, ch_level=logging.INFO, fh_level=logging.DEBUG, log_file_name="logfile.log"):
        """
        Initialize the logger with specified settings.

        Parameters:
        - log_to_file (bool): Enables logging to a file.
        - show_plots (bool): This flag is reserved for future plotting functionalities.
        - img_to_file (bool): This flag is reserved for future functionalities where images might be saved.
        - uniform_logging_level (bool): When True, applies a uniform logging level across all handlers.
        - desired_level (logging level): The logging level applied if uniform_logging_level is True.
        """
        self._log_to_file = log_to_file
        self._show_plots = show_plots
        self._img_to_file = img_to_file
        self._uniform_logging_level = uniform_logging_level
        self._desired_level = desired_level
        
        self._logger_level = logger_level
        self._ch_level = ch_level
        self._fh_level = fh_level
        self._log_file_name = log_file_name
        self.logger = self.setup_logger()

    def get_log_to_file(self):
        return self._log_to_file

    def set_log_to_file(self, value):
        self._log_to_file = value

    def get_show_plots(self):
        return self._show_plots

    def set_show_plots(self, value):
        self._show_plots = value

    def get_img_to_file(self):
        return self._img_to_file

    def set_img_to_file(self, value):
        self._img_to_file = value

    def get_uniform_logging_level(self):
        return self._uniform_logging_level

    def set_uniform_logging_level(self, value):
        self._uniform_logging_level = value

    def get_desired_level(self):
        return self._desired_level

    def set_desired_level(self, value):
        self._desired_level = value

    def get_logger_level(self):
        return self._logger_level

    def set_logger_level(self, value):
        self._logger_level = value

    def get_ch_level(self):
        return self._ch_level

    def set_ch_level(self, value):
        self._ch_level = value

    def get_fh_level(self):
        return self._fh_level

    def set_fh_level(self, value):
        self._fh_level = value

    def get_log_file_name(self):
        return self._log_file_name

    def set_log_file_name(self, value):
        self._log_file_name = value

    def setup_logger(self):
        logger = logging.getLogger('estrellio_logger')
        logger.setLevel(self._desired_level if self._uniform_logging_level else self._logger_level)

        ch = logging.StreamHandler()
        ch.setLevel(self._desired_level if self._uniform_logging_level else self._ch_level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        if self._log_to_file:
            fh = logging.FileHandler(self._log_file_name)
            fh.setLevel(self._desired_level if self._uniform_logging_level else self._fh_level)
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
        getattr(self.logger, level.lower(), self.logger.error)(message)
        'todo, what is getattr'
def main():
    # Example usage in another file
    from estrellio_logging_lib import EstrellioLogger
    logger = EstrellioLogger(log_to_file=True, show_plots=True, img_to_file=False, uniform_logging_level=True, desired_level=logging.DEBUG,logger_level=logging.DEBUG,ch_level=logging.INFO,fh_level=logging.DEBUG,log_file_name="logfile.log")
    logger = EstrellioLogger()
    global show_plots
    global img_to_file
    show_plots=logger.get_show_plots
    img_to_file=logger.get_img_to_file
    logger.set_log_to_file(True)
    logger.set_show_plots(True)
    logger.log_message('info', 'This is an info message.')
    import matplotlib.pyplot as plt
    if show_plots or img_to_file:
        data=[1, 2, 3, 4]
        plot_title='Sample Plot'
        plt.figure()
        plt.plot(data)
        plt.title(plot_title)
    if show_plots:
        plt.show()
    if img_to_file:
        plt.savefig('plot.png')
if __name__ == '__main__':
    main()