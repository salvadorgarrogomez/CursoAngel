{
# name: nombre
# summary: descripción
# version: versión
# author: autor
# installable: si es instalable
# aplication: si es una aplicación
# depends: si depende de otros módulos
# data: ficheros xml y csv para vistas, datos, permisos…

    'name':'Sales - Helpdesk de Salva Garro',
    'summary':'Manage helpdesk de ticket',
    'version':'16.0.1.0.0',
    'author':'Salva Garro',
    'depends':[
        'sale', 
        'helpdesk_salva'
               ],
    'license':'AGPL-3',
    'data':[
        'views/sale_order_views.xml',
        'views/product_templates_views.xml',
            ],

}