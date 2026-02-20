from flask import Flask, render_template

app = Flask(__name__)

# ──────────────────────────────────────────────
# Ruta principal
# ──────────────────────────────────────────────
@app.route('/')
def index():
    especialidades = [
        {"nombre": "Cardiología",    "icono": "❤️",  "descripcion": "Diagnóstico y tratamiento del corazón."},
        {"nombre": "Neurología",     "icono": "🧠",  "descripcion": "Trastornos del sistema nervioso."},
        {"nombre": "Pediatría",      "icono": "👶",  "descripcion": "Atención médica para niños y adolescentes."},
        {"nombre": "Traumatología",  "icono": "🦴",  "descripcion": "Lesiones y enfermedades del sistema óseo."},
        {"nombre": "Dermatología",   "icono": "🩺",  "descripcion": "Diagnóstico de enfermedades de la piel."},
        {"nombre": "Oftalmología",   "icono": "👁️",  "descripcion": "Salud visual y enfermedades del ojo."},
    ]
    return render_template('index.html', especialidades=especialidades)

# ──────────────────────────────────────────────
# Ruta dinámica: detalle de cita por paciente
# ──────────────────────────────────────────────
@app.route('/cita/<paciente>')
def cita(paciente):
    return render_template('cita.html', paciente=paciente.capitalize())

# ──────────────────────────────────────────────
# Ruta dinámica: especialidad médica
# ──────────────────────────────────────────────
@app.route('/especialidad/<nombre>')
def especialidad(nombre):
    info = {
        "cardiologia":   {"titulo": "Cardiología",   "icono": "❤️",  "descripcion": "Especialidad médica que se ocupa de las afecciones del corazón y del aparato circulatorio.", "horario": "Lunes a Viernes 8:00 – 18:00"},
        "neurologia":    {"titulo": "Neurología",    "icono": "🧠",  "descripcion": "Rama de la medicina que estudia los trastornos del sistema nervioso central y periférico.",    "horario": "Lunes a Jueves 9:00 – 17:00"},
        "pediatria":     {"titulo": "Pediatría",     "icono": "👶",  "descripcion": "Especialidad médica dedicada a la atención de la salud de niños y adolescentes.",             "horario": "Lunes a Sábado 8:00 – 14:00"},
        "traumatologia": {"titulo": "Traumatología", "icono": "🦴",  "descripcion": "Especialidad que trata lesiones y enfermedades del sistema músculo-esquelético.",             "horario": "Martes a Viernes 8:00 – 16:00"},
        "dermatologia":  {"titulo": "Dermatología",  "icono": "🩺",  "descripcion": "Especialidad médica enfocada en el diagnóstico de enfermedades de la piel.",                  "horario": "Lunes, Miércoles y Viernes 10:00 – 18:00"},
        "oftalmologia":  {"titulo": "Oftalmología",  "icono": "👁️",  "descripcion": "Especialidad médica que trata las enfermedades y trastornos del ojo.",                        "horario": "Martes a Sábado 9:00 – 15:00"},
    }
    key = nombre.lower().replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    datos = info.get(key, {"titulo": nombre.capitalize(), "icono": "🏥", "descripcion": "Especialidad disponible en nuestra clínica.", "horario": "Consultar en recepción"})
    return render_template('especialidad.html', datos=datos)

# ──────────────────────────────────────────────
# Ruta: Acerca de
# ──────────────────────────────────────────────
@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

# ──────────────────────────────────────────────
# NUEVAS RUTAS - SEMANA 10
# ──────────────────────────────────────────────

# Ruta: Lista de Médicos
@app.route('/medicos')
def medicos():
    doctores = [
        {
            "nombre": "Dr. Carlos Mendoza",
            "especialidad": "Cardiología",
            "experiencia": "15 años",
            "educacion": "Universidad Nacional · Maestría en Cardiología Clínica",
            "icono": "❤️"
        },
        {
            "nombre": "Dra. Ana Torres",
            "especialidad": "Neurología",
            "experiencia": "12 años",
            "educacion": "Universidad de los Andes · Especialización en Neurología",
            "icono": "🧠"
        },
        {
            "nombre": "Dr. Luis Ramírez",
            "especialidad": "Pediatría",
            "experiencia": "10 años",
            "educacion": "Universidad Central · Postgrado en Pediatría Integral",
            "icono": "👶"
        },
        {
            "nombre": "Dra. María González",
            "especialidad": "Dermatología",
            "experiencia": "8 años",
            "educacion": "Universidad Javeriana · Dermatología Cosmética",
            "icono": "🩺"
        },
        {
            "nombre": "Dr. Jorge Castro",
            "especialidad": "Traumatología",
            "experiencia": "18 años",
            "educacion": "Universidad del Rosario · Cirugía Ortopédica",
            "icono": "🦴"
        },
        {
            "nombre": "Dra. Patricia Rojas",
            "especialidad": "Oftalmología",
            "experiencia": "14 años",
            "educacion": "Universidad Nacional · Cirugía Láser Ocular",
            "icono": "👁️"
        }
    ]
    return render_template('medicos.html', doctores=doctores)

# Ruta: Horarios de Atención
@app.route('/horarios')
def horarios():
    horarios_data = {
        "clinica": {
            "lunes_viernes": "7:00 AM - 8:00 PM",
            "sabados": "8:00 AM - 2:00 PM",
            "domingos": "Cerrado",
            "urgencias": "24/7"
        },
        "especialidades": [
            {"nombre": "Cardiología", "horario": "Lunes a Viernes 8:00 – 18:00"},
            {"nombre": "Neurología", "horario": "Lunes a Jueves 9:00 – 17:00"},
            {"nombre": "Pediatría", "horario": "Lunes a Sábado 8:00 – 14:00"},
            {"nombre": "Traumatología", "horario": "Martes a Viernes 8:00 – 16:00"},
            {"nombre": "Dermatología", "horario": "Lunes, Miércoles y Viernes 10:00 – 18:00"},
            {"nombre": "Oftalmología", "horario": "Martes a Sábado 9:00 – 15:00"}
        ]
    }
    return render_template('horarios.html', horarios=horarios_data)

# Ruta: Servicios Adicionales
@app.route('/servicios')
def servicios():
    servicios_list = [
        {
            "titulo": "Laboratorio Clínico",
            "icono": "🔬",
            "descripcion": "Análisis de sangre, orina, heces y estudios especializados con resultados en 24 horas.",
            "incluye": ["Hemograma completo", "Perfil lipídico", "Glucosa", "Análisis de orina"]
        },
        {
            "titulo": "Radiología e Imágenes",
            "icono": "📷",
            "descripcion": "Rayos X, ecografías, tomografías y resonancias magnéticas con equipo de última generación.",
            "incluye": ["Rayos X digital", "Ecografía 4D", "Tomografía", "Resonancia magnética"]
        },
        {
            "titulo": "Farmacia 24 Horas",
            "icono": "💊",
            "descripcion": "Medicamentos genéricos y de marca disponibles las 24 horas del día.",
            "incluye": ["Entrega inmediata", "Medicamentos recetados", "Genéricos", "Productos de cuidado"]
        },
        {
            "titulo": "Servicio de Urgencias",
            "icono": "🚑",
            "descripcion": "Atención médica de emergencia disponible todos los días del año, las 24 horas.",
            "incluye": ["Atención inmediata", "Ambulancia", "Sala de observación", "Médicos especializados"]
        },
        {
            "titulo": "Vacunación",
            "icono": "💉",
            "descripcion": "Esquemas de vacunación para niños, adultos y viajeros internacionales.",
            "incluye": ["Vacunas infantiles", "Vacunas para adultos", "Certificados internacionales", "Asesoría médica"]
        },
        {
            "titulo": "Telemedicina",
            "icono": "💻",
            "descripcion": "Consultas médicas virtuales desde la comodidad de tu hogar.",
            "incluye": ["Consulta en línea", "Recetas digitales", "Seguimiento", "Historial médico digital"]
        }
    ]
    return render_template('servicios.html', servicios=servicios_list)

# Ruta: Contacto
@app.route('/contacto')
def contacto():
    datos_contacto = {
        "direccion": "Calle Principal #45-67, Sector Centro",
        "telefono": "+593 (02) 234-5678",
        "whatsapp": "+593 98 765 4321",
        "email": "contacto@clinicasalud.com",
        "horario_atencion": "Lunes a Viernes: 7:00 AM - 8:00 PM | Sábados: 8:00 AM - 2:00 PM"
    }
    return render_template('contacto.html', contacto=datos_contacto)

# ──────────────────────────────────────────────
if __name__ == '__main__':
    app.run(debug=True)
