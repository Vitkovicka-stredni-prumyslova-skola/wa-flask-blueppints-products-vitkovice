from API.api import GetAllProducts

def get_recommended_products(product_id, max_results=4):
    all_products = GetAllProducts()
    product = next((p for p in all_products if p['id'] == product_id), None)
    if product is None:
        return []  # Product not found, return empty list
    
    category = product['category']
    recommended_products = [p for p in all_products if p['category'] == category and p['id'] != product_id][:max_results]
    return recommended_products