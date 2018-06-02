import requests
import re
import subprocess

GITLAB_TAGS_API_URI = 'https://gitlab.com/api/v4/projects/QEF%2Fq-e/repository/tags'

def get_gitlab_tags() -> list:
    res = requests.get(GITLAB_TAGS_API_URI)
    tags = res.json()
    print(tags)
    return tags

def get_versions(tags: list):
    for tag in tags:
        res = re.search(r'^qe-([0-9\.]+)$', tag['name'])
        if res:
            release_version = res.group(1)
            commit_id = tag['commit']['id']
            yield release_version, commit_id, tag

if __name__ == '__main__':
    for release_version, commit_id, tag in get_versions(get_gitlab_tags()):
        proc = subprocess.Popen([
            'bash',
            './build_docset.sh',
            release_version,
            commit_id
        ])
        proc.wait()