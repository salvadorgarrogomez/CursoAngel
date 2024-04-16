from datetime import datetime, timedelta
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

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
        ('north', "North"),
        ('south', "South"),
        ('east', "East"),
        ('west', "West")],
        string = "Garden Orientation",
    )

    active = fields.Boolean(
        default = True,
    )

    state = fields.Selection(
        [('new', "New"),
         ('offer received', "Offer Recceived"),
         ('offer Accepted', "Offer Accepted"),
         ('sold', "Sold"),
         ('canceled', "Canceled")],
         string = "Status",
         default = "new",
         readonly=True,
    )

    user_id = fields.Many2one(
        comodel_name = "res.users",
        string = "Salesman",
        default = lambda self: self.env.user,
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

    total_area = fields.Float(
        compute = "_compute_total_area",
    )

    def _compute_total_area(self):
        for place in self:
            total_area = place.living_area + place.garden_area
            place.total_area = total_area

    best_price = fields.Float(
        compute = "_compute_best_price",
        string = "Best Offer",
    )

    def _compute_best_price(self):
        for place in self:
            if place.offer_ids:
                prices = [offer.price for offer in place.offer_ids]
                place.best_price = max(prices)
            else:
                place.best_price = 0.0 

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = self.garden_area or 10
            self.garden_orientation = self.garden_orientation or 'north'
        else:
            self.garden_area = False
            self.garden_orientation = False

    def value_sold(self):
        if self.state == 'canceled':
            raise UserError("Canceled properties cannot be sold.")
        else:
            self.write({'state':'sold'})

    def value_canceled(self):
        self.write({'state': 'canceled'})

    @api.constrains('expected_price')
    def _check_expected_price(self):
        for record in self:
            if record.expected_price <= 0:
                raise ValidationError("The expected price must be strictly positive")
            
    @api.constrains('selling_price')
    def _check_selling_price(self):
        for record in self:
            if record.selling_price < 0:
                raise ValidationError("The expected price must be strictly positive")