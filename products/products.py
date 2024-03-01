from flask import Blueprint, render_template
from API.api import GetAllProducts, GetSingleProducts
from .recommendation import get_recommended_products

products_bp = Blueprint('products_bp', __name__,
                        template_folder='templates',
                        static_folder='static')

@products_bp.route('/products')
def index():
    data = GetAllProducts()
    l = len(data)
    categories = set(product["category"] for product in data)
    return render_template('products/products.html', length = l, products = data, categories = categories)
    

@products_bp.route('/products/<int:id>')
def detailOfProduct(id):
    data = GetSingleProducts(id)
    recommended_products = get_recommended_products(id)  # Fetch recommended products
    return render_template('products/detail.html', detailOfProduct=data, recommended_products=recommended_products)
