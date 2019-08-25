""""
Intermediate Exercises
"""

COLORS = {"maroon": "#b03060", "medium": "#66cdaa", "LawnGreen": "#7cfc00", "khaki": "#f0e68c", "indianred": "#cd5c5c",
          "hotpink": "#ff69b4", "black": "#000000", "brown": "#a52a2a", "chocolate": "#d2691e"}

for color in COLORS:
    print("Name:{:10s} Code: {:8s}".format(color,COLORS[color]))

color_name = input("Enter Color name: ")

while color_name != "":
    color_name.lower()
    if color_name in COLORS:
        print(color_name, "code is ",COLORS[color_name])
    else:
        print("That's color name isn't store in DB!")
    color_name = input("Enter Color name: ")