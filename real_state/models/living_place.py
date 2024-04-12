from datetime import datetime, timedelta
from odoo import fields, models

class LivingPlace(models.Model):
    _name = "living.place"
    _description = "Living Place"

    name = fields.Char(
        required = True,
    )
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        default=lambda self: (datetime.now() + timedelta(days=90)).date(),
    )
    expected_price = fields.Float(
        required=True,
    )
    selling_price = fields.Float()
    bedrooms = fields.Integer(
        default=2,
    )
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('North', 'North'),
        ('South', 'South'),
        ('East', 'East'),
        ('West', 'West'),
    ])
    active = fields.Boolean()
    state = fields.Selection(
        [('new', "New"),
         ('offer received', "Offer Recceived"),
         ('offer Accepted', "Offer Accepted"),
         ('sold', "Sold"),
         ('canceled', "Canceled")],
         string = "State",
         default = "new",
    )
