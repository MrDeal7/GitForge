# GitForge

A personal portfolio website that automatically fetches and displays your GitHub repositories.  
Built with Python and Jinja2. Deployed via GitHub Pages with automatic updates through GitHub Actions.

## How it works

1. `main.py` calls the GitHub API to fetch your public repositories.
2. It filters, sorts, and groups repos by language.
3. Jinja2 fills in `templates/index.html` with the real data.
4. The output is written to `index.html` at the project root.
5. GitHub Actions runs this script automatically and publishes the result to GitHub Pages.

## Project structure

```
GitForge/
├── main.py               # Fetches repos and generates index.html
├── config.json           # Your personal info (name, bio, email, GitHub username)
├── templates/
│   └── index.html        # Jinja2 HTML template
├── index.html            # Generated output (do not edit manually)
└── .github/
    └── workflows/
        └── deploy.yml    # GitHub Actions workflow
```

## Setup

**Requirements**
- Python 3.10+
- pip packages: `requests`, `jinja2`

**Install dependencies**
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install requests jinja2
```

**Generate the page locally**
```bash
python main.py
```

Then open `index.html` in your browser.

## Configuration

Edit `config.json` to update your info:

```json
{
  "name": "Your Name",
  "github_username": "your-username",
  "bio": "A short description about you.",
  "email": "you@example.com"
}
```

## Language grouping

Repos with `JavaScript` or `TypeScript` as their primary language are grouped under the **Fullstack Web Page** filter tab.  
All other languages get their own tab automatically.  
Repos without a description are excluded from the listing.
