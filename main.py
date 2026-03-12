import json
import requests
from jinja2 import Environment, FileSystemLoader


def main():
	with open("config.json", "r") as f:
		config = json.load(f)

	url = f"https://api.github.com/users/{config['github_username']}/repos"
	response = requests.get(url)
	allRepos = response.json()

	webLanguages = {"JavaScript", "TypeScript", None}
	for repo in allRepos:
		language = repo.get("language")
		repo["filter_language"] = "Fullstack Web Page" if language in webLanguages else language

	reposWithDescription = [r for r in allRepos if r.get("description")]
	repos = sorted(reposWithDescription, key=lambda r: (r["filter_language"] or "zzzz").lower())
	languages = sorted({r["filter_language"] for r in repos if r.get("filter_language")}, key=str.lower)

	env = Environment(loader=FileSystemLoader("templates"))
	template = env.get_template("index.html")
	html = template.render(config=config, repos=repos, languages=languages)

	with open("index.html", "w") as f:
		f.write(html)

	print("index.html generated successfully.")


if __name__ == "__main__":
	main()