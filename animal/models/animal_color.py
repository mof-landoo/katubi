# Copyright (C) 2020 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class AnimalColor(models.Model):
    _name = "animal.color"
    _description = "Animal Colors"

    name = fields.Char(translate=True)