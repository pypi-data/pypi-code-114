'''
Created on Mar 19, 2021

@author: Juan L. Mateo
'''

import json
import re
from aceofbases import pam

class BaseEditor:
    '''
    Generic class to define the different base editors with their PAM types
    and the methods needed.
    The seed for Bowtie will be always 5 prime, as well as the window location,
    but with respect to the target sequence.
    '''
    def __init__(self, pam_str, window_start, window_end, optimal_window_start,
                 optimal_window_end, base_to_edit, target_size):
        self.pam = pam.factory(pam_str)
        self.window_start = window_start
        self.window_end = window_end
        self.optimal_window_start = optimal_window_start
        self.optimal_window_end = optimal_window_end
        self.base_to_edit = base_to_edit
        self.target_size = target_size

    def get_pam(self):
        "Returns the object representing the PAM"
        return self.pam

    def get_window_start(self):
        "Returns the initial position of the windown within the target sequence"
        return self.window_start

    def get_window_end(self):
        "Returns the final position of the windown within the target sequence"
        return self.window_end

    def get_optimal_window_start(self):
        "Returns the optimal initial position of the windown within the target sequence"
        return self.optimal_window_start

    def get_optimal_window_end(self):
        "Returns the optimal final position of the windown within the target sequence"
        return self.optimal_window_end

    def get_base_to_edit(self):
        "Returns the base to be edited"
        return self.base_to_edit

    def get_target_size(self):
        "Returns the target size"
        return self.target_size

    def score_target(self, target_seq):
        "Returns the score for the current target as the efficacy of the edit"
        return 0

class BE4_Gam(BaseEditor):
    "Class that encodes the BE4-Gam base editor"
    def __init__(self):
        super().__init__("NGG",2,10,3,8,'C',20)

    def score_target(self, target_seq):
        idx_cs = [m.start() for m in re.finditer("C",target_seq, re.I)]
        score = float('-inf')
        for idx in idx_cs:
            if idx<self.window_start:
                continue
            if idx>=self.window_end:
                break
            if self.optimal_window_start <= idx < self.optimal_window_end:
                current_score = 5
            else:
                current_score = 1
            if target_seq[idx-1] == "C":
                current_score -= 2
            if target_seq[idx-1] == "A":
                current_score -= 3
            if target_seq[idx-1] == "G":
                current_score -= 4
            if current_score>score:
                score=current_score
        return score

class ancBE4max(BaseEditor):
    "Class that encodes the ancBE4max base editor"
    def __init__(self):
        super().__init__("NGG",2,9,3,7,'C',20)

    def score_target(self, target_seq):
        idx_cs = [m.start() for m in re.finditer("C",target_seq, re.I)]
        score = float('-inf')
        for idx in idx_cs:
            if idx<self.window_start:
                continue
            if idx>=self.window_end:
                break
            if self.optimal_window_start <= idx < self.optimal_window_end:
                current_score = 10
            else:
                current_score = 2
            if target_seq[idx-1] == "C":
                current_score -= 2
            if target_seq[idx-1] == "A":
                current_score -= 2
            if target_seq[idx-1] == "G":
                current_score -= 8
            if current_score>score:
                score=current_score
        return score

class evoBE4max(BaseEditor):
    "Class that encodes the evoBE4max base editor"
    def __init__(self):
        super().__init__("NGG",0,11,3,8,'C',20)

    def score_target(self, target_seq):
        idx_cs = [m.start() for m in re.finditer("C",target_seq, re.I)]
        score = float('-inf')
        for idx in idx_cs:
            if idx<self.window_start:
                continue
            if idx>=self.window_end:
                break
            if self.optimal_window_start <= idx < self.optimal_window_end:
                current_score = 10
            else:
                current_score = 2
            if target_seq[idx-1] == "C":
                current_score -= 2
            if target_seq[idx-1] == "A":
                current_score -= 8
            if target_seq[idx-1] == "G":
                current_score -= 2
            if current_score>score:
                score=current_score
        return score

class ABE8e(BaseEditor):
    "class that encodes the ABE8e base editor"
    def __init__(self):
        super().__init__("NGG",2,9,3,8,'A',20)

    def score_target(self, target_seq):
        if "A" in target_seq[self.optimal_window_start:self.optimal_window_end]:
            return 10
        if "A" in target_seq[self.window_start:self.window_end]:
            return 2
        return 0

def factory(type):
    "Method following the factory patern to create the different base editor objects"
    editors = {
        "BE4-Gam": BE4_Gam,
        "ancBE4max": ancBE4max,
        "evoBE4max": evoBE4max,
        "ABE8e": ABE8e
        }
    if not type in editors:
        assert 0, "Wrong Base Editor type: " + type
    return editors[type]()

if __name__ == "__main__":
    dictionary = {}
    for cls in BaseEditor.__subclasses__():
        obj = cls()
        dictionary[obj.__class__.__name__] = obj.__dict__
    with open("base_editors.js", "w") as fp:
        fp.write("var jsonBaseEditors=")
        json.dump(dictionary, fp, default=vars)
