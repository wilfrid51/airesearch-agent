import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the value of the key
secret_key = os.getenv('SERPAPI_API_KEY')

# Print the key
print(f'SERPAPI_API_KEY: {secret_key}')