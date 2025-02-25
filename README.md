# Factoria F5 - Django CRUD App

Una aplicación **Django CRUD** que permite a los usuarios gestionar modelos de IA.
Cada modelo de IA recibe automáticamente un **autor aleatorio** obtenido de [randomuser.me](https://randomuser.me/api/).

---

## Características
- ✅ **Operaciones CRUD** (Crear, Leer, Actualizar, Eliminar) para modelos de IA.
- ✅ **Asignación automática de autor** desde la API `randomuser.me`.
- ✅ **Interfaz de administración** para gestionar modelos de IA.
- ✅ **CI/CD con GitHub Actions** para pruebas automatizadas.

---

## 🛠️ Instalación

### **1️⃣ Clonar el Repositorio**
```bash
 git clone https://github.com/peoplenarthax/f5-sdlc-workshop.git
 cd f5-sdlc-workshop
```

### ** Optional: Virtual Environmennt **
```bash
python3 -m venv env
source env/bin/activate
pip install django
pip install requests
```

### **2️⃣ Instalar Dependencias**
```bash
pip install -r requirements.txt
```
---

## 🚀 Ejecutar la Aplicación

### **1️⃣ Aplicar Migraciones**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **2️⃣ Crear un Superusuario (Acceso al Panel de Administración)**
```bash
python manage.py createsuperuser
```
Sigue las instrucciones para configurar un **nombre de usuario y contraseña de administrador**.

### **3️⃣ Iniciar el Servidor de Desarrollo**
```bash
python manage.py runserver
```
Luego, abre:
- **http://127.0.0.1:8000/** → Página principal de la aplicación
- **http://127.0.0.1:8000/admin/** → Panel de Administración de Django (Iniciar sesión con credenciales de superusuario)

---

## 📌 API Endpoints

### **Obtener todos los modelos de IA**
**GET** `/api/models/`
```json
[
    {
        "id": 1,
        "name": "GPT-4",
        "description": "Modelo de IA avanzado",
        "author": "Juan Pérez",
        "created_at": "2024-02-16T12:00:00Z"
    }
]
```

### **Crear un nuevo modelo de IA**
**POST** `/api/models/`
#### **Cuerpo de la solicitud:**
```json
{
    "name": "GPT-5",
    "description": "Siguiente generación de IA"
}
```
#### **Respuesta esperada:**
```json
{
    "id": 2,
    "name": "GPT-5",
    "description": "Siguiente generación de IA",
    "author": "Carlos Rodríguez",
    "created_at": "2024-02-16T12:05:00Z"
}
```

### **Actualizar un modelo de IA**
**PUT** `/api/models/{id}/`
#### **Cuerpo de la solicitud:**
```json
{
    "name": "GPT-5 Mejorado",
    "description": "Versión mejorada del GPT-5"
}
```

### **Eliminar un modelo de IA**
**DELETE** `/api/models/{id}/`
#### **Respuesta esperada:**
```json
{
    "message": "Modelo eliminado exitosamente"
}
```

