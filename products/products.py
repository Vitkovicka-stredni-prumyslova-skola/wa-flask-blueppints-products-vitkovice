from flask import Blueprint, render_template, request, redirect, url_for
import requests
from API.api import GetAllProducts, GetSingleProducts
from .recommendation import get_recommended_products

products_bp = Blueprint('products_bp', __name__,
                        template_folder='templates',
                        static_folder='static')

FAKE_STORE_API_URL = 'https://fakestoreapi.com/products'


def GetCategories():
   
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
    recommended_products = get_recommended_products(id) 
    return render_template('products/detail.html', detailOfProduct=data, recommended_products=recommended_products)

@products_bp.route('/products/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
    
        title = request.form.get('title')
        image = request.form.get('img')
        description = request.form.get('description')
        category = request.form.get('category')
        price = float(request.form.get('price'))

    
        new_product_data = {
            'title': title,
            'image': image,
            'description': description,
            'category': category,
            'price': price
        }


        response = requests.post(FAKE_STORE_API_URL, json=new_product_data)

        if response.status_code == 201:
     
            return redirect(url_for('products_bp.index'))
        else:
       
            error_message = 'Nepodařilo se vložit produkt, prosím zkuste to znovu.'
            return render_template('products/newproducts.html', error_message=error_message)

    else:
      
        Categories = GetCategories()  
        return render_template('products/newproducts.html', categories=Categories)
