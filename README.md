# gestor

## Project setup
```
# **Instrucciones para Levantar el Proyecto 🚀**

Este proyecto utiliza `Docker` y `docker-compose` para facilitar la configuración del entorno de desarrollo. Sigue estos pasos para ejecutar el sistema correctamente.  

## **1️⃣ Requisitos Previos**
Antes de comenzar, asegúrate de tener instalados en tu sistema:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

Para verificar la instalación, ejecuta en la terminal:

```sh
docker --version
docker-compose --version
```

---

## **2️⃣ Clonar el Repositorio**
Clona este repositorio en tu máquina local:

```sh
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

---

## **3️⃣ Configurar Variables de Entorno**
Dentro del proyecto, crea un archivo `.env` en la raíz y define las credenciales para la base de datos:

```sh
MYSQL_ROOT_PASSWORD=root
MYSQL_USER=user
MYSQL_PASSWORD=password
MYSQL_DATABASE=gestor_db
```

---

## **4️⃣ Construir y Levantar los Contenedores**
Ejecuta el siguiente comando en la terminal dentro del proyecto:

```sh
docker-compose up --build -d
```

Esto hará lo siguiente:
✅ Construirá la imagen de PHP y Flask.
✅ Iniciará los contenedores de MySQL, PHP y phpMyAdmin.
✅ Expondrá los puertos necesarios para acceder a los servicios.

---

## **5️⃣ Verificar que Todo Funciona**
Para comprobar que los servicios están corriendo correctamente:

### **📌 Backend PHP**
Abre en tu navegador:
[http://localhost:8000/api.php](http://localhost:8000/api.php)

Si la configuración es correcta, verás los datos de la base de datos en formato JSON.

### **📌 Backend Flask**
Puedes probar el servicio de matrícula con:

```sh
curl -X POST http://localhost:5000/confirmar_matricula -H "Content-Type: application/json" -d '{"cursos_seleccionados": ["123", "543"]}'
```

### **📌 phpMyAdmin**
Para acceder a la base de datos visualmente, ve a:
[http://localhost:8081](http://localhost:8081)
Usuario: `root`
Contraseña: `root`

---

## **6️⃣ Detener los Contenedores**
Cuando termines de trabajar, puedes detener los servicios con:

```sh
docker-compose down
```

Si deseas eliminar los volúmenes y datos almacenados, usa:

```sh
docker-compose down -v
```

---

## **7️⃣ Notas Adicionales**
- Si realizas cambios en el código y necesitas reconstruir las imágenes, ejecuta:
  ```sh
  docker-compose up --build -d
  ```
- Si quieres ver los logs de los contenedores:
  ```sh
  docker-compose logs -f
  ```
- Puedes acceder al contenedor de PHP con:
  ```sh
  docker exec -it gestor-php bash
  ```
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
