from multiprocessing import Manager

m = Manager()

i = m.Value(int, 0)


if __name__ == '__main__':
    print('Done')
