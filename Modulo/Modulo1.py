from odoo import models,fields

class Socio(models.Model):
    _name='Socio'
    numsocio=fields.Integer('Numero de socio')
    nombre=fields.Char('Nombre de socio')
    apellidos=fields.Char('Apellido de socio')
    preferente=fields.Boolean('Preferente?')
    direccion=fields.Char('Direccion')
    codpostal=fields.Integer('Codigo postal')
    poblacion=fields.Char('Poblacion socio')
    
class Autor(models.Model):
    _name='Autor'
    dni=fields.Char('DNI autor')   
    nombre=fields.Char('Nombre autor')
    apellidos=fields.Char('Apellidos autor')
    direccion=fields.Char('Direccion autor')

class Libros(models.Model):
    _name='Libros'
    codigo=fields.Integer('Codigo de libro')
    titulo=fields.Char('Titulo de libro')
    autor=fields.Char('Autor del libro')
    editorial=fields.Char('Editorial del libro')
    fechacompra=fields.Date('Fecha de compra') #?
    preciocompra=fields.Monetary('Precio de compra')
    categoria=fields.Selection([('intriga','intriga'),('drama','drama'),('infantil','infantil'),('aventuras','aventuras'),('historia','historia')],'Categoria')
    dniautor=fields.One2many('Autor','dni','DNI Autor') #IMPORTANTE

class Prestamos(models.Model):
    _name='Prestamos'
    codigo=fields.Integer('Codigo prestamo')
    fecha=fields.Datetime('Fecha y Hora del prestamo') 
    numsocio=fields.One2many('Socio','numsocio','Prestamo a socio')
    codigolibro=fields.One2many('Libros','codigo','Codigo libro prestamo')
    
    