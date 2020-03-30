En el api_djoser se utiliza la biblioteca djoser para utilizar el register y actualizaciones(PUT)
con el usuario y su tabla relacionada.

Además se encuentra el login donde obtiene token y logout para borrar el token utilizado.

Se registra como usuario para ingresar, pero luego se pasa a actualizar la información a la tabla que pertenece.

En rutas.txt se encuentran las rutas ha seguir para conseguir el username, login, token, actualizar información,
ver a los usuarios en la tabla y logout.


SOBRE LAS TABLAS QUE SE ENCUENTRAN SOBRE PASEADOR, MASCOTA O CLIENTE TIENEN TODOS LOS METODOS DEL CRUD.

Para mayor información sobre Djoser, ingresar a https://pypi.org/project/djoser/

Hay un ejemplo detallado con Json Web Token en la dirección 
https://dev.to/lewiskori/user-registration-and-authorization-on-a-django-api-with-djoser-and-json-web-tokens-4kc7
