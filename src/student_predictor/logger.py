import logging
import os
from datetime import datetime

# 1. Create a filename based on current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Define the path for the logs folder
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# 3. Create the directory if it doesn't exist
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

# 4. Configure the logging settings
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Test it (Optional)
if __name__ == "__main__":
    logging.info("Logging has started successfully.")