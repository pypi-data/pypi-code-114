def read_envi_binary():
    print("ENVI Read .bin Test")


def read_envi_hdr(filename: str):
    print("ENVI Read .hdr Test")
    print(filename)


def eni_read():
    read_envi_hdr()
    read_envi_binary()

def envi_write():
    print("ENVI Write Test")