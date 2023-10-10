{
    'name':"Saldo  App",
    'description':"Aplicaicon web para registrar ingresos y egresos",
    'author':"Robinson Gutierrez",
    'version':"1.1",
    #se importa mail para que pueda ocupar el atributo
    'depends':["base","mail"],
    'data':[
        "views/views.xml",
        "security/ir_model_access.xml"
    ]
}