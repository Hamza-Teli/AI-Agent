import os
from dotenv import load_dotenv

load_dotenv()

# To get the absolute path of current script
script_dr = os.path.abspath(os.getcwd())

# To get absolute path of the parent directory
parent_dir = os.path.join(script_dr, os.pardir)

dotenv_path = os.path.join(parent_dir, '.env')

# Load the .env file from parent directory
load_dotenv(dotenv_path)

