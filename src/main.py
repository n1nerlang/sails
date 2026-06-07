from config import settings
from utils.logger import logger
from services.processor import run_app

def main():
    """
    Entry point for the application.
    Orchestrates configuration loading and execution.
    """
    logger.info(f"Initializing {settings.app_name}...")
    logger.debug(f"Mode: {'DEBUG' if settings.debug else 'PRODUCTION'}")

    try:
        # We start the processor, passing configuration if needed
        run_app(debug=settings.debug)
        logger.success("Process completed successfully.")
        
    except KeyboardInterrupt:
        logger.warning("Application stopped by user.")
        
    except Exception as e:
        # Catch-all for any uncaught runtime errors
        logger.exception(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
