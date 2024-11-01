class SistemaCausal:
    def __init__(self):
        self.eventos = []

    def activar_evento(self, evento):
        """Activa un evento y registra sus efectos."""
        print(f"Evento activado: {evento}")
        self.eventos.append(evento)
        self.evaluar_causas(evento)

    def evaluar_causas(self, evento):
        """Evalúa las causas en función del evento activado."""
        if evento == "Lluvia":
            self.activar_evento("Activación de sistema de drenaje")
        elif evento == "Nieve":
            self.activar_evento("Activación de calefacción")
        elif evento == "Lluvia" and "Temperatura baja" in self.eventos:
            self.activar_evento("Nieve")

# Ejemplo de uso
sistema = SistemaCausal()
sistema.activar_evento("Lluvia")
sistema.activar_evento("Temperatura baja")
