import requests
url = "https://manhwaread.com/manhwa/cleaning-service/chapter-25/"
reponse = requests.get(url)
print(reponse.content)