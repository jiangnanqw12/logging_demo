### EstrellioLogger Usage Manual

#### Introduction

The `EstrellioLogger` class provides a customizable logging setup that allows you to log messages to both console and file with various levels of verbosity. This manual will guide you through using `EstrellioLogger` for logging different types of messages and managing log files.

#### Logging Levels and Their Usage

1. **Info**:
   - Used to log the start and end of the program, and entry and exit points.
   - Example: `logger.log_message('info', 'Program started')`

2. **Debug**:
   - Used to log variable values and other detailed information for debugging.
   - Example: `logger.log_message('debug', f'Variable value: {variable}')`

3. **Warning**:
   - Used to log warnings that indicate a potential problem.
   - Example: `logger.log_message('warning', 'This is a warning message')`

4. **Error**:
   - Used to log errors that indicate a failure in the program.
   - Example: `logger.log_message('error', 'An error occurred')`

#### Example Usage

Here is an example of how you can use `EstrellioLogger` in your program:

```python
import logging
from estrellio_logging_lib import EstrellioLogger

def main():
    logger = EstrellioLogger(log_to_file=True, show_plots=False, img_to_file=False, uniform_logging_level=True, desired_level=logging.DEBUG)

    logger.log_message('info', 'Program started')

    logger.log_message('info', 'Entering main function')
    
    variable = 42
    logger.log_message('debug', f'Variable value: {variable}')

    try:
        # Simulating a warning scenario
        if variable > 10:
            logger.log_message('warning', 'Variable is greater than 10, which may cause issues')
        
        # Simulating an error scenario
        result = 10 / 0
    except ZeroDivisionError as e:
        logger.log_message('error', f'An error occurred: {e}')
    
    logger.log_message('info', 'Exiting main function')
    logger.log_message('info', 'Program ended')

if __name__ == '__main__':
    main()
```

### Log File Location

By default, the log file is stored in the current working directory with the name specified during the initialization of the `EstrellioLogger` instance. If not specified, the default log file name is `logfile.log`.

To specify a different log file name:

```python
logger = EstrellioLogger(log_file_name="custom_logfile.log")
```

### Clearing All Logs Fun Using a Regular Expression


### Summary

- Use `EstrellioLogger` to log different types of messages using `info`, `debug`, `warning`, and `error` levels.
- Log important program events like start, entry, variable values, warnings, errors, exit, and end.
- Specify the log file name during initialization to direct logs to a custom file.
