import requests

# pull_requests = requests.get(f"https://api.github/repos/Wordz278")


def pull_requests(owner, repo_name, start_date, end_date):
    pull_requests = requests.get(
        f"https://api.github.com/repos/{owner}/{repo_name}/pulls?state=all")
    pr = pull_requests.json()


print(pull_requests("Wordz278", "api_project", "asfdksahf", "asda"))
