import os, re, sys
import subprocess as sb
import requests
from encryption import decrypt
from github import Github

def validate_path(path):
    if os.path.exists(path):
        return True
    print('Path: {} doesn\'t exists')
    sys.exit(1)

def check_configuration():
    file = open('configuration.txt')
    project_location_pattern = r'^Project File\s?:\s?\'(.*)\''
    username_pattern = r'^User\s?:\s?\'(.*)\''
    password_pattern = r'^Password\s?:\s?\'(.*)\''
    username = 'None'
    password = 'None'
    project_path = ''
    for line in file:
        line = line.strip()
        username_match = re.search(username_pattern, line)
        password_match = re.search(password_pattern, line)
        project_location = re.search(project_location_pattern, line)
        if project_location != None:
            project_path = project_location.group(1)
        if username_match != None:
            username = username_match.group(1)
        if password_match != None:
            password = password_match.group(1)
    validate_path(project_path)
    if len(username) is 0 or len(password) is 0:
        print('Please provide valid username or password')
        sys.exit(1)
    return project_path, decrypt(username), decrypt(password)

def create_project_with_name(project_name):
    project_path, username, password = check_configuration()
    for i in range(3):
        successful_trial = 0
        unsuccessful_trial = 0
        try:
            print('Logging in...')
            login = Github(username, password) # login with github API
            try:
                login.get_user().get_repo(project_name)
                break
            except Exception:
                pass
            login.get_user().create_repo(project_name) # Create the repo
            successful_trial += 1
            print('Created a repo on github')
            break
        except Exception:
            unsuccessful_trial += 1
    os.chdir(project_path)
    try:
        os.mkdir(project_name) # make the project directory
        print('Made directory in your specified path for projects')
    except Exception:
        pass
    os.chdir('./{}'.format(project_name))
    if not '.git' in os.listdir():
        os.system('git init') # initialize it with git
    if unsuccessful_trial is 3:
        print('Can\'t login using the username, create a manual repo and adding a remote origin to it')
    else:
        print('Adding remote origin...')
        sb.run(['git', 'remote', 'add', 'origin', 'https://github.com/{}/{}.git'.format(username, project_name)], capture_output = True)
        print('Pushing origin master...')
        sb.run(['git', 'push', '-u', 'origin', 'master'], capture_output = True)
        sb.run(['git', 'push', '--set-upstream', 'origin', 'master'], capture_output = True)
    print('Done')
    if project_path.endswith('/'):
        return project_path + project_name
    return project_path + '/' + project_name

if __name__ == '__main__':
    # convert spaces to underscores
    project_name = input('Enter your new project name: ').strip().replace(' ', '_')
    create_project_with_name(project_name)