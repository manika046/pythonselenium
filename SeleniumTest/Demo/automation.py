import os

from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('../.venv/.env')
load_dotenv(dotenv_path=dotenv_path)

print(os.getenv("MY_KEY"))
