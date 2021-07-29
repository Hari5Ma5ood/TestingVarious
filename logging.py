import logging
import os
logger = logging.getLogger()
logger.setLevel(logging.INFO)
carte_output_path = os.getenv('CARTE_BINARY_OUTPUT_DIR')
logging_output_dir = os.getenv('LOGGING_OUTPUT_DIR')
# Variables how the log file should be named and where to place it
if "LOGGING_OUTPUT_DIR" in os.environ:
    logPath = logging_output_dir
else:
    logPath = carte_output_path
fileName = 'PyEtlLogs'

# Setting the config of the log object
logging.basicConfig(
    format='%(process)d - %(asctime)s - %(message)s',
    filename= logPath + "/" +fileName
)

# Giving a log it started.
logging.info("Logging started!")