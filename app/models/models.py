from flask import Flask

from app import db

class Product(db.Model):
    ProductID = db.Column(db.Integer, primary_key=True, name='productid')
    EAN = db.Column(db.String, name='ean')
    Name = db.Column(db.String, name='name')
    ShortName = db.Column(db.String, name='shortname')
    Description = db.Column(db.Text, name='description')
    FeatureSummary = db.Column(db.Text, name='featuresummary')
    ProductStatus = db.Column(db.Text, name='productstatus')
    ProductConfiguratorType = db.Column(db.Text, name='productconfiguratortype')
    SundayDeliveryAvailable = db.Column(db.Boolean, name='sundaydeliveryavailable')
    PrimaryCategoryId = db.Column(db.Integer, name='primarycategoryid')
    PrimaryCategoryName = db.Column(db.String, name='primarycategoryname')
    Purchasable = db.Column(db.Boolean, name='purchasable')
    ContactCentreOrderingOnly = db.Column(db.Boolean, name='contactcentreorderingonly')
    PDPURL = db.Column(db.Text, name='pdpurl')
    PublishingStatus = db.Column(db.Text, name='publishingstatus')
    DisplayCoverageCalculator = db.Column(db.Boolean, name='displaycoveragecalculator')


class Pricing(db.Model):
    PricingID = db.Column(db.Integer, primary_key=True)
    ProductID = db.Column(db.Integer, db.ForeignKey('product.ProductID'))
    CurrencyCode = db.Column(db.String)
    UnitOfMeasure = db.Column(db.Text)
    UnitPriceDisplay = db.Column(db.Boolean)
    AmountIncTax = db.Column(db.Float)
    AmountExtTax = db.Column(db.Float)
    DeliveryChargeIdentifier = db.Column(db.Text)
    DeliveryChargeThreshold = db.Column(db.Float)
    DeliveryChargeAboveThreshold = db.Column(db.Float)
    DeliveryChargeBelowThreshold = db.Column(db.Float)

class Tax(db.Model):
    TaxID = db.Column(db.Integer, primary_key=True)
    PricingID = db.Column(db.Integer, db.ForeignKey('pricing.PricingID'))
    Type = db.Column(db.Text)
    Amount = db.Column(db.Float)
    Rate = db.Column(db.Float)

class Feature(db.Model):
    FeatureID = db.Column(db.Integer, primary_key=True)
    ProductID = db.Column(db.Integer, db.ForeignKey('product.ProductID'))
    Description = db.Column(db.Text)

class Manual(db.Model):
    ManualID = db.Column(db.Integer, primary_key=True)
    ProductID = db.Column(db.Integer, db.ForeignKey('product.ProductID'))
    FriendlyName = db.Column(db.Text)
    URL = db.Column(db.Text)
    Type = db.Column(db.Text)

class URL(db.Model):
    URLID = db.Column(db.Integer, primary_key=True)
    ProductID = db.Column(db.Integer, db.ForeignKey('product.ProductID'))
    SeoId = db.Column(db.Text)
    SeoText = db.Column(db.Text)
    ShareableUrl = db.Column(db.Text)

class Rating(db.Model):
    RatingID = db.Column(db.Integer, primary_key=True)
    ProductID = db.Column(db.Integer, db.ForeignKey('product.ProductID'))
    Value = db.Column(db.Float)
    Count = db.Column(db.Integer)

class TechnicalSpecification(db.Model):
    TechSpecID = db.Column(db.Integer, primary_key=True)
    ProductID = db.Column(db.Integer, db.ForeignKey('product.ProductID'))
    Name = db.Column(db.String)
    Value = db.Column(db.Text)

if __name__ == '__main__':
    db.create_all()
