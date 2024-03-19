from flask import Blueprint, render_template
from API.api import GetAllProducts, GetSingleProducts
from .recommendation import get_recommended_products

products_bp = Blueprint('products_bp', __name__,
                        template_folder='templates',
                        static_folder='static')

# Define GetCategories function
def GetCategories():
    # Your logic to fetch categories goes here
    categories = ['Category 1', 'Category 2', 'Category 3']
    return categories

@products_bp.route('/products')
def index():
    data = GetAllProducts()
    l = len(data)
    categories = set(product["category"] for product in data)
    return render_template('products/products.html', length=l, products=data, categories=categories)
    
@products_bp.route('/products/<int:id>')
def detailOfProduct(id):
    data = GetSingleProducts(id)
    recommended_products = get_recommended_products(id)  # Fetch recommended products
    return render_template('products/detail.html', detailOfProduct=data, recommended_products=recommended_products)

@products_bp.route('/products/add')
def add_product():
    Categories = GetCategories()  # Call GetCategories function
    return render_template('products/newproducts.html', categories=Categories)
