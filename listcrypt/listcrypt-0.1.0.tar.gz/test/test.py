from multiprocessing import Process, Manager, cpu_count
import math


def multi(data, cores):
    d = Manager().dict()
    
    segment_lengths = math.ceil(len(data)/cores)

    segmented_data = [data[size:size+segment_lengths] for size in range(0,segment_lengths*cores,segment_lengths)]

    def f(data, process, d):
        d[process] = data

    
    for item,process in zip(segmented_data, range(cores)):
        Process(target=f, args=(item, process, d)).start()

    while True:
        if len(d) == cores:
            return d

cores = cpu_count()

data = "hey man how are you doing on this fine day today?"

print(multi(data, cores))

