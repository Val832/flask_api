from flask import Blueprint, jsonify
from flask import jsonify
from sqlalchemy import func, text
from app.models.models import Product # Assurez-vous que cet import est correct en fonction de la structure de votre dossier
from app import db # Assurez-vous que cet import est correct en fonction de la structure de votre dossier


# Création d'un blueprint pour les routes principales.
main_bp = Blueprint('main_bp', __name__)

# Une route simple qui renvoie "Hello, World!" au format JSON.
@main_bp.route('/')
def hello_world():
    return jsonify(message="Hello, World!")

@main_bp.route('/kpi/purchasable-products-count', methods=['GET'])
def get_purchasable_products_count():
    count = db.session.query(Product).filter(Product.Purchasable == True).count()
    return jsonify(purchasable_products_count=count)

@main_bp.route('/products-per-category', methods=['GET'])
def products_per_category():

    sql_query = text("select primarycategoryname, count(productid) from product group by primarycategoryname ;")
    #category_counts = db.session.query(Product.PrimaryCategoryName, 
                                       #func.count(Product.ProductID)).group_by(Product.PrimaryCategoryName).all()
    
    #result = {category: count for category, count in category_counts}
    
    result = db.session.execute(sql_query)
    categories = result.fetchall()
    
    print = {category[0]: category[1] for category in categories}
    
    return jsonify(print)

@main_bp.route('/products/<string:ean>', methods=['GET'])
def get_product_details(ean):
    # construction de la requête sql
    sql_query = text("SELECT * FROM product WHERE ean = :ean;")
    

    # On éxécute la requête sql et on récupère son contenu 
    result = db.session.execute(sql_query, {'ean':ean})
    product = result.fetchone()

    #On vérifie que le produit soit trouvé 
    if product:
        # On convertit en dictionnaire 
        product_data = product._asdict()
        return jsonify(product_data), 200
    else:
        return jsonify({"error": "Product not found"}), 404
