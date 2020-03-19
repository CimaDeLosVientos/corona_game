class Scene:
    """Representa un escena abstracta del videojuego.
 
    Una escena es una parte visible del juego, como una pantalla
    de presentación o menú de opciones. Tiene que crear un objeto
    derivado de esta clase para crear una escena utilizable."""
 
    def __init__(self):
        self.next = None
   
    def load(self, data):
        "Se llama antes de empezar la ejecución para configurarla según los datos de la partida."
        raise NotImplemented("Tiene que implementar el método on_event.")


    def on_event(self, time, event):
        "Se llama cuando llega un evento especifico al bucle."
        raise NotImplemented("Tiene que implementar el método on_event.")
    

    def on_update(self, time):
        "Actualización lógica que se llama automáticamente desde el director."
        raise NotImplemented("Tiene que implementar el método on_update.")
 
 
    def on_draw(self, screen):
        "Se llama cuando se quiere dibujar la pantalla."
        raise NotImplemented("Tiene que implementar el método on_draw.")

    def finish(self):
        "Se llama cuando se quiere pasar a la siguiente escena."
        raise NotImplemented("Tiene que implementar el método on_draw.")
