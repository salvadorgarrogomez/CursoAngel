{
# name: nombre
# summary: descripción
# version: versión
# author: autor
# installable: si es instalable
# aplication: si es una aplicación
# depends: si depende de otros módulos
# data: ficheros xml y csv para vistas, datos, permisos…

    'name':'Real State de Salva Garro',
    'summary':'Proyecto inicial',
    'version':'16.0.1.0.0',
    'author':'Salva Garro',
    'depends':['base',
               ],
    'license':'AGPL-3',
    'data':[
        'security/ir.model.access.csv',
        'views/estate_menus.xml',
        'views/estate_property_views.xml',
            ],
     'demo':[
            ],

}