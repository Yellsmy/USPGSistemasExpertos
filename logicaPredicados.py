class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.sintomas = []

    def agregarSintoma(self, sintoma):
        self.sintomas.append(sintoma)

class Diagnostico:
    def __init__(self):
        self.enfermedades = {}

    def agregarEnfermedad(self, enfermedad, sintomas):
        self.enfermedades[enfermedad] = set(sintomas)

    def diagnosticar(self, persona):
        posiblesEnfermedades = []
        for enfermedad, sintomas in self.enfermedades.items():
            if sintomas.issubset(set(persona.sintomas)):
                posiblesEnfermedades.append(enfermedad)
        return posiblesEnfermedades

if __name__ == "__main__":
    # Creación de personas
    juan = Persona("Juan")
    juan.agregarSintoma("fiebre")
    juan.agregarSintoma("dolor al tragar")

    maria = Persona("Maria")
    maria.agregarSintoma("dolor de cabeza")
    maria.agregarSintoma("nauseas")

    pedro = Persona("Pedro")
    pedro.agregarSintoma("fiebre")
    pedro.agregarSintoma("secrecion nasal")
    pedro.agregarSintoma("tos")

    # Creación del sistema de diagnóstico
    diagnostico = Diagnostico()

    # Agregando enfermedades y sus síntomas característicos
    diagnostico.agregarEnfermedad("Gripe", ["fiebre", "tos", "secrecion nasal"])
    diagnostico.agregarEnfermedad("Deshidratacion", ["dolor de cabeza", "nauseas"])
    diagnostico.agregarEnfermedad("infección de garganta", ["fiebre", "dolor al tragar"])

    # Diagnosticar personas
    print(f"Diagnóstico para Juan: {diagnostico.diagnosticar(juan)}")
    print(f"Diagnóstico para Maria: {diagnostico.diagnosticar(maria)}")
    print(f"Diagnóstico para Pedro: {diagnostico.diagnosticar(pedro)}")
