# -*- coding: utf-8 -*-
from odoo import models,fields

class ToDo(models.Model):
    _name = "todo.app" # el nombre en la bd se creara como todo_app
    _description = "Lista de Tareas"

    name = fields.Char(String="Nombre")
    description = fields.Char(String="Descripcions")
    state = fields.Char(String="Estado")
    #detalle = fields.Char(String="Estado")
    #price = fields.Char(String="Precio")
    #capacity = fields.Char(String="Capacidad")


    
