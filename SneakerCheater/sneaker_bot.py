import requests
from fake_useragent import UserAgent

ua = UserAgent()
headers = {"User-Agent": ua.random}

def search_sneakers(query, max_price):
    print(f"Searching for {query} with max price {max_price}...")
    sneakers = [
        {"brand": "Nike", "name": "Air Jordan 1", "price": 150},
        {"brand": "Adidas", "name": "Yeezy 350", "price": 220}
    ]
    filtered_sneakers = [s for s in sneakers if s['price'] <= max_price]
    return filtered_sneakers

sneakers = search_sneakers("Air Jordan", 200)
for sneaker in sneakers:
    print(sneaker)
