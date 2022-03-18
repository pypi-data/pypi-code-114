import enum
from typing import Tuple

USAGE = """\
i2w <x> <z>: convert coordinate in 8K radar image to the corresponding coordinate in 2b2t world
image2world <x> <z>: convert coordinate in 8K radar image to the corresponding coordinate in 2b2t world
w2i <x> <z>: convert coordinate in 2b2t world to the corresponding coordinate in 8K radar image
world2image <x> <z>: convert coordinate in 2b2t world to the corresponding coordinate in 8K radar image
q (or quit, exit): exit program
h (or help): show this help menu\
"""


class RadarImageType(enum.Enum):
    RADAR_4K = (3840, 2160, 8)
    RADAR_8K = (7680, 4320, 4)


def world_to_image(loc, image_type=RadarImageType.RADAR_8K) -> Tuple[int, int]:
    """
    Given a coordinate in 2b2t overworld, return the corresponding pixel coordinate in radar image.
    """
    x, z = loc
    off_x, off_z, chunks_per_pixel = image_type.value[0] // 2, image_type.value[1] // 2, image_type.value[2]
    return 3840 + x // 16 // chunks_per_pixel, 2160 + z // 16 // chunks_per_pixel


def image_to_world(loc, image_type=RadarImageType.RADAR_8K) -> Tuple[int, int]:
    """
    Given a position in radar image, return the center coordinate of the corresponding range in 2b2t overworld.
    """
    x, z = loc
    off_x, off_z, chunks_per_pixel = image_type.value[0] // 2, image_type.value[1] // 2, image_type.value[2]
    x, z = x - off_x, z - off_z
    return int((x + 0.5) * 16 * chunks_per_pixel), int((z + 0.5) * 16 * chunks_per_pixel)


def main():
    """ REPL """
    while True:
        try:
            inp = input('> ').strip().split(' ') or None
            cmd = inp[0] if len(inp) > 0 else None
            if cmd == 'i2w' or cmd == 'image2world':
                world_x, world_y = image_to_world((int(inp[1]), int(inp[2])))
                print(f'World: ({world_x}, {world_y})')
                print(f'Nether: ({world_x // 8}, {world_y // 8})')
            elif cmd == 'w2i' or cmd == 'world2image':
                print(world_to_image((int(inp[1]), int(inp[2]))))
            elif cmd == 'q' or cmd == 'quit' or cmd == 'exit':
                break
            elif cmd == 'h' or cmd == 'help':
                print(USAGE)
            elif not cmd:
                pass
            else:
                print('Invalid command. Run \'help\' or \'h\' for usage description.')
        except (ValueError, IndexError):
            print('Invalid command. Type `help` or `h` for help.')
        except KeyboardInterrupt:
            print()
            pass  # Ignore Ctrl-C event


if __name__ == '__main__':
    main()
