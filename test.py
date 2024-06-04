import requests

def test_search_product(product_name):
    url = "http://127.0.0.1:8000/search"
    payload = {"name": product_name}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print("Failed to get results:", response.status_code, response.json())

if __name__ == "__main__":
    # Test with an example product
    test_search_product("Iphone")