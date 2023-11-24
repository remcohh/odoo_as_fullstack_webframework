# models/application.py
from odoo import models, fields

class Application(models.Model):
    _name = 'webframework_example_qweb_basic.book'
    _description = 'Book Model'
    title = fields.Char(string='Name', required=True)