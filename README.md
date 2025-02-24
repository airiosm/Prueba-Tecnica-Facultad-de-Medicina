# **📌 Documentación del Proyecto**

## **1️⃣ Introducción**
Este proyecto es un sistema de agendamiento de clases basado en microservicios, desarrollado con Vue.js, PHP, Flask y MySQL. Está completamente contenedorizado con Docker para facilitar su despliegue.

---

## **2️⃣ Arquitectura del Sistema**
El sistema sigue una arquitectura basada en microservicios:

```
📦 Proyecto
 ├── 📂 frontend (Vue.js - Interfaz de usuario)
 ├── 📂 backend-php (PHP - Gestión de cursos)
 ├── 📂 backend-python (Flask - Validación de matrículas)
 ├── 📂 database (MySQL - Almacenamiento de datos)
 ├── 📂 docker (Docker Compose - Orquestación de contenedores)
```

**Servicios principales:**
- **Frontend:** Desarrollado en Vue.js para la interfaz de usuario.
- **Backend PHP:** Maneja los cursos disponibles.
- **Backend Flask:** Valida y registra las matrículas, asegurando que no haya conflictos de horario.
- **Base de Datos MySQL:** Almacena la información de cursos y matrículas.
- **Docker Compose:** Orquesta todos los servicios para una configuración sencilla.

---

## **3️⃣ Decisiones de Diseño**
- **Uso de Docker:** Facilita la configuración del entorno sin necesidad de instalar dependencias manualmente.
- **Separación en Microservicios:** PHP y Flask manejan distintas responsabilidades para mayor escalabilidad.
- **Uso de MySQL:** Base de datos relacional ideal para almacenar cursos y registros de matrículas.

---

## **4️⃣ Instrucciones para Levantar el Proyecto**
Sigue estos pasos para ejecutar el sistema en tu computadora:

### 🔹 Paso 1: Instalar Docker y Docker Compose
Asegúrate de tener Docker instalado. Si no lo tienes, descárgalo desde:
[https://www.docker.com/get-started](https://www.docker.com/get-started)

Para verificar que está instalado, ejecuta en la terminal:
```sh
docker --version
docker-compose --version
```

### 🔹 Paso 2: Clonar el Repositorio
Clona este repositorio y entra en la carpeta del proyecto:
```sh
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

### 🔹 Paso 3: Levantar los Contenedores
Ejecuta el siguiente comando:
```sh
docker-compose up --build -d
```
Esto hará que el backend, frontend y base de datos se inicien automáticamente.

### 🔹 Paso 4: Verificar que Todo Funciona
Abre en tu navegador:
- **Frontend (si está configurado):** `http://localhost`
- **Backend PHP:** `http://localhost:8000/api.php`
- **Backend Flask:** Prueba con:
  ```sh
  curl -X POST http://localhost:5000/confirmar_matricula \
       -H "Content-Type: application/json" \
       -d '{"cursos_seleccionados": ["123", "543"]}'
  ```
- **phpMyAdmin (para ver la base de datos):** `http://localhost:8081`

### 🔹 Paso 5: Detener los Contenedores
Cuando termines de trabajar, apaga todo con:
```sh
docker-compose down
```
Si quieres borrar los datos almacenados, usa:
```sh
docker-compose down -v
```

---

## **5️⃣ Endpoints de las APIs**
### **Backend PHP - Gestión de Cursos**
| Método | Endpoint          | Descripción                     |
|--------|------------------|---------------------------------|
| GET    | `/api.php`       | Obtener todos los cursos.       |

### **Backend Flask - Validación de Matrículas**
| Método | Endpoint                      | Descripción                          |
|--------|--------------------------------|--------------------------------------|
| POST   | `/confirmar_matricula`        | Valida y registra una matrícula.    |

Ejemplo de uso:
```sh
curl -X POST http://localhost:5000/confirmar_matricula \
     -H "Content-Type: application/json" \
     -d '{"cursos_seleccionados": ["123", "543"]}'
```quina local:

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
