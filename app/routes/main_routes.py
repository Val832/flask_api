from flask import Blueprint, jsonify, request
from sqlalchemy import text
from app.models.models import *
from app import db 

# Création d'un blueprint pour les routes principales de l'application Flask.
main_bp = Blueprint('main_bp', __name__)

# Route pour obtenir les détails d'un produit spécifique par son ID.
@main_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product_details(product_id):
    # Requête SQL pour sélectionner les informations d'un produit spécifique.
    sql_query = text("""
    SELECT p.productid, p.name, p.description, 
           pr.unitpricedisplay, f.description as featuredescription 
    FROM product p
    JOIN pricing pr ON p.productID = pr.productID
    JOIN feature f ON p.productID = f.productID
    WHERE p.productID = :product_id;
    """)

    # Exécution de la requête SQL avec le paramètre product_id.
    product = db.session.execute(sql_query, {'product_id': product_id}).fetchone()

    # Si le produit n'existe pas, retourner une erreur 404.
    if product is None:
        return jsonify({"error": "Product not found"}), 404

    # Convertir le résultat en dictionnaire et le retourner en JSON.
    product_dict = product._asdict()
    return jsonify(product_dict)

# Route pour obtenir le nombre de produits disponibles à l'achat.
@main_bp.route('/purchasable-products-count', methods=['GET'])
def get_purchasable_products_count():
    # Compter le nombre de produits disponibles à l'achat.
    count = db.session.query(Product).filter(Product.Purchasable == True).count()
    return jsonify(purchasable_products_count=count)

# Route pour obtenir le nombre de produits par catégorie.
@main_bp.route('/products-per-category', methods=['GET'])
def products_per_category():
    # Requête SQL pour compter les produits par catégorie.
    sql_query = text("""
    SELECT primarycategoryname, 
           COUNT(productid) 
    FROM product 
    GROUP BY primarycategoryname;
    """)

    # Exécution de la requête SQL et récupération des résultats.
    result = db.session.execute(sql_query)
    categories = result.fetchall()
    
    # Conversion des résultats en dictionnaire.
    categories_dict = {category[0]: category[1] for category in categories}
    
    # Retourner le résultat en JSON.
    return jsonify(categories_dict)

# Route pour mettre à jour le statut d'un produit.
@main_bp.route('/products/<int:product_id>/status', methods=['PUT'])
def update_product_status(product_id):
    # Récupération du nouveau statut depuis le corps de la requête JSON.
    new_status = request.json.get('status', '')
    
    # Vérification que le statut n'est pas vide.
    if not new_status:
        return jsonify({"error": "Status is required"}), 400

    # Mise à jour du statut dans la base de données.
    sql_query = text("""
    UPDATE Product SET ProductStatus = :status 
    WHERE ProductID = :product_id;
    """)
    db.session.execute(sql_query, {'status': new_status, 'product_id': product_id})
    db.session.commit()

    # Message de succès retourné en JSON.
    return jsonify({"message": "Product status updated successfully"}), 200

# Exemple de commande curl pour tester la mise à jour du statut.
#curl -X PUT -H "Content-Type: application/json" -d '{"status":"non dispo"}' http://localhost:5000/products/120/status

# Route pour mettre à jour le prix d'un produit.
@main_bp.route('/products/<int:product_id>/pricing', methods=['PUT'])
def update_pricing(product_id):
    # Récupération du nouveau prix depuis le corps de la requête JSON.
    new_price = request.json.get('new_price')
    
    # Mise à jour du prix dans la base de données.
    sql_query = text("""
    UPDATE pricing SET amountinctax = :new_price
    WHERE productid = :product_id;
    """)
    db.session.execute(sql_query, {'new_price': new_price, 'product_id': product_id})
    db.session.commit()

    # Message de succès retourné en JSON.
    return jsonify({"message": "Pricing updated"}), 200

# Exemple de commande curl pour tester la mise à jour du prix.
#curl -X PUT http://localhost:5000/products/3/pricing -H "Content-Type: application/json" -d '{"new_price": 19.99}'

# Route pour supprimer un produit par son ID.
@main_bp.route('/del-product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    # Vérification de l'existence du produit avant de tenter de le supprimer.
    exist_query = text("""
    SELECT EXISTS(SELECT 1 FROM product WHERE productid = :product_id)
    """)
    exists = db.session.execute(exist_query, {'product_id': product_id}).scalar()
    
    # Si le produit n'existe pas, retourner une erreur 404.
    if not exists:
        return jsonify({"error": "Product not found"}), 404

    # Suppression du produit s'il existe.
    delete_query = text("""
    DELETE FROM product WHERE productid = :product_id
    """)
    db.session.execute(delete_query, {'product_id': product_id})
    db.session.commit()

    # Message de succès retourné en JSON.
    return jsonify({"message": "Product deleted successfully"}), 200

# Exemple de commande curl pour tester la suppression d'un produit.
#curl -X DELETE http://localhost:5000/del-products/1
