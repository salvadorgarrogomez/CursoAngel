{
# name: nombre
# summary: descripción
# version: versión
# author: autor
# installable: si es instalable
# aplication: si es una aplicación
# depends: si depende de otros módulos
# data: ficheros xml y csv para vistas, datos, permisos…

    'name':'Project - Helpdesk de Salva Garro',
    'summary':'Manage helpdesk de ticket',
    'version':'16.0.1.0.0',
    'author':'Salva Garro',
    'depends':[
        'project',
               ],
    'license':'AGPL-3',
    'data':[
        'security/ir.model.access.csv',
#        'views/crm_ticket_views.xml',
        'views/project_ticket_views.xml',
            ],

}