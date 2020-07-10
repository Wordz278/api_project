from github import Github
import datetime
import requests
import os

username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")
token = os.environ.get("TOKEN")


g = Github("Wordz278","Javas008")
g = Github(token)

def get_pull_requests(start_date:str, end_date:str, repo_name:str):
    #uMUZI organisation has been used to access the repo
    repo = g.get_repo(f"Umuzi-org/{repo_name}")
    
    pulls = repo.get_pulls(state='all', sort='created', base='master')

    for pr in pulls:
        if pr.created_at.date() == start_date and pr.closed_at.date() == end_date:
            pull_requests = {
                "Date created" : pr.created_at,
                "Date updated" : pr.updated_at,
                "Date Merged" : pr.merged_at,
                "Date Closed" : pr.closed_at,}
            print(pull_requests)
    return "done"

        
if __name__ == "__main__":
    #Date Format "YYYY,M,D"
    start_date = datetime.date(2020,7,2)
    closed_date = datetime.date(2020,7,3)
    print(get_pull_requests(start_date,closed_date,"YOUR REPO"))