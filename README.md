# Logging Library

This Python library provides a customizable logging setup that can be integrated into Python applications to manage both console and file logging with configurable verbosity levels.

## Features

- **Flexible Logging**: Supports both console and file logging with independent or uniform verbosity levels.
- **Configurable Logging Levels**: Set individual logging levels for the console and file handlers, or apply a uniform level across both.
- **Conditional File Logging**: Option to enable or disable file logging based on runtime configuration.
- **Future-Proof Flags**: Reserved flags for potential future features related to plotting and saving output.

## Configuration Parameters

- `log_to_file` (bool): Enable logging to a file. Defaults to `True`.
- `show_plots` (bool): Reserved for future plotting functionalities. Defaults to `True`.
- `img_to_file` (bool): Reserved for future functionalities where images might be saved. Defaults to `False`.
- `uniform_logging_level` (bool): When set to `True`, applies a uniform logging level across all handlers. Defaults to `True`.
- `desired_level` (logging level): Specifies the logging level to apply when `uniform_logging_level` is `True`. Defaults to `logging.DEBUG`.
- `logger_level` (logging level): Default logging level for the logger. Defaults to `logging.DEBUG`.
- `ch_level` (logging level): Logging level for the console handler. Defaults to `logging.INFO`.
- `fh_level` (logging level): Logging level for the file handler. Defaults to `logging.DEBUG`.
- `log_file_name` (str): Name of the log file. Defaults to `"logfile.log"`.

## Usage

Import and instantiate `MyLogger` to integrate logging into your Python application. Adjust the initialization parameters as needed to configure the logging behavior.