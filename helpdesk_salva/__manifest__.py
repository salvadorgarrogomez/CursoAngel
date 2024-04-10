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
    'depends':['base',
               'mail',
               ],
    'license':'AGPL-3',
    'data':[
     'security/helpdesk_security.xml',
     'security/ir.model.access.csv',
     'views/helpdesk_menu_views.xml',
     'wizards/create_ticket_views.xml',
     'views/helpdesk_ticket_tags_views.xml',
     'views/helpdesk_ticket_views.xml',
     'views/helpdesk_ticket_actions_views.xml',
     'data/tag_cron.xml',
     'reports/tickets_reports_templates.xml',
     'reports/ticket_report.xml',
     'reports/partner_card_reports_templates.xml',
     'reports/partner_card_report.xml',
            ],
     'demo':[
         'demo/demo_helpdesk.xml',
            ],

}