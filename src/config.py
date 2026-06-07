from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Sails AI"
    debug: bool = True
    model_path: str = "./data/weights"  # Default local path
    
    # By removing 'model_config', it won't force you to have a .env file.
    # It will use these defaults, or look for environment variables 
    # if you happen to pass them in your terminal.

settings = Settings()
