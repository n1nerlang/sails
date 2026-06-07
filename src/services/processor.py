# src/services/processor.py
import re
from loguru import logger
from utils.rules import BYPASS_RULES  # Import the rules!
from models import ProcessingRequest, AIResponse

def sorting_machine(text: str) -> tuple[bool, str]:
    for category, pattern in BYPASS_RULES.items():
        if re.search(pattern, text):
            # ... (your existing logging and refusal logic)
            return False, f"sorry, I can't do that. The message you have provided contains {category}."
    return True, ""

# ... (rest of your processor code)
