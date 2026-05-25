import json
from pathlib import Path
from typing import List


def scaffold_api_request(api: dict, output_dir: Path) -> None:
    """Generate Python code for API requests."""
    output_dir.mkdir(exist_ok=True)
    code = f"""import requests

# {api['API']} - {api['Description']}
# Docs: {api['Link']}

def fetch_data():
    url = "{api['Link']}"
    headers = {{}}
    params = {{}}

    # Add authentication if required
    if "{api.get('Auth', '')}":
        headers["Authorization"] = "Bearer YOUR_API_KEY"

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    data = fetch_data()
    print(data)
"""
    (output_dir / f"{api['API'].lower().replace(' ', '_')}.py").write_text(code)


if __name__ == "__main__":
    # Example usage
    api = {
        "API": "Cat Facts",
        "Description": "Daily cat facts",
        "Auth": "",
        "HTTPS": True,
        "Link": "https://catfact.ninja/fact"
    }
    scaffold_api_request(api, Path("examples"))