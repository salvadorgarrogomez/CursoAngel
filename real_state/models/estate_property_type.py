from odoo import api, fields, models
from odoo.exceptions import ValidationError

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"
    _order = "name"
    _order = "sequence"

    name = fields.Char(
        required = True,
    )

    sequence = fields.Integer()

    type_ids = fields.One2many(
        comodel_name='living.place',
        inverse_name='property_type',
    )

    @api.constrains('name')
    def _check_unique_name(self):
        for tag in self:
            if self.search_count([('name', '=', tag.name)]) > 1:
                raise ValidationError("The name must be unique")