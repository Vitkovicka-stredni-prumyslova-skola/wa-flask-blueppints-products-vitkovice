from flask import Blueprint, render_template, request, redirect, url_for
import requests

products_bp = Blueprint('products_bp', __name__,
                        template_folder='templates',
                        static_folder='static')

FAKE_STORE_API_URL = 'https://fakestoreapi.com/products'

@products_bp.route('/products/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # Získání dat z formuláře
        title = request.form.get('title')
        image = request.form.get('img')
        description = request.form.get('description')
        category = request.form.get('category')
        price = float(request.form.get('price'))

        # Příprava dat pro odeslání na Fake Store API
        new_product_data = {
            'title': title,
            'image': image,
            'description': description,
            'category': category,
            'price': price
        }

        # Odeslání POST požadavku na Fake Store API
        response = requests.post(FAKE_STORE_API_URL, json=new_product_data)

        if response.status_code == 201:
            # Úspěšné vložení produktu, přesměrování na domovskou stránku
            return redirect(url_for('products_bp.index'))
        else:
            # Pokud se nezdaří vložení produktu, zobrazíme chybovou zprávu
            error_message = 'Nepodařilo se vložit produkt, prosím zkuste to znovu.'
            return render_template('products/newproducts.html', error_message=error_message)

    else:
        # Pokud je požadavek GET, zobrazíme formulář pro vložení produktu
        return render_template('products/newproducts.html')
