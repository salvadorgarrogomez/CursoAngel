from datetime import datetime, timedelta
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"
    _order = "price desc"

    price = fields.Float(
        string="Price",
    )

    status = fields.Selection([
        ('accepted', "Accepted"),
        ('refused', "Refused"),
        ], 
        string="Status", 
        copy=False,
    )

    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner",
    )

    property_id = fields.Many2one(
        comodel_name='living.place',
    )

    property_type_id = fields.Many2one(
        related="property_id.property_type",
        string="Property Type",
        store=True,
    )

    validity = fields.Integer(
        string="Validity (days)",
        default=7,
    )

    create_date=fields.Date(
        default=fields.Date.today,
    )

    date_deadline = fields.Date(
        string="Deadline",
        compute="_compute_date_deadline",
        inverse = "_inverse_date_deadline",
    )

    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for offer in self:
            offer.date_deadline = datetime.now() + timedelta(days=offer.validity)

    def _inverse_date_deadline(self):
        for offer in self:
            offer.validity = (offer.date_deadline - offer.create_date).days

    @api.constrains('price')
    def _check_selling_price(self):
        for offer in self:
            if offer.property_id:
                expected_price = offer.property_id.expected_price
                ninety_percent_expected_price = expected_price * 0.9
                if float_compare(offer.price, ninety_percent_expected_price, precision_digits=2) == -1:
                    raise ValidationError("The selling price must be at least 90% of the expected price! You must reduce the expected price if you want to accept this offer")

    def action_confirm(self):
        for offer in self:
            offer._check_selling_price()
            if offer.status != 'accepted':
                if offer.property_id.offer_ids.filtered(lambda o: o.status == 'accepted'):
                    raise UserError("There is already an accepted offer for this property.")
                offer.property_id.selling_price = offer.price
                offer.property_id.partner_id = offer.partner_id
                offer.write({'status': 'accepted'})


    def action_refused(self):
        for offer in self:
            if offer.status == 'accepted':
                offer.property_id.selling_price = 0.0
            offer.write({'status': 'refused'})

    @api.constrains('price')
    def _check_price(self):
        for record in self:
            if record.price < 0:
                raise ValidationError("The expected price must be strictly positive")
                
