
from openerp import models, fields, api


class Book(models.Model):
    _name = 'booklibrary.book'

    name = fields.Char(string="Title", required=True)
    author = fields.Char(string="Author", required=True)
    date = fields.Date(string="Date Published")
    pages = fields.Integer(string="Number of Pages")
    type = fields.Many2one('typebook.book', string="Type of Book")


class Type(models.Model):
    _name = 'typebook.book'

    name = fields.Char(string="Type")