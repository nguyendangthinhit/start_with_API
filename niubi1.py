import requests

# URL của API public (không cần đăng nhập)
url = "https://meme-api.com/gimme"

# Gửi yêu cầu GET tới API
response = requests.get(url)
# Kiểm tra phản hồi thành công không (status code 200)
if response.status_code == 200:
    data = response.json()  # Chuyển phản hồi JSON thành dict Python
    print("🔥 Here's a random meme!")
    print("Title:", data['title'])
    print("Subreddit:", data['subreddit'])
    print("URL:", data['url'])  # Đây là link ảnh meme
else:
    print("Oops! Không lấy được meme rồi 😢")

