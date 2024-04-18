from odoo import api, fields, models
from odoo.exceptions import ValidationError

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag"
    _order = "name"

    name = fields.Char(
        required = True,
    )

    color = fields.Integer()

    @api.constrains('name')
    def _check_unique_name(self):
        for tag in self:
            if self.search_count([('name', '=', tag.name)]) > 1:
                raise ValidationError("The name must be unique")