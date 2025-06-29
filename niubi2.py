import requests

url = "https://api.github.com/repos/nguyendangthinhit/start_with_API"
response = requests.get(url)

if response.status_code == 200:
    repo_info = response.json()
    print("📦 Repo name:", repo_info['name'])
    print("👤 Owner:", repo_info['owner']['login'])
    print("⭐ Stars:", repo_info['stargazers_count'])
    print("📝 Description:", repo_info['description'])
    print("📅 Created at:", repo_info['created_at'])
else:
    print("Lấy thông tin repo thất bại 😢")
