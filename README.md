# serv-correos-prueba2
Manejo de Api, status.HTTP, autenticacion, tokens

# ToDoList
Django versión 5, y usando djangorestframework.
Crear un proyecto en el que se generen 3 modelos:

1.- Modelo: Login
con sus campos: username, password
Para hacer el login en con autenticacion simple en django
2.- Modelo DataSystem:
con sus campos: name, uuid, email, password
3.- Modelo Notification:
con sus campos uuid( que es foreignkey del modelo DataSystem), title, email
Es necesario crear los siguiente en relación a los modelos anteriores:
- crear la configuración de djangorestframework y apps dentro de settings.py
- crear su archivo models.py
- crear su archivo serializers.py. Es importante decir que dentro de serializers es necesario validar para el serializer notification que el campo uuid proveniente del modelo Notification exista previamente en el modelo DataSystem
- crear su archivo urls.py tanto en settigs.py como en notification/urls.py
- crear su archivo views.py Es importante mencionar que en views.py se requiere trabajar con ApiView para crear nuestros métodos GET, PUT, DELETE y POST y manejar las respuestas HTTP a través de cada return Response("message", status)
