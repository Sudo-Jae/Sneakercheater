import time
import random
def find_sneakers(brand, shoe_type, price_range):
    print(f"Searching for {brand} {shoe_type} within {price_range} range...")
    time.sleep(random.randint(1, 3))
    return {"status": "success", "sneakers": [{"brand": brand, "type": shoe_type, "price": price_range}]}
if __name__ == "__main__":
    sneakers = find_sneakers("Nike", "Air Jordan", "00-00")
    print(sneakers)
