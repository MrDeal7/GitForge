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
	print(response)
	repos = response.json()
	return render_template("index.html", config=config, repos=repos)
	
if __name__ == "__main__":
	app.run(debug=True)