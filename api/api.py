from github import Github
from credentials import Api_Token
from urllib.parse import parse_qs

api_credentials = Api_Token()
token = api_credentials.token_code()
username = api_credentials.user_name()
user_pass = api_credentials.user_pass()


g = Github(token)

# for repo in g.get_user().get_repos():
#     print(repo.name, repo.created_at, repo.updated_at)

# repository = g.get_repos()
# pulls = repository.get_pulls()
# pulls_numbers_list = []
# for pull in pulls:
#     pulls_numbers_list.append(pull.number)
#     print(pulls_numbers_list)


class Repo:
    def repo_details(self, repo_name):
        self.repo_name = repo_name
        pass

        # for repo in g.get_pulls('closed'):
        #     details = repo.get_pull().closed_at
        # return details
        # repository = g.get_repos()
        # pulls = repository.get_pulls()
        # pulls_numbers_list = []
        # for pull in pulls:
        #     pulls_numbers_list.append(pull.number)
        # return pulls_numbers_list

        repo = g.get_repo(self.repo_name)
        repo_info = f"""
        Repo Name : {repo.name}
        Repo Created Date : {repo.created_at}
        Repo End Date : {repo.updated_at}"""
        return repo_info

        # repo_list_details = []
        # for repo in g.get_user().get_repos():
        #     repo = g.get_repo(self.repo_name )
        #     # self.repo_start_date = repo.created_at
        #     # self.repo_end_date = repo.updated_at
        #     repo_info = repo.name, repo.created_at, repo.updated_at
        #     repo_list_details.append(repo_info)
        #     list_trimmed = str(repo_list_details)
        # return repo_list_details


if __name__ == "__main__":
    test = Repo()
    print(test.repo_details("Wordz278/animal"))
