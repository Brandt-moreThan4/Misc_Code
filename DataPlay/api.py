import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()

print(f"Total reps: {response_dict['total_count']}")

repo_dicts = response_dict['items']
repo = repo_dicts[0]

for key in sorted(repo.keys()):
    print(key)
