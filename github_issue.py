# encoding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import requests
from config import USERNAME, REPO_OWNER, REPO_NAME


def make_github_issue(title, body=None, assignee=USERNAME, closed=False, labels=None, TOKEN="TOKEN_needed"):
    """Create a GitHub issue without making issue failures fatal to email delivery.

    The workflow passes GitHub Actions' built-in GITHUB_TOKEN, so no personal
    access token needs to be stored or rotated for this repository. Network/API
    failures are logged and returned as False rather than raised: the daily
    email is the primary delivery channel and must not be duplicated by the
    semantic workflow's legacy fallback merely because issue creation failed.
    """
    url = "https://api.github.com/repos/{}/{}/issues".format(REPO_OWNER, REPO_NAME)
    headers = {
        "Authorization": "Bearer {}".format(TOKEN),
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    data = {
        "title": title,
        "body": body or "",
    }
    if assignee:
        data["assignees"] = [assignee]
    if labels:
        data["labels"] = labels

    try:
        response = requests.post(url, json=data, headers=headers, timeout=30)

        # Some historical keyword labels may not exist in the repository. If
        # GitHub rejects metadata, retry once with only title/body.
        if response.status_code == 422 and ("labels" in data or "assignees" in data):
            response = requests.post(
                url,
                json={"title": title, "body": body or ""},
                headers=headers,
                timeout=30,
            )
    except requests.RequestException as exc:
        print('Could not create Issue "{}": {}'.format(title, exc))
        return False

    if response.status_code == 201:
        print('Successfully created Issue "{}"'.format(title))
        print(response.status_code)
        return True

    print('Could not create Issue "{}"'.format(title))
    print("Response:", response.text)
    print(response.status_code)
    return False


if __name__ == '__main__':
    make_github_issue(
        title='Pretty title',
        body='Beautiful body',
        assignee=USERNAME,
        closed=False,
        labels=["imagenet", "image retrieval"],
    )
