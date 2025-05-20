# Optional(Creating logger and then use logging)

import os
import sys
import logging

log_format = '%(asctime)s : %(levelname)s : %(module)s : %(message)s'  # Adjusted format name

log_dir = "logs"
log_path = os.path.join(log_dir, "shows_log.log")

os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(level=logging.INFO,
                    format=log_format,
                    handlers=[
                        logging.FileHandler(log_path),
                        logging.StreamHandler(sys.stdout)
                    ]
                    )

logger = logging.getLogger('mlLogger')