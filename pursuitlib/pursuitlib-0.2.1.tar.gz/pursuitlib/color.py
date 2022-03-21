
def hex_to_rgb(value):
    value = value.lstrip('#')
    val_len = len(value)
    return tuple(int(value[i:i + val_len // 3], 16) for i in range(0, val_len, val_len // 3))


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


def is_dark(color):
    if isinstance(color, str):
        color = hex_to_rgb(color)

    rgb = (color[0] / 255, color[1] / 255, color[2] / 255)
    lum = [rgb[i] for i in range(3)]

    for i in range(3):
        if lum[i] < 0.03928:
            lum[i] /= 12.92
        else: lum[i] = pow((lum[i] + 0.055) / 1.055, 2.4)

    return (0.2126 * lum[0] + 0.7152 * lum[1] + 0.0722 * lum[2]) <= 0.179
