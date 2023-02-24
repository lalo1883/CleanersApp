README

Introducción

Este es un ejemplo de documentación para una aplicación que permite a los usuarios gestionar información sobre personal de limpieza. La aplicación está construida con FastAPI y está diseñada para ser fácil de usar e intuitiva.

Instalación

Para utilizar esta aplicación, primero deberá instalar las siguientes dependencias:

FastAPI
jwt_manager
Puede instalarlas con el siguiente comando:

Copy code
pip install fastapi jwt_manager
Uso

uvicorn main:app --reload


La aplicación ofrece una serie de endpoint que permiten al usuario realizar diferentes operaciones con los datos sobre el personal de limpieza. Estos endpoint incluyen:

/cleaners - Devuelve la información de todo el personal de limpieza.
/cleaners/{id} - Devuelve la información de un solo personal de limpieza específico.
/cleaners/ - Devuelve la información de los personal de limpieza específicos de una ciudad específica.
/cleaner/ - Permite crear una nueva entrada para un personal de limpieza.
/cleaner/{id} - Permite editar la información de un personal de limpieza existente.
/cleaner/{id} - Permite eliminar la información de un personal de limpieza existente.
Modelo de datos

El modelo de datos de la clase personal de limpieza incluye los siguientes atributos:

id - El identificador único para cada personal de limpieza.
name - El nombre completo del personal de limpieza.
age - La edad del personal de limpieza.
hourly_rate - La tarifa por hora del personal de limpieza.
city - La ciudad en la que reside el personal de limpieza.
Conclusion

Este es un ejemplo básico de cómo documentar una aplicación FastAPI. Esta aplicación es solo un ejemplo y puede ser personalizada y ampliada según las necesidades del usuario.