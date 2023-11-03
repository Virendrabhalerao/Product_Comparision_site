import requests

def get_product_info(api_key, product_name):
    url = "https://price-api.datayuge.com/api/v1/compare/search"

    querystring = {
        "api_key": api_key,
        "product": product_name,
        "page": "1"
    }

    headers = {'content-type': 'application/json'}

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()

    if 'data' in data:
        product_info = data['data']
        return product_info
    else:
        return None

if __name__ == "__main__":
    api_key = "NkXQQnZZjAdFtrnINzCFJlMEr8AmUKyFLDh"
    product_name = input("Enter the product name: ")

    product_info = get_product_info(api_key, product_name)

    if product_info:
        print("Product Info:")
        print("Product Title:", product_info[0]['product_title'])
        print("Lowest Price:", product_info[0]['product_lowest_price'])
        print("Product Link:", product_info[0]['product_link'])
        print("Product Image:", product_info[0]['product_image'])
    else:
        print("No product found with the given name.")
