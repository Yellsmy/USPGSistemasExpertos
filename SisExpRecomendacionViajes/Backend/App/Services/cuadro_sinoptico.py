import matplotlib.pyplot as plt

# Crear figura y ejes
fig, ax = plt.subplots(figsize=(16, 14))

# Datos para el cuadro sinóptico
textos = {
    "Bienestar Laboral": {
        "Programas de Salud Ocupacional": {
            "Efectos": [
                "Reducción del ausentismo",
                "Mejora en seguridad laboral",
                "Incremento en satisfacción"
            ],
            "Aplicación en la SAT": ["Jornadas de chequeos médicos y asesorías nutricionales"]
        },
        "Flexibilidad Laboral": {
            "Efectos": [
                "Mayor productividad",
                "Retención de talento",
                "Mejora del equilibrio trabajo-vida"
            ],
            "Aplicación en la SAT": ["Implementar esquemas híbridos para desarrolladores"]
        },
        "Programas de Capacitación y Desarrollo": {
            "Efectos": [
                "Incremento en habilidades técnicas",
                "Mayor compromiso del equipo",
                "Reducción de rotación de personal"
            ],
            "Aplicación en la SAT": ["Certificaciones en tecnologías emergentes"]
        },
        "Reconocimiento Laboral": {
            "Efectos": [
                "Mejora en clima organizacional",
                "Incremento en motivación",
                "Fortalecimiento del sentido de pertenencia"
            ],
            "Aplicación en la SAT": ["Premios mensuales al desempeño destacado"]
        },
        "Espacios de Recreación": {
            "Efectos": [
                "Reducción del estrés",
                "Mejora en relaciones laborales",
                "Aumento del compromiso"
            ],
            "Aplicación en la SAT": ["Salas de descanso y actividades recreativas"]
        }
    }
}

# Ajustes en posiciones iniciales
x_start = 0.05
y_start = 0.95
line_space = 0.12  # Incremento del espacio entre líneas

# Función recursiva para dibujar texto y llaves
def dibujar_cuadro(ax, x, y, datos, nivel=0, offset=0):
    if isinstance(datos, dict):
        for i, (clave, valor) in enumerate(datos.items()):
            current_y = y - (offset + i) * line_space
            ax.text(x + nivel * 0.2, current_y, clave, fontsize=10, va="center", ha="left")
            if isinstance(valor, (dict, list)):
                ax.plot(
                    [x + nivel * 0.18, x + nivel * 0.2],
                    [current_y, current_y - line_space * len(valor) * 0.5],
                    'k-'
                )
            offset = dibujar_cuadro(ax, x, current_y, valor, nivel + 1, offset + i + 1)
    elif isinstance(datos, list):
        for j, item in enumerate(datos):
            current_y = y - (offset + j) * line_space
            ax.text(x + nivel * 0.2, current_y, f"- {item}", fontsize=9, va="center", ha="left")
        offset += len(datos)
    return offset

# Dibujar el cuadro sinóptico
dibujar_cuadro(ax, x_start, y_start, textos)

# Configuración del gráfico
ax.axis("off")
plt.title("Cuadro Sinóptico: Bienestar Laboral", fontsize=16, pad=20)
plt.tight_layout()

# Mostrar el cuadro sinóptico
plt.show()
