import argparse
from pymeshview import show_mesh


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, default=None, dest='input', help="Mesh file to load")
    parser.add_argument("-o", "--output", type=str, default=None, dest='output', help="Name of output file")
    parser.add_argument("--verbose", action='store_true', dest='verbose', help="Show the window")
    parser.add_argument("--no-highlight", action='store_true', dest='no_highlight',
                        help="Interactively look at mesh instead of generating highlight video")
    args = parser.parse_args()
    print(args)

    show_mesh(args)


if __name__ == '__main__':
    main()
    # args = convert_kwargs_to_args(output="out2.mp4")
    # show_mesh(args)
