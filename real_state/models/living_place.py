from datetime import datetime, timedelta
from odoo import fields, models

class LivingPlace(models.Model):
    _name = "living.place"
    _description = "Living Place"

    name = fields.Char(
        string = "Title",
        required = True,
    )
    description = fields.Text(
        string = "Description",
    )
    postcode = fields.Char(
        string = "Postcode",
    )
    date_availability = fields.Date(
        string = "Availale From",
        default=lambda self: (datetime.now() + timedelta(days=90)).date(),
    )
    expected_price = fields.Float(
        string = "Expected Price",
        required=True,
    )
    selling_price = fields.Float(
        string = "Selling Price",
    )
    bedrooms = fields.Integer(
        string = "Bedrooms",
        default=2,
    )
    living_area = fields.Integer(
        string = "Living Area (sqm)",
    )
    facades = fields.Integer(
        string = "Facades",
    )
    garage = fields.Boolean(
        string = "Garage",
    )
    garden = fields.Boolean(
        string = "Garden",
    )
    garden_area = fields.Integer(
        string = "Garden Area (sqm)",
    )
    garden_orientation = fields.Selection([
        ('North', 'North'),
        ('South', 'South'),
        ('East', 'East'),
        ('West', 'West'),
        ],
        string = "Garden Orientation",
    )
    active = fields.Boolean()
    state = fields.Selection(
        [('new', "New"),
         ('offer received', "Offer Recceived"),
         ('offer Accepted', "Offer Accepted"),
         ('sold', "Sold"),
         ('canceled', "Canceled")],
         string = "Status",
         default = "new",
    )

    user_id = fields.Many2one(
        comodel_name = "res.users",
        string = "Salesman",
    )

    partner_id = fields.Many2one(
        comodel_name = "res.partner",
        string = "Buyer",
    )

    tags_id = fields.Many2many(
        comodel_name = "estate.property.tag",
    )

    property_type = fields.Many2one(
        comodel_name = "estate.property.type",
        string = "Property Type",
    )

    offer_ids = fields.One2many(
        comodel_name='estate.property.offer',
        inverse_name='property_id',
    )


