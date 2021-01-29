# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class Visit(models.Model):
     _name = 'custom_crm.visit'   #sigue un estandar que es nombre del módulo . nombre del modelo
     _description = 'Visit'

     name = fields.Char(string='Descripción')   #etiqueta que nos va a mostrar luego en las vistas. Luego en el menú, cuando abramos a cada cliente nos pondrá la descripción junto al nombre del menú
     #customer = fields.Char(string='Cliente', required=True)  #si no ponemos el string=, nos pondría el nombre del campo

     # Vamos a modelarlo ahora con relación: Varias visitas comerciales pueden estar asociadas a un cliente
     customer = fields.Many2one (string='Cliente', comodel_name='res.partner') # comodel_name es el modelo al que hace referencia  (los clientes se almacenan en la tabla res.partner)
     date = fields.Datetime(string="Fecha")
     type = fields.Selection([('P','Presencial'),('W','WhatsApp'),('T','Telefónico')], string='Tipo', required=True)  #tipo de visita
     done = fields.Boolean(string='Realizada', readonly=True)


     #creamos la función que cambiará el valor de done a través del botón. Al pulsar el boton definido en la vista "toggle_state" cambiará el estado

     def toggle_state(self):
          self.done = not self.done


     def action_test(self):
          raise ValidationError("Hola Mundo")  #Esto para la aplicación, es un brake.

     # vamos a crear una accion que modifique un campo

     def action_cambiarName(self):
          if self.name:
               self.name = 'Descripción: ' + self.name





