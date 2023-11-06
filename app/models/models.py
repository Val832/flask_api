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
    PricingID = db.Column(db.Integer, primary_key=True, name='pricingid')
    ProductID = db.Column(db.Integer, db.ForeignKey('product.productid'), name='productid')
    CurrencyCode = db.Column(db.String, name='currencycode')
    UnitOfMeasure = db.Column(db.Text, name='unitofmeasure')
    UnitPriceDisplay = db.Column(db.Boolean, name='unitpricedisplay')
    AmountIncTax = db.Column(db.Float, name='amountinctax')
    AmountExtTax = db.Column(db.Float, name='amountexttax')
    DeliveryChargeIdentifier = db.Column(db.Text, name='deliverychargeidentifier')
    DeliveryChargeThreshold = db.Column(db.Float, name='deliverychargethreshold')
    DeliveryChargeAboveThreshold = db.Column(db.Float, name='deliverychargeabovethreshold')
    DeliveryChargeBelowThreshold = db.Column(db.Float, name='deliverychargebelowthreshold')

class Tax(db.Model):
    TaxID = db.Column(db.Integer, primary_key=True, name='taxid')
    PricingID = db.Column(db.Integer, db.ForeignKey('pricing.pricingid'), name='pricingid')
    Type = db.Column(db.Text, name='type')
    Amount = db.Column(db.Float, name='amount')
    Rate = db.Column(db.Float, name='rate')

class Feature(db.Model):
    FeatureID = db.Column(db.Integer, primary_key=True, name='featureid')
    ProductID = db.Column(db.Integer, db.ForeignKey('product.productid'), name='productid')
    Description = db.Column(db.Text, name='description')

class Manual(db.Model):
    ManualID = db.Column(db.Integer, primary_key=True, name='manualid')
    ProductID = db.Column(db.Integer, db.ForeignKey('product.productid'), name='productid')
    FriendlyName = db.Column(db.Text, name='friendlyname')
    URL = db.Column(db.Text, name='url')
    Type = db.Column(db.Text, name='type')

class URL(db.Model):
    URLID = db.Column(db.Integer, primary_key=True, name='urlid')
    ProductID = db.Column(db.Integer, db.ForeignKey('product.productid'), name='productid')
    SeoId = db.Column(db.Text, name='seoid')
    SeoText = db.Column(db.Text, name='seotext')
    ShareableUrl = db.Column(db.Text, name='shareableurl')

class Rating(db.Model):
    RatingID = db.Column(db.Integer, primary_key=True, name='ratingid')
    ProductID = db.Column(db.Integer, db.ForeignKey('product.productid'), name='productid')
    Value = db.Column(db.Float, name='value')
    Count = db.Column(db.Integer, name='count')

class TechnicalSpecification(db.Model):
    TechSpecID = db.Column(db.Integer, primary_key=True, name='techspecid')
    ProductID = db.Column(db.Integer, db.ForeignKey('product.productid'), name='productid')
    Name = db.Column(db.String, name='name')
    Value = db.Column(db.Text, name='value')

if __name__ == '__main__':
    db.create_all()
