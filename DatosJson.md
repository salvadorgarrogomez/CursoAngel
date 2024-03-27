{
    // Use IntelliSense para saber los atributos posibles.
    // Mantenga el puntero para ver las descripciones de los existentes atributos.
    // Para más información, visite: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [

        {
            "name": "Depurador de Python: Archivo actual",
            "type": "debugpy",
            "request": "launch",
            "program": "/home/odoo/odoo/odoo-bin",
            "args": [
                "-c/home/odoo/odoo.conf",
                "--update=helpdesk_salva",
                "--database=FCT"
            ],
            "console": "integratedTerminal",
            "justMyCode": true,
        }
    ]
}


## Datos de ejemplo, para dar funcion al Json para lanzar el servicio desde VSC