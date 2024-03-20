{
# name: nombre
# summary: descripción
# version: versión
# author: autor
# installable: si es instalable
# aplication: si es una aplicación
# depends: si depende de otros módulos
# data: ficheros xml y csv para vistas, datos, permisos…

    'name':'Helpdesk de Salva Garro',
    'summary':'Manage helpdesk de ticket',
    'version':'16.0.1.0.0',
    'author':'Salva Garro',
    'depends':['base'
               ],
    'license':'AGPL-3',
    'data':[
     'security/helpdesk_security.xml',
     'security/ir.model.access.csv',
     'views/helpdesk_ticket_view.xml',
            ]

}