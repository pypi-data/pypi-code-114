import re

# Function : Interface
# Description : This Function needs to be used as decorator to specify the custom functions which will be called in the template
# Returns : Returns a Wrapper for any functions defined as Interface using keyword "@Interface"
def Interface(InputFunction):

	def Wrapper(self, *args, **kwargs):

		RetStr = str(InputFunction(self, *args, **kwargs));
		self._OUT = RetStr;
		return self._OUT;

	return Wrapper;

# class : VARIABLES
# A Utility class to be used to store the Object members used in template function call arguments
class VARIABLES():

	pass

# class : TemplateEngine(for FILLING)
# The class will be used to fill a template and write the resultant content as a filename
class FillerTemplateEngine():

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
		assert FuncCallTemplate[cap_len:-shoe_len].strip() == "self.FUNC_CALL()", """	  Second Parameter has 3 parts, \n <LEADING_EDGE><FUNC_CALL><TRAILING_EDGE>""";
		
		#Finalizing the REGEX pattern, Leading edge, Trailing edge specifications
		self.__pattern = RegexPattern.replace("*self.","*#* *self.");
		self.__LeadTrailSpecs = [ ( cap, cap_len ), ( shoe, -shoe_len )];

	# method : InFile
	# Gets the Template Name/Path of the template function calls that is going to be used.
	# Will initialize the MapDict for updating the function calls in the template.
	# Parameters : 
	#   arg1 - TemplateName [a String that contains the Path/Name of the template]
	#   arg2 - DebugTokens [If True prints the function calls identified in the template, if False doesn't print - meant for debugging]
	def InFile(self, TemplateName, DebugTokens=False):

		#Getting the file content of TemplateName
		template = open(TemplateName, 'r');
		self.__content = template.read();
		template.close();

		#Initializing MapDict as per TemplateName
		self.__MapDict = {  };
		func_calls = [self.__content[m.start(0):m.end(0)] for m in re.finditer(self.__pattern, self.__content)];
		for x in func_calls:
			self.__MapDict[x] = "";

		#Printing all function calls for debugging if DebugTokensEnabled
		if(DebugTokens):
			for x in self.__MapDict.keys():
				print(x);

	# method : VARS
	# Returns an Instance of the an empty class <VARIABLES>, for argument variables storage.
	def VARS(self):

		return VARIABLES();

	# method : AbstractFuncCalls
	# Internal function for the updation of local variables and function calls from the template.
	# This function abstracts the variables and function calls from the entire class
	def __AbstractFuncCalls(self):

		assert "self" not in self.__VarDict.keys(), "self is a KEYWORD, not ALLOWED FOR USE";

		#Initialising function local variables from self.__VarDict
		for self.__key in self.__VarDict.keys():
			locals()[self.__key] = self.__VarDict[self.__key];

		#Calculating Mapdict[key] results by function Invocation
		self.__INP = "";
		for x in self.__MapDict.keys():
			self.__INP = x[self.__LeadTrailSpecs[0][1]:self.__LeadTrailSpecs[1][1]].strip();
			self._OUT = "";
			if(self.__INP[0] != "#"):
				exec(self.__INP);
			self.__MapDict[x] = self._OUT;

	# method : OutFile
	# Defines the file Name/Path that needs to be generated with the filled content from the template.
	# It edits the template based on the dependencies/arguments of the template function calls.
	# Parameters : 
	#   arg1 - FuncArgVars [an instance of class <VARIABLES> with appropriate members filled]
	#   arg2 - UniqueName [filename tobe generated with the edited template content]
	# Returns : 
	# 	self.__MapDict - the result as a dictionary [keys:func_calls and values:Return_values]
	def OutFile(self, FuncArgVars, UniqueName):

		self.__VarDict = FuncArgVars.__dict__;
		self.__AbstractFuncCalls();

		#Replacing key with MapDict[Key] in Template 
		content = self.__content;
		file = open(UniqueName, 'w');
		for x in self.__MapDict.keys():
			content = content.replace(x, self.__MapDict[x]);

		#Writing the contents modified with the filename
		lines = content.splitlines(True);
		file.writelines(lines);
		file.close();

		return self.__MapDict;

	# method : VAR(sample Interface)
	# Defined as an interface which can be called directly in the template
	# Gets the variable and returns it.
	# Parameters : 
	#   arg1 - variable [a variable customised with the function call specified in the template]
	# Returns : 
	#	variable [which is providedas arg 1]
	@Interface
	def VAR(self, variable):

		return variable;

# 
# (see FillerCodeFlow.png) for the code flow
#
# Visit @Palani-SN(github profile) or send messages to
# psn396@gmail.com.
#
