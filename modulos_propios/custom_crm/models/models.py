# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
import datetime


class Visit(models.Model):
    _name = 'custom_crm.visit'  # sigue un estandar que es nombre del módulo . nombre del modelo
    _description = 'Visit'

    name = fields.Char(string='Descripción')  # etiqueta que nos va a mostrar luego en las vistas (Las vistas muestran nombre vista / atributo name del modelo. Luego en el menú, cuando abramos a cada cliente nos pondrá la descripción junto al nombre del menú
    # customer = fields.Char(string='Cliente', required=True)  #si no ponemos el string=, nos pondría el nombre del campo

    # Vamos a modelarlo ahora con relación: Varias visitas comerciales pueden estar asociadas a un cliente
    customer = fields.Many2one(string='Cliente',
                               comodel_name='res.partner')  # comodel_name es el modelo al que hace referencia  (los clientes se almacenan en la tabla res.partner)
    customer_description = fields.Char(string='Descripción Cliente', readonly=True)
    date = fields.Datetime(string="Fecha")
    type = fields.Selection([('P', 'Presencial'), ('W', 'WhatsApp'), ('T', 'Telefónico')], string='Tipo', required=True)  # tipo de visita
    done = fields.Boolean(string='Realizada', readonly=True)
    image_client = fields.Binary(string='Imagen Cliente')

    # creamos la función que cambiará el valor de done a través del botón. Al pulsar el boton definido en la vista "toggle_state" cambiará el estado

    def toggle_state(self):
        self.done = not self.done

    def action_test(self):
        raise ValidationError("Hola Mundo")  # Esto para la aplicación, es un brake.

    # vamos a crear una accion que modifique un campo

    def action_cambiarName(self):
        if self.customer.name_get():
            customer_name = self.customer.name_get()[0]  # Extraemos el nombre del campo Many2one
            nombre_cliente = str(customer_name[1])
            if self.name:
                self.customer_description = 'Cliente: ' + nombre_cliente + ' - Descripción: ' + self.name
            # if self.name:
                  # self.name = 'Cliente: ' + nombre_cliente + ' - Descripción: ' + self.name

    # definimos la función para crear entidades. Creamos un JSON
    def funcion_crear(self):
        json_visit = {
            'name': 'ORM test',
            'customer': 1,
            'date': str(datetime.date(2021, 8, 6)),
            'type': 'P',
            'done': False
        }
        print(json_visit)
        self.env['custom_crm.visit'].create(json_visit)

    # hacemos la búsqueda del modelo y luego hacemos el update -> tenemos dos métodos para buscar el search (pasamos array de tuplas que nos permiten acotar el resultado)
    # y el browse (pasams el array de identificadores en la bd.
    # Utilizando write y un JSON guardamos el modelo en la bd
    def funcion_search_update(self):
        visit_search = self.env['custom_crm.visit'].search([('name', '=', 'ORM test')])
        buscado = visit_search.id
        print('search()', buscado, visit_search.name)

        visit_browse = self.env['custom_crm.visit'].browse([buscado])  #sabemos que el id en la bd del ORM test es el 3
        print('browse()', visit_browse, visit_browse.name)

        visit_search.write({
            'name': 'ORM test write'
        })

    def funcion_delete(self):
        visit_search = self.env['custom_crm.visit'].search([('name', '=', 'ORM test')])
        if visit_search:
            visit_search.unlink() #elimina de la bd
        else:
            raise ValidationError("No se encuentra registro 'ORM test'")