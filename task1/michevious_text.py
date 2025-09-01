import re
from datetime import datetime

def transform_text(input_text: str) -> str:
    text = input_text

    text = re.sub(r'\b\d{5}[- ]?\d{5}\b', '[REDACTED]', text)

    def convert_date(match):
        date_str = match.group()
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            day = dt.day
            if 11 <= day <= 13:
                suffix = "th"
            else:
                suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
            return f"{day}{suffix} {dt.strftime('%B %Y')}"
        except ValueError:
            return date_str  

    text = re.sub(r'\b\d{4}-\d{2}-\d{2}\b', convert_date, text)

    text = re.sub(r'\bPython\b', '🐍', text)


    text = re.sub(r'\bJava\b', '☕️', text)

    return text



text_in=input("enter michenvous text")
print(transform_text(text_in))