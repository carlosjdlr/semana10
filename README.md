# 🏥 ClínicaSalud – Sistema de Citas Médicas

Aplicación web desarrollada con **Python + Flask** como proyecto del curso de desarrollo web.  
**Actualizado para Semana 10** con plantillas dinámicas usando Jinja2.

## 📋 Descripción

ClínicaSalud es un sistema de gestión de citas médicas que permite a los pacientes:
- Consultar especialidades médicas disponibles
- Ver el equipo de médicos especialistas
- Revisar horarios de atención
- Conocer servicios adicionales (laboratorio, radiología, farmacia, etc.)
- Contactar con la clínica
- Agendar citas ingresando su nombre

---

## 🆕 Novedades Semana 10

✅ **Plantillas con herencia** – Todas las páginas extienden de `base.html`  
✅ **4 nuevas rutas** relacionadas al sistema médico:
- `/medicos` – Lista de médicos especialistas
- `/horarios` – Horarios de atención general y por especialidad
- `/servicios` – Servicios adicionales (laboratorio, farmacia, etc.)
- `/contacto` – Información de contacto y formulario

✅ **Navegación mejorada** – Menú actualizado con todas las secciones  
✅ **Separación de estructura y contenido** – Uso efectivo de bloques Jinja2

---

## 🗂️ Estructura del Proyecto

```
semana9-main/                  (o proyecto_clinicasalud)
├── app.py                     # Aplicación Flask con 9 rutas
├── requirements.txt           # Dependencias (Flask + Gunicorn)
├── .gitignore                 # Archivos excluidos del repo
├── README.md                  # Este archivo
├── static/
│   ├── css/
│   │   └── style.css          # Estilos personalizados
│   └── js/
│       └── main.js            # JavaScript del frontend
└── templates/
    ├── base.html              # ⭐ Plantilla base (herencia)
    ├── index.html             # Página principal
    ├── acerca.html            # Acerca de la clínica
    ├── cita.html              # Ruta dinámica: cita por paciente
    ├── especialidad.html      # Ruta dinámica: especialidad médica
    ├── medicos.html           # 🆕 Lista de médicos
    ├── horarios.html          # 🆕 Horarios de atención
    ├── servicios.html         # 🆕 Servicios adicionales
    └── contacto.html          # 🆕 Página de contacto
```

---

## 🔗 Rutas Disponibles

### Rutas Estáticas
| Ruta | Descripción |
|------|-------------|
| `/` | Página principal – especialidades médicas |
| `/acerca` | Información sobre ClínicaSalud |
| `/medicos` | 🆕 Lista de médicos especialistas |
| `/horarios` | 🆕 Horarios de atención |
| `/servicios` | 🆕 Servicios adicionales |
| `/contacto` | 🆕 Información de contacto |

### Rutas Dinámicas
| Ruta | Ejemplo | Descripción |
|------|---------|-------------|
| `/cita/<paciente>` | `/cita/Ana` | "Hola, Ana. Tu cita está en proceso." |
| `/especialidad/<nombre>` | `/especialidad/cardiologia` | Detalle de la especialidad |

---

## 🚀 Instalación y Ejecución Local

### 1. Clonar el repositorio
```bash
git clone https://github.com/TU_USUARIO/proyecto_clinicasalud.git
cd proyecto_clinicasalud
```

### 2. Crear y activar el entorno virtual
```bash
# Crear entorno virtual
python -m venv venv

# Activar en Windows
.\venv\Scripts\activate

# Activar en macOS/Linux
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
```bash
python app.py
```

Abre tu navegador en: **http://127.0.0.1:5000**

---

## ☁️ Despliegue en Render

### Pasos para desplegar:
1. Subir el proyecto a GitHub
2. Ir a [render.com](https://render.com) y crear cuenta
3. Crear un nuevo **Web Service** conectado al repositorio
4. Configurar:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Python Version:** 3.11
5. Hacer clic en **Deploy** 🚀

> ℹ️ `gunicorn` ya está incluido en `requirements.txt`

Si ya tenías el proyecto desplegado, Render lo actualizará automáticamente al hacer `git push`.

---

## 🔄 Actualizar el Repositorio de GitHub

Si ya tenías el proyecto en GitHub de la Semana 9, actualízalo con los nuevos cambios:

```bash
# Agregar los cambios
git add .

# Confirmar los cambios
git commit -m "Semana 10: Agregar plantillas con herencia y nuevas rutas"

# Subir a GitHub
git push origin main
```

Render detectará el cambio automáticamente y redesplegará la aplicación.

---

## 🛠️ Tecnologías

- **Backend:** Python 3.11 · Flask 3.1
- **Frontend:** HTML5 · CSS3 · JavaScript
- **Plantillas:** Jinja2 (herencia con `{% extends %}` y `{% block %}`)
- **Tipografía:** DM Serif Display · DM Sans (Google Fonts)
- **Control de versiones:** Git · GitHub
- **Despliegue:** Render

---

## 📚 Conceptos de Jinja2 Aplicados

✅ **Herencia de plantillas** – `{% extends "base.html" %}`  
✅ **Bloques de contenido** – `{% block content %}{% endblock %}`  
✅ **Variables** – `{{ variable }}`  
✅ **Bucles** – `{% for item in lista %}...{% endfor %}`  
✅ **Condicionales** – `{% if condicion %}...{% endif %}`  
✅ **Filtros** – `{{ texto | capitalize }}`, `{{ texto | lower }}`  
✅ **Funciones de Flask** – `{{ url_for('static', filename='css/style.css') }}`

---

## 📌 Próximas Mejoras (Fases Futuras)

- [ ] Conexión a base de datos MySQL (Aiven/Railway)
- [ ] Formularios funcionales con POST
- [ ] Panel de administración para médicos
- [ ] Autenticación de usuarios (pacientes y doctores)
- [ ] Notificaciones por correo electrónico
- [ ] Sistema de reservas con calendario

---

## 👨‍💻 Autor

Proyecto desarrollado como parte del curso de **Desarrollo Web con Flask**.  
**Semana 10:** Implementación de plantillas dinámicas con Jinja2.
