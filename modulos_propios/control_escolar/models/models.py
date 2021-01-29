# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Alumnos(models.Model):
    _name = 'control_escolar.alumnos'
    _description = 'Alumnos del control escolar'

    nombre = fields.Char(string='Nombre del Alumno')  # etiqueta que nos va a mostrar luego en las vistas
    apellido_paterno = fields.Char(string='Apellido Paterno')  # si no ponemos el string=, nos pondría el nombre del campo
    apellido_materno = fields.Char(string='Apellido Materno')
    sexo = fields.Selection([('Masculino', 'Masculino'), ('Femenino', 'Femenino')])
    edad = fields.Integer(string='Edad')
