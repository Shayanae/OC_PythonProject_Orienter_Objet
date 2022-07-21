class ToolsBox:
    def __init__(self):
        self.tools = []

    def add_tool(self, tool):
        pass

    def remove_tool(self, tool):
        pass


class Screwdriver:
    def __init__(self, size):
        self.size = size

    def tighten(self, screw):
        """Serrer une vis."""
        pass

    def loosen(self, screw):
        """Dessrre une vis"""
        pass


class Hammer:
    def __init__(self, color = "red"):
        self.color = color

    def paint(self, color):
        pass

    def hammer_in(self, nial):
        """Enfonce un clou."""
        pass

    def remove(self, nail):
        """Enleve un clou."""
        pass


