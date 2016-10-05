
# ENUM Pokemon Modifiers
SHINY = 1
METALLIC = 2
SHADOW = 4
DARK = 8
MYSTIC = 16

class Pokemon:
    def __init__(self, type_, level, mod = 0):
        self.type = type_
        self.level = level
        self.mod = mod
    
    def has_mod(self, mod):
        return bool(self.mod | mod)
