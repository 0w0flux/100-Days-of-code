import colorgram

def cgram():
    colors = colorgram.extract(r"C:\\Users\\oweca\\Documents\\VS Code Workspace\\GitHub\\Learning\\01Python\\100 days of code\\Day 18 (turtle graphics)\\cody.jpg", 10)

    # colorgram.extract returns Color objects, which let you access
    # RGB, HSL, and what proportion of the image was that color.
    first_color = colors[0]
    rgb = first_color.rgb # e.g. (255, 151, 210)
    hsl = first_color.hsl # e.g. (230, 255, 203)
    proportion  = first_color.proportion # e.g. 0.34

    # RGB and HSL are named tuples, so values can be accessed as properties.
    # These all work just as well:
    red = rgb[0]
    red = rgb.r
    saturation = hsl[1]
    saturation = hsl.s

    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    print(rgb_colors)

cgram()
