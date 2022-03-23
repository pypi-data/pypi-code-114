from conceptlearning.ConceptLearning import ConceptLearning
class FindS(ConceptLearning):
    def __init__(self,data):
        super().__init__(data)
        self.hypothesis = ['0'] * self.num_attributes
    
    def initialize_hypothesis(self):
        self.hypothesis = [self.data[0][j] for j in range(0,self.num_attributes)]
    
    def find_s(self):
        for instance in self.data:
# Consider only positive training instance x
            x, label = instance[:-1], instance[-1]  # Splitting data into attributes and decisions
            print(f"Training instance {x} Label is '{label}'")
            if label=='yes':
                    for j in range(0,self.num_attributes):
        # Replace ai in h by the next more general constraint that is satisfied by x

                        if x[j]!=self.hypothesis[j]:
                            self.hypothesis[j]='?'
                        else :
                            self.hypothesis[j]= x[j] 
            print(f"Updated hypothesis {self.hypothesis}\n")

