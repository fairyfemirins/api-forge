# API Forge

**A CLI tool to search and scaffold API integrations from [public-apis/public-apis](https://github.com/public-apis/public-apis).**

![Demo](https://via.placeholder.com/600x400?text=API+Forge+Demo)

## Features
- **Search APIs** by category, HTTPS support, and authentication type.
- **Scaffold Python code** for API requests (using `requests`).
- **Cache the dataset** locally for offline use.

## Note
This repository was published under `fairyfemirins` due to GitHub namespace restrictions. A transfer to `femirins` is pending.

To request a transfer, open an issue in this repository or contact `@femirins` on GitHub.

## Installation
```bash
pip install api-forge
```

## Usage
```bash
# Update the local API cache
api-forge update

# Search for free, HTTPS-enabled APIs in the "Animals" category
api-forge search --category "Animals" --https
```

## Technical Architecture
- **Scraper:** Parses the `public-apis` README.md into structured JSON.
- **Cache:** Stores the dataset locally at `~/.api-forge/public_apis.json`.
- **CLI:** Built with `typer` and `rich` for a user-friendly experience.

## License
MIT