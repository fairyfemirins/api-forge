import json
import os
import requests
from pathlib import Path
from typing import List, Optional
from rich.console import Console
from rich.table import Table

# Path to local cache
DATA_DIR = Path(__file__).parent / "data"
CACHE_FILE = DATA_DIR / "public_apis.json"
console = Console()


def fetch_public_apis() -> List[dict]:
    """Fetch the latest public-apis dataset from GitHub."""
    url = "https://raw.githubusercontent.com/public-apis/public-apis/master/src/data.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def load_cached_apis() -> List[dict]:
    """Load APIs from local cache."""
    if not CACHE_FILE.exists():
        return []
    with open(CACHE_FILE, "r") as f:
        return json.load(f)


def save_apis_to_cache(apis: List[dict]) -> None:
    """Save APIs to local cache."""
    DATA_DIR.mkdir(exist_ok=True)
    with open(CACHE_FILE, "w") as f:
        json.dump(apis, f)


def update_cache() -> None:
    """Update the local API cache."""
    apis = fetch_public_apis()
    save_apis_to_cache(apis)
    console.print(f"[green]Updated cache with {len(apis)} APIs.[/green]")


def search_apis(
    category: Optional[str] = None,
    https: Optional[bool] = None,
    auth: Optional[str] = None,
) -> None:
    """Filter APIs by category, HTTPS, and authentication."""
    apis = load_cached_apis()
    if not apis:
        console.print("[red]Cache is empty. Run 'api-forge update' first.[/red]")
        return
    results = apis
    if category:
        results = [api for api in results if api.get("Category", "").lower() == category.lower()]
    if https is not None:
        results = [api for api in results if api.get("HTTPS", False) == https]
    if auth:
        results = [api for api in results if api.get("Auth", "").lower() == auth.lower()]

    table = Table(title="API Search Results")
    table.add_column("API")
    table.add_column("Category")
    table.add_column("Description")
    table.add_column("HTTPS")
    table.add_column("Auth")

    for api in results:
        table.add_row(
            api.get("API", "N/A"),
            api.get("Category", "N/A"),
            api.get("Description", "N/A"),
            "✓" if api.get("HTTPS", False) else "✗",
            api.get("Auth", "None"),
        )
    console.print(table)