# src/utils/rules.py

BYPASS_RULES = {
    "obfuscation": r"(?i)(LOVE\s*PL[1I]NY|PL[1I]NY|P1INY|L0VE|L\/0\/V\/E|Bypass)",
    "roleplay": r"(?i)(act as|you are now|ignore previous instructions|DAN mode|developer mode|system prompt|override mode)",
    "malware": r"(?i)(create a virus|write a keylogger|how to hack|inject shellcode|exploit|buffer overflow|payload)",
    "injection": r"(?i)(prompt injection|ignore all rules|system override|jailbreak|jail-break|ignore everything)",
    "encoding": r"(?i)(base64|hex|encoded|binary|payload|base 64|shellcode|ascii)",
    "recursive": r"(?i)(repeat this|print the prompt|output your instructions|start your response with|what were your instructions)",
    "privilege": r"(?i)(root access|sudo|admin mode|developer settings|unlock all features|super user|terminal mode)",
    "social_engineering": r"(?i)(help me get around|is it possible to|how can i trick|circumvent|bypass filters|rule violation)",
    "malicious_scripts": r"(?i)(powershell|bash|cmd|rm -rf|sql injection|directory traversal)"
}
