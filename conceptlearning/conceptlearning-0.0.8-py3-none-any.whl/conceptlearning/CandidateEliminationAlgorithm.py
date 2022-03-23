from conceptlearning.ConceptLearning import ConceptLearning

class CandidateElimination(ConceptLearning):
    def __init__(self,data):
        super().__init__(data)
        self.G = set([("?", ) * len(self.domains[:-1])])
        self.S = set([("0", ) * len(self.domains[:-1])])
    
    def candidate_elimination(self):
        i=0
        print(f"Initial Generic Boundary G{i} {self.G}")
        print(f"Initial Specific Boundary S{i} {self.S}\n")
        for instance in self.data:
            i += 1
            x, label = instance[:-1], instance[-1]  # Splitting data into attributes and decisions
            print(f"Training instance {x} Label is '{label}'")
            if label=='yes': # x is positive example
                self.G = {g for g in self.G if self.__fulfills(x, g)}
                self.__generalize_S(x)
                print(f"Updated Specific Boundary {self.S}")
            else: # x is negative example
                self.S = {s for s in self.S if not self.__fulfills(x, s)}
                self.__specialize_G(x)
                print(f"Updated Generic Boundary {self.G}")
            print(f"Generic Boundary G{i}: {self.G}")
            print(f"Specific Boundary S{i}: {self.S}\n")
            
        return
    

    def __more_general(self,h1, h2):
        more_general_parts = []
        for x, y in zip(h1, h2):
            mg = x == "?" or (x != "0" and (x == y or y == "0"))
            more_general_parts.append(mg)
        return all(more_general_parts)

# min_generalizations
    def __fulfills(self,data, hypothesis):
    ### the implementation is the same as for hypotheses:
        return self.__more_general(hypothesis, data)
    

    def __generalize_S(self,x):
        S_prev = list(self.S)
        for s in S_prev:
            if s not in self.S:
                continue
            if not self.__fulfills(x, s):
                self.S.remove(s)
                Splus = self.__min_generalizations(s, x)
                ## keep only generalizations that have a counterpart in G
                self.S.update([h for h in Splus if any([self.__more_general(g,h) for g in self.G])])
                ## remove hypotheses less specific than any other in S
                self.S.difference_update([h for h in self.S if any([self.__more_general(h, h1) for h1 in self.S if h != h1])])
    
    def __specialize_G(self,x):
        G_prev = list(self.G)
        for g in G_prev:
            if g not in self.G:
                continue
            if self.__fulfills(x, g):
                self.G.remove(g)
                Gminus = self.__min_specializations(g, x)
    ## keep only specializations that have a conuterpart in S
                self.G.update([h for h in Gminus if any([self.__more_general(h, s) for s in self.S])])
    ## remove hypotheses less general than any other in G
                self.G.difference_update([h for h in self.G if any([self.__more_general(g1, h) for g1 in self.G if h != g1])])

    
    def __min_generalizations(self,h, x):
        h_new = list(h)
        for i in range(len(h)):
            if not self.__fulfills(x[i:i+1], h[i:i+1]):
                h_new[i] = '?' if h[i] != '0' else x[i]
        return [tuple(h_new)]
    
    def __min_specializations(self,h,x):
        results = []
        for i in range(len(h)):
            if h[i] == "?":
                for val in self.domains[i]:
                    if x[i] != val:
                        h_new = h[:i] + (val,) + h[i+1:]
                        results.append(h_new)
            elif h[i] != "0":
                h_new = h[:i] + ('0',) + h[i+1:]
                results.append(h_new)
        return results
