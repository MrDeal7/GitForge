from flask import Flask, render_template
import json
import requests

app = Flask(__name__)
@app.route("/")

def home():
	with open("config.json", "r") as f:
		config = json.load(f)
	
	url = f"https://api.github.com/users/{config['github_username']}/repos"
	response = requests.get(url)
	allRepos = response.json()

	web_languages = {"JavaScript", "TypeScript", None}
	for repo in allRepos:
		language = repo.get("language")
		repo["filter_language"] = "Fullstack Web Page" if language in web_languages else language

	repos = sorted(allRepos, key=lambda r: (r["filter_language"] or "zzzz").lower())
	languages = sorted({r["filter_language"] for r in repos if r.get("filter_language")}, key=str.lower)
	return render_template("index.html", config=config, repos=repos, languages=languages)
	
if __name__ == "__main__":
	app.run(debug=True)