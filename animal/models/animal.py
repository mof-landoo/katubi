# Copyright (C) 2020 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models
import datetime

class Animal(models.Model):
    _name = "animal"
    _description = "Animal"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "contract_number"


    company_id = fields.Many2one('res.company', 'Company', required=True,
                                 index=True,
                                 default=lambda self: self.env.company)
    name = fields.Char(string="Nombre")
    ref = fields.Char(string="Reference")
    gender = fields.Selection(string="Sexo",
        selection=[
            ("female", "Hembra"),
            ("male", "Macho"),
        ],
        required=False,
    )
    contract_number = fields.Integer(string="Nº Contrato", size=4)
    contract_number_year = fields.Char(string="Nº Contrato/Año", size=7)

    @api.onchange("contract_number")
    def _compute_cny(self):
        self.contract_number_year = str(self.contract_number) + "/" + datetime.date.today().strftime('%y')

    color_id = fields.Many2one("animal.color", string="Color")
    fur = fields.Selection(string="Pelo",
        selection=[
            ("largo", "Largo"),
            ("corto", "Corto")
        ]
    )
    #weight = fields.Float(string="Weight (in kg)")
    katubi_name = fields.Char(string="Nombre Katubihotz")
    birth_date = fields.Date(string="Fecha Nacimiento")
    adoption_date = fields.Date(string="Fecha Adopción")
    paid_chip = fields.Boolean(string="Chip pagado")

    despa = fields.Selection(string="Desparasitado",
                             selection=[('si','Sí'),('no','No')])
    ester = fields.Selection(string="Esterilizado",
                             selection=[('si', 'Sí'), ('no', 'No')])
    chip = fields.Selection(string="Chip",
                            selection=[('si', 'Sí'), ('no', 'No')])
    vacuna = fields.Selection(string="Vacunado",
                             selection=[('si','Sí'),('no','No')])
    leuc = fields.Selection(string="Leucemia felina",
                            selection=[
                                ('si','Positivo'),
                                ('no','Negativo')
                            ])
    inmuno = fields.Selection(string="Inumunodeficiencia felina",
                            selection=[
                                ('si','Positivo'),
                                ('no','Negativo')
                            ])

    active = fields.Boolean(default=True)

    partner_id = fields.Many2one(
        "res.partner", string="Owner", index=True, tracking=True, default=3
    )
    firma = fields.Boolean("Firma", default=False)
    cub = fields.Boolean("Cría", default=False)
    image = fields.Binary(
        attachment=True, help="This field holds the photo of the animal."
    )

    @api.model_create_multi
    def create(self, vals):
        animals = super(Animal, self).create(vals)
        for animal in animals:
            if not animal['contract_number_year']:
                animal['contract_number_year'] = str(animal["contract_number"]) + "/" + datetime.date.today().strftime('%y')
        return animals





