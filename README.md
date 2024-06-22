## Introduction

- `log_to_file`: Set this to `True` to enable logging to a file. If set to `False`, logs will only be displayed on the console.
- `show_plots`: Determines whether to display plots using Matplotlib. If `True`, plots are shown on screen using `plt.show()`. If `False`, plots are not displayed.
- `img_to_file`: Set this to `True` to save plots to a file instead of displaying them. When enabled, plots are saved as 'plot.png' in the current directory.
- `uniform_logging_level`: Enables a uniform logging level across all handlers. Set this to `True` to apply a single logging level specified by `desired_level` to both the console and file handlers.
- `desired_level`: Specifies the logging level to be applied when `uniform_logging_level` is `True`. Acceptable values are `logging.DEBUG`, `logging.INFO`, `logging.WARNING`, `logging.ERROR`, and `logging.CRITICAL`. This setting ensures consistent log verbosity across different output channels.

