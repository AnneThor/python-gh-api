import requests
from os import environ
import base64

access_token = environ['GITHUB_ACCESS_TOKEN']
repo_name=""
owner="annethor"

def create_repo():
    repo_name = input("Please enter the new repository name: ")
    repo_description=input("Please enter a repo description")
    resp=requests.post(
        ' https://api.github.com/user/repos',
        headers={
            'Authorization': f'Bearer {access_token}'
        },
        json={
            'name': f'{repo_name}',
            'description': f'{repo_description}',
            'homepage': 'https://github.com',
            'private': False,
            'has_issues': True,
            'has_projects': True,
            'has_wiki': True  
            }
    )
    print(resp.status_code)

def add_file_to_repo(owner, repo_name, file_name, commit_message):
    base_64_content=read_file_to_base_64(file_name)
    resp=requests.put(
        f'https://api.github.com/repos/{owner}/{repo_name}/contents/{file_name}',
        headers={
            'Authorization': f'Bearer {access_token}'
        },
        json={
            'message': commit_message,
            'content': base_64_content
        }
    )
    print(f'Add file: {file_name} response code: {resp.status_code}')

def add_this_file_to_repo(user_name, repo_name, file_name):
    with open(__file__, 'r') as this_file:
        this_file_as_str = this_file.read()
    resp=requests.put(
        f'https://api.github.com/repos/{user_name}/{repo_name}/contents/{file_name}',
        headers={
            'Authorization': f'Bearer {access_token}'
        },
        json={
            'message': 'reading script file',
            'content': base64.b64encode(this_file_as_str.encode('utf-8')).decode('utf-8')
        }
    )
    print(f'Add file: {file_name} response code: {resp.status_code}')

def read_file_to_string(file_name):
    with open(file_name, 'r') as file:
        file_contents = file.read()
    return file_contents

def read_file_to_base_64(file_name):
    file_content=read_file_to_string(file_name)
    return base64.b64encode(file_content.encode('utf-8')).decode('utf-8')

# create_repo()
# add_file_to_repo('annethor', 'python-gh-api', 'gh-readme.md', 'first commit-README')
add_this_file_to_repo('annethor', 'python-gh-api', 'github_repo.py')

# If you put this in your script it will open in a new window 
# You'll need to impor the webbrowser package
# webbrowser.open(create_repo_response.json()['html_url'], new=0, autoraise=True)