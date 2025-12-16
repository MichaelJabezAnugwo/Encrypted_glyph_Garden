text_input = "I dream in encrypted color"

glyphs = []


def setup():
    size(800, 800)
    noStroke()
    textAlign(CENTER, CENTER)
    frameRate(60)

    # Convert text to ASCII values
    values = [ord(c) for c in text_input]

    # Pad to fill grid
    while len(values) < 64:
        values += values
    values = values[:64]

    # Create glyphs
    cols = 8
    rows = 8
    w = width / cols
    h = height / rows

    for i in range(rows):
        for j in range(cols):
            idx = i * cols + j
            val = values[idx]
            glyphs.append({
                "x": j * w + w / 2,
                "y": i * h + h / 2,
                "angle": radians(val % 360),
                "speed": radians((val % 10) + 1),
                "size": map(val, 32, 126, 10, 60),
                "color": color((val * 3) % 255, (val * 5) % 255, (val * 7) % 255, 180),
                "type": val % 3  # 0 = circle, 1 = arc, 2 = line
            })


def draw():
    background(10)

    for g in glyphs:
        pushMatrix()
        translate(g["x"], g["y"])
        rotate(g["angle"])
        fill(g["color"])

        t = g["type"]
        s = g["size"] + sin(frameCount * 0.05) * 5

        if t == 0:
            ellipse(0, 0, s, s)
        elif t == 1:
            arc(0, 0, s, s, 0, PI + QUARTER_PI)
        else:
            stroke(g["color"])
            strokeWeight(2)
            line(-s / 2, 0, s / 2, 0)
            noStroke()

        g["angle"] += g["speed"] * 0.01
        popMatrix()