import re
import difflib

# class : TemplateEngine(for PARSING)
# The class will be used to parse a template and file associated with the template an returns the edited content as a dictionary
class ParserTemplateEngine():

    # constructor : __init__
    # Defines the configuration of the template function calls that is going to be used.
    # Configuration specified will be validated for the authenticity of Regex Pattern. 
    # Parameters : 
    #   arg1 - RegexEdges [a Tuple with a leading edge and trailing edge]
    #   arg2 - FuncCallTemplate [a string for initial validation of the RegexEdges]
    def __init__(self, RegexEdges=("{{", "}}"), FuncCallTemplate="{{self.FUNC_CALL()}}"):

        #Verify REGEX Pattern
        RegexPattern=f"{RegexEdges[0]} *self.(?:(?!{RegexEdges[1]}).)*{RegexEdges[1]}";
        func_call = [FuncCallTemplate[m.start(0):m.end(0)] for m in re.finditer(RegexPattern, FuncCallTemplate)][0]
        assert func_call == FuncCallTemplate, "RegexPattern and FuncCallTemplate not matching"
        
        #Verify FUNC_CALL Template
        lst = re.split("self.FUNC_CALL\\(\\)", func_call.replace(" ", ""));
        cap, cap_len, shoe ,shoe_len = tuple([ lst[0], len(lst[0]), lst[1], len(lst[1]) ]);
        assert FuncCallTemplate[cap_len:-shoe_len].strip() == "self.FUNC_CALL()", """     Second Parameter has 3 parts, \n <LEADING_EDGE><FUNC_CALL><TRAILING_EDGE>""";
        
        #Finalizing the REGEX pattern, Leading edge, Trailing edge specifications
        self.__pattern = RegexPattern.replace("*self.","*#* *self.");
        self.__LeadTrailSpecs = [ ( cap, cap_len ), ( shoe, -shoe_len ) ];

    # method : Root
    # Parses the file Name/Path and template Name/Path.
    # Returns the differences between them as a dict.
    # Parameters : 
    #   arg1 - TemplateName [Name of the template to be edited]
    #   arg2 - FileName [filename to be generated with the edited template content]
    # Returns : 
    #   RootDict - the result as a dictionary [keys:func_calls and values:Return_values]
    def Root(self, TemplateName, FileName):

        #Getting the file content of TemplateName
        template = open(TemplateName, 'r');
        TempCont = template.read();
        template.close();

        file = open(FileName, 'r');
        FileCont = file.read();
        file.close();

        #Initializing funccalls as per TemplateName
        func_calls = [TempCont[m.start(0):m.end(0)] for m in re.finditer(self.__pattern, TempCont)];

        #Finding Insertion List from TemplateWithoutInterfaces and File
        TempContReplaced = TempCont;
        for x in func_calls:
            TempContReplaced = TempContReplaced.replace(x, "");

        InsertionList = [];
        diffs = difflib.SequenceMatcher(None, TempContReplaced, FileCont);
        for opcode, a0, a1, b0, b1 in diffs.get_opcodes():
            if opcode == 'insert':
                InsertionList.append(diffs.b[b0:b1]);

        # Checking the length of the lists found
        CommentedList =[x for x in func_calls if "#" in x];
        assert len(InsertionList) == len(func_calls)-len(CommentedList), "Insertion and deletion list should be of same size";

        RootDict = {};
        for x in range(len(func_calls)):
            if("#" in func_calls[x]):
                RootDict[func_calls[x]] = "#Commented";
            else:
                RootDict[func_calls[x]] = InsertionList[x];

        return RootDict;

# 
# (see ParserCodeFlow.png) for the code flow
#
# Visit @Palani-SN(github profile) or send messages to
# psn396@gmail.com.
#