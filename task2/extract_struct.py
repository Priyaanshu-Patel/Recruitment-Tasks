import re
import json

text = """
[1] Smith, J. and Doe, A. (2020). Deep Learning for NLP. Journal of AI Research, 45(2), 123–145.
[2] Brown, P. (2018). High-Frequency Trading Systems. Quantitative Finance, 12(4), 233–249.
[3] Johnson, L. and Lee, R. (2021). Advances in Reinforcement Learning. Machine Learning Journal, 18(1), 56–70.
"""

pattern = re.compile(
    r"\[(\d+)\]\s+(.*?)\s+\((\d{4})\)\.\s+(.*?)\.\s+(.*?),\s+(\d+)\((\d+)\),\s+([\d\s–\-]+)\."
)

structured_data = []
for match in pattern.finditer(text):
    ref_num, authors, year, title, journal, volume, issue, pages = match.groups()
    pages = pages.replace("–", "-").strip()  #
    structured_data.append({
        "reference_number": int(ref_num),
        "authors": authors,
        "year": int(year),
        "title": title,
        "journal": journal,
        "volume": int(volume),
        "issue": int(issue),
        "pages": pages
    })


print(json.dumps(structured_data, indent=4, ensure_ascii=False))
