import re
import requests
from typing import List, Dict


def fetch_public_apis() -> List[Dict]:
    """Scrape the public-apis README for API entries."""
    url = "https://raw.githubusercontent.com/public-apis/public-apis/master/README.md"
    response = requests.get(url)
    response.raise_for_status()
    markdown = response.text

    apis = []
    category = "Uncategorized"

    # Split by category headers
    sections = re.split(r"(## .+?)\n", markdown)[1:]
    for i in range(0, len(sections), 2):
        category = sections[i].strip()[3:].strip()
        section_content = sections[i+1]
        
        # Extract all rows in this section
        rows = re.findall(r"\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|\n", section_content)
        for row in rows:
            api = {
                "API": row[0].strip(),
                "Description": row[1].strip(),
                "Auth": row[2].strip(),
                "HTTPS": row[3].strip().lower() == "yes",
                "CORS": row[4].strip().lower() == "yes",
                "Link": row[5].strip(),
                "Category": category,
            }
            apis.append(api)

    return apis