import os
import sys
import logging

# timestamp, levelname (kind of log), which module, log message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" 
log_dir = "logs" 
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
                    level=logging.INFO, 
                    format=logging_str,
                    
            handlers=[
                logging.FileHandler(log_filepath), # logs in a file
                logging.StreamHandler(sys.stdout) # prints on terminal
            ]
        )

logger = logging.getLogger("textSummarizationLogger")