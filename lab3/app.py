class Figure:
    def __init__(self, type, length):
        self.type = type
        self.length = length

    def get_figure_type(self):
        return self.type

    def get_figure_length(self):
        return self.length  

    @property
    def get_angles(self):
        if self.type in ["квадрат", "прямокутник"]:
            return 4
        if self.type == "трикутник":
            return 3
        return 0
    
