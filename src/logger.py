# ################Krish#################
# import logging
# import os
# from datetime import datetime


# LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# logs_path = os.path.join(os.getcwd() , "logs" , LOG_FILE)
# os.makedirs(logs_path , exist_ok=True)


# LOG_FILE_PATH = os.path.join(logs_path , LOG_FILE)

# logging.basicConfig(
#   filename=LOG_FILE_PATH,
#   format="[ %(asctime)s ]  %(lineno)d %(name)s - %(levelname)s - %(message)s ", 
#   level=logging.INFO, 
# )

# if __name__ == "__main__":
#   logging.info("Logging has started ")
  
################alternate#################
# logger.py
import logging
import os
from datetime import datetime

# Correct: logs/ directory only
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Generate file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Setup logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ]  %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging has started")
    print(f"Log file written to: {LOG_FILE_PATH}")




  

