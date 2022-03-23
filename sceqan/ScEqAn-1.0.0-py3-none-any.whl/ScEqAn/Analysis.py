import os
import re
import itertools

# class : DynamicProgramAnalysis
# The class will be used for analysing an equation/expression written in SEA script based on the boundary values from the ranges
class DynamicProgramAnalysis():

    # constructor : __init__
    # Defines the Input FileName to be used and the LogFileName to be created as reports. 
    # Parameters : 
    #   arg1 - FileName (File containing expressions as SEA script)
    #   arg2 - LogFileName (File to be created as reports)
    def __init__(self, FileName, LogFileName):

        with open(os.path.join(os.getcwd(),FileName), "r") as file:
            self.__lines = file.readlines()

        self.__LogFileName = os.path.join(os.getcwd(),LogFileName);
        self.__Exception_Stack = []
        self.__Debug = False;
        self.__unmonitored_outputs = [];
        self.CELL_LENGTH = 20;

    # method : Run
    # Initiates the process of dynamic analysis of the expressions read.
    # Parameters : 
    #   arg1 - Debug [If True prints the stages , if False doesn't print - meant for debugging]
    def Run(self, Debug = False):

        self.__Debug = Debug;

        MESSAGE = f" Phase I - Extract_Variables ";
        if(self.__Debug): print("\n"+MESSAGE.center(82, '#')+"\n");
        self.__Extract_Variables()

        MESSAGE = f" Phase II - Extract_Ranges ";
        if(self.__Debug): print("\n"+MESSAGE.center(82, '#')+"\n");
        self.__Extract_Ranges()

        MESSAGE = f" Phase III - Build_CodeLines ";
        if(self.__Debug): print("\n"+MESSAGE.center(82, '#')+"\n");
        self.__Build_CodeLines()

        MESSAGE = f" Phase IV - Build_Combinations ";
        if(self.__Debug): print("\n"+MESSAGE.center(82, '#')+"\n");
        self.__Build_Combinations()

        MESSAGE = f" Phase V - Run_Iterations ";
        if(self.__Debug): print("\n"+MESSAGE.center(82, '#')+"\n");
        self.__Run_Iterations()

        MESSAGE = f" Phase VI - Create_Reports ";
        if(self.__Debug): print("\n"+MESSAGE.center(82, '#')+"\n");
        self.__Create_Reports()
        MESSAGE = f" XXX ";
        if(self.__Debug): print("\n"+MESSAGE.center(82, '#')+"\n");

    # method : __Extract_Variables (Internal function)
    # Extracts the variable names in the expressions.
    def __Extract_Variables(self):

        self.__Var_IN = [];
        self.__Var_OUT = [];

        regex = r"([a-zA-Z]+)"
        for i in range(len(self.__lines)):
            exp = re.split('[{}; ]', self.__lines[i]);
            Vars = [exp[x] for x in range(0,len(exp)) if (re.match('.*[a-zA-Z].*', exp[x]) != None)]

            for var in Vars:

                if(self.__lines[i].find(var)>self.__lines[i].find('=')):

                    if(self.__lines[i][self.__lines[i].find(var)+len(var)]=="{"):
                        self.__Var_IN.append(var);
                    else:
                        if(var not in (self.__Var_IN + self.__Var_OUT + self.__unmonitored_outputs)):
                            print("uncontrolled inputs :", var)
                elif(self.__lines[i].find(var)<self.__lines[i].find('=')):
                    if(var[0] == "[") and (var[len(var)-1] == "]"):
                        self.__Var_OUT.append(var[1:-1])
                    else:
                        self.__unmonitored_outputs.append(var);
                else:
                    print("unsatisfied variables :", var);

        Var_List = self.__Var_IN+self.__Var_OUT;
        self.CELL_LENGTH = len( max(Var_List, key=len) )+10;

        if(self.__Debug):
            print(f"input_vars : {self.__Var_IN}");
            print(f"output_vars : {self.__Var_OUT}");

    # method : __Extract_Ranges (Internal function)
    # Extracts the ranges of the input variable names in the expressions.
    def __Extract_Ranges(self):

        self.__Ranges={};

        for i in range(len(self.__lines)):
            for var in self.__Var_IN:
                if(var in self.__lines[i]):
                    strt_idx = self.__lines[i].find(var)+len(var);
                    if(strt_idx != -1) and (self.__lines[i][strt_idx] == "{"):
                        end_idx = self.__lines[i][strt_idx:len(self.__lines[i])].find("}");
                        ranges = self.__lines[i][(strt_idx+1):((strt_idx + end_idx)-1)]
                        if(ranges.find(',') != -1):
                            sub = re.split(',', ranges)
                            st = float(sub[0]);
                            nd = float(sub[1]);
                            self.__Ranges[var]=self.__worst_case_in(st,nd);
                        else:
                            print("no comma found !");
                    else:
                        pass

        if(self.__Debug):
            print(f"ranges : {self.__Ranges}");

    # method : __Build_CodeLines (Internal function)
    # Builds the codelines based on variables, for running with boundary values.
    def __Build_CodeLines(self):

        self.__CodeLines = "";

        code_lines_list = self.__lines.copy();
        for i in range(len(self.__lines)):
            for var in self.__Var_OUT:
                if var in code_lines_list[i]:
                    code_lines_list[i] = code_lines_list[i].replace("["+var+"]", "globals()[\""+var+"\"]");

        code_lines = "".join(code_lines_list.copy());
        func_calls = [code_lines[m.start(0):m.end(0)] for m in re.finditer("{ *(?:(?!}).)*}", code_lines)];
        for x in func_calls:
            code_lines = code_lines.replace(x, "");

        self.__CodeLines = code_lines;

        if(self.__Debug):
            print(self.__CodeLines)

    # method : __Build_Combinations (Internal function)
    # Builds the combinations based on boundary values, for running codelines.
    def __Build_Combinations(self):

        self.__Keyss = []
        self.__Combinations = [];

        self.__Keyss = [x for x in self.__Ranges.keys()];
        valuess = [self.__Ranges[x] for x in self.__Ranges.keys()]
        self.__Combinations = [p for p in itertools.product(*valuess)]

        if(self.__Debug):
            print(self.__Combinations);

    # method : __Run_Iterations (Internal function)
    # Runs the iterations of codelines with different possibilities of boundary values.
    def __Run_Iterations(self):

        for var in self.__Var_OUT:
            globals()[var+"_max"] = -10000000;
            globals()[var+"_min"] = 10000000;

        for combination in self.__Combinations:

            for x in range(len(self.__Keyss)):
                globals()[self.__Keyss[x]] = list(combination)[x]

            try:

                exec(self.__CodeLines)

                for x in range(len(self.__Var_OUT)):
                
                    if(globals()[self.__Var_OUT[x]] < globals()[self.__Var_OUT[x]+"_min"]):
                        globals()[self.__Var_OUT[x]+"_min"] = globals()[self.__Var_OUT[x]];
                        for y in range(len(self.__Keyss)):
                            globals()[self.__Var_OUT[x]+"_min"+self.__Keyss[y]] = globals()[self.__Keyss[y]];
                        
                    if(globals()[self.__Var_OUT[x]] > globals()[self.__Var_OUT[x]+"_max"]):
                        globals()[self.__Var_OUT[x]+"_max"] = globals()[self.__Var_OUT[x]]
                        for y in range(len(self.__Keyss)):
                            globals()[self.__Var_OUT[x]+"_max"+self.__Keyss[y]] = globals()[self.__Keyss[y]];

            except Exception as ex:
                print(ex);
                if(str(x) not in self.__Exception_Stack):
                    self.__Exception_Stack.append(str(ex));

        if(self.__Debug):
            for var in self.__Var_OUT:
                output = "min("+var+"): "+str(globals()[var+"_min"]), "max("+var+"): "+str(globals()[var+"_max"])
                print(str(output))

    # method : __Create_Reports (Internal function)
    # Creates the reports with extreme values of output and the boundary values which is the cause of it.
    def __Create_Reports(self):

        self.__Reports = "";
        CELL_LENGTH = self.CELL_LENGTH;
        log = open(self.__LogFileName, "w");
        log.write("#"*( (4* (CELL_LENGTH+1) )+1 )+"\n\n");
        log.write("".join(self.__lines)+"\n\n")
        log.write("#"*( (4* (CELL_LENGTH+1) )+1 )+"\n\n");
        header = "\n|"+"VAR".center(CELL_LENGTH, ' ')+"|"+"TYPE".center(CELL_LENGTH, ' ')+"|"+"MIN".center(CELL_LENGTH, ' ')+"|"+"MAX".center(CELL_LENGTH, ' ')+"|";

        if(self.__Exception_Stack == []):

            for var in self.__Var_OUT:
                output = "|"+var.center(CELL_LENGTH, ' ')+"|"+"OUT".center(CELL_LENGTH, ' ')+"|"+str(globals()[var+"_min"]).center(CELL_LENGTH, ' ')+"|"+str(globals()[var+"_max"]).center(CELL_LENGTH, ' ')+"|";
                log.write("="*( (4* (CELL_LENGTH+1) )+1 ));
                log.write(str(header)+"\n")
                log.write("="*( (4* (CELL_LENGTH+1) )+1 )+"\n");
                log.write(str(output)+"\n")
                log.write("-"*( (4* (CELL_LENGTH+1) )+1 )+"\n");
                

                for y in range(len(self.__Keyss)):
                    max_min_out = "|"+self.__Keyss[y].center(CELL_LENGTH, ' ')+"|"+"IN".center(CELL_LENGTH, ' ')+"|"+str(globals()[var+"_min"+self.__Keyss[y]]).center(CELL_LENGTH, ' ')+"|"+str(globals()[var+"_max"+self.__Keyss[y]]).center(CELL_LENGTH, ' ')+"|";
                    log.write(str(max_min_out)+"\n");

                log.write("="*( (4* (CELL_LENGTH+1) )+1 )+"\n");

        else:

            log.write("\n".join(self.__Exception_Stack));

        log.close()
        if(self.__Debug):
            print(f"Written file [ {self.__LogFileName} ]");

    # method : __abs_min_max (Internal function)
    # returns the absolute sorted list of the two arguments fed.
    # Parameters : 
    #   arg1 - variable_st
    #   arg2 - variable_nd
    # Returns : 
    #   list [ absolute min & max ]
    def __abs_min_max(self, st, nd):

        lst = [st,nd];
        return [min(lst), max(lst)]

    # method : __act_min_max (Internal function)
    # returns the actual sorted list of the two arguments fed.
    # Parameters : 
    #   arg1 - variable_st
    #   arg2 - variable_nd
    # Returns : 
    #   list [ actual min & max ]
    def __act_min_max(self, st, nd):

        lst = [st,nd];
        return self.__abs_min_max(0,max(lst)) + [st]

    # method : __worst_case_in (Internal function)
    # returns the worst case ranges from the two arguments fed.
    # Parameters : 
    #   arg1 - variable_st
    #   arg2 - variable_nd
    # Returns : 
    #   list [ sorted list ]
    def __worst_case_in(self, st, nd):

        if((int(st) >= 0) and (int(nd) >= 0)):
            lst = self.__abs_min_max(st,nd);
        else:
            lst = self.__act_min_max(st,nd);

        return sorted(lst)

# 
# (see AnalysisCodeflow.png) for the code flow
#
# Visit @Palani-SN(github profile) or send messages to
# psn396@gmail.com.
#
