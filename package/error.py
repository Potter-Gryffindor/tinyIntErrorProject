class TinyIntError(Exception):
    def __init__(self):
        self.message = "El valor debe ser entre 0 y 255"

    def __str__(self):
        return self.message