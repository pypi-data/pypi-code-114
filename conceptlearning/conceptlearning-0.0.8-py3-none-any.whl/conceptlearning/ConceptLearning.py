class ConceptLearning:
    def __init__(self,data) -> None:
        self.domains = self.__get_domains(data)
        self.data = data
        self.num_attributes = len(self.domains[:-1])
    
    def __get_domains(self,data):
        d = [set() for i in data[0]]
        for x in data:
            for i, xi in enumerate(x):
                d[i].add(xi)
        return [list(sorted(x)) for x in d]