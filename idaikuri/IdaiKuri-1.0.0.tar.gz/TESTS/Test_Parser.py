from IdaiKuri.Parser import ParserTemplateEngine as TemplateEngine
import pytest

##########################################################################################################
## Default Test cases using default Regex delimiters without custom function calls 
##########################################################################################################

@pytest.fixture
def DefaultRegex1():
    TE = TemplateEngine();
    return TE;

def test_DefaultCase1(DefaultRegex1):

    print("Test cases using "
        "default Regex delimiters in templates "
        "without custom function calls "
        "for parsing file 1")

    input_dict = {};
    TE = DefaultRegex1;  
    result_dict = TE.Root("TemplateFiles/Template_DefaultCase1.html", "GeneratedFiles/GuidoVanRossum_DefaultCase1.html");
    input_dict["inputPortrait"] = "images/GuidoVanRossum.png";
    input_dict["Logo"] = "images/PythonLogo.png";
    input_dict["FullName"] = "Guido Van Rossum";
    input_dict["Position"] = "Python's Benevolent Dictator for life";
    input_dict["Quote"] = "In Python, every symbol you type is essential.";
    input_dict["Author"] = "Guido van Rossum";
    for x in result_dict.keys():
        for y in input_dict.keys():
            if(y in x):
                assert(result_dict[x] == input_dict[y]);

def test_DefaultCase2(DefaultRegex1):

    print("Test cases using "
        "default Regex delimiters in templates "
        "without custom function calls "
        "for parsing file 2")

    input_dict = {};
    TE = DefaultRegex1;
    result_dict = TE.Root("TemplateFiles/Template_DefaultCase1.html", "GeneratedFiles/LinusTorvalds_DefaultCase1.html");
    input_dict["Portrait"] = "images/LinusTorvalds.png";
    input_dict["Logo"] = "images/LinuxLogo.png";
    input_dict["FullName"] = "Linus Torvalds";
    input_dict["Position"] = "Creator of Linux and Git";
    input_dict["Quote"] = "The Linux philosophy is \n'laugh in the face of danger'. \n<br> Oops. Wrong one. \n<br>'Do it yourself'. \nThat's it.";
    input_dict["Author"] = "Linus Torvalds";
    for x in result_dict.keys():
        for y in input_dict.keys():
            if(y in x):
                assert(result_dict[x] == input_dict[y]);

def test_DefaultCase3(DefaultRegex1):

    print("Test cases using "
        "default Regex delimiters in templates "
        "with custom function calls "
        "for parsing file 1")

    input_dict = {};
    TE = DefaultRegex1;  
    result_dict = TE.Root("TemplateFiles/Template_DefaultCase2.html", "GeneratedFiles/GuidoVanRossum_DefaultCase2.html");
    input_dict["FullName"] = "Guido Van Rossum";
    input_dict["Position"] = "Python's Benevolent Dictator for life";
    input_dict["Quote"] = "In Python, every symbol you type is essential.";
    input_dict["Contribution"] = "Python"
    for x in result_dict.keys():
        for y in input_dict.keys():
            if(y in x):
                if("get_portrait" in x): assert(result_dict[x] == "images/GuidoVanRossum.png");
                elif("get_logo" in x): assert(result_dict[x] == "images/PythonLogo.png");
                else:assert(result_dict[x] == input_dict[y]);

def test_DefaultCase4(DefaultRegex1):

    print("Test cases using "
        "default Regex delimiters in templates "
        "with custom function calls "
        "for parsing file 2")

    input_dict = {};
    TE = DefaultRegex1;
    result_dict = TE.Root("TemplateFiles/Template_DefaultCase2.html", "GeneratedFiles/LinusTorvalds_DefaultCase2.html");
    input_dict["FullName"] = "Linus Torvalds";
    input_dict["Position"] = "Creator of Linux and Git";
    input_dict["Quote"] = "The Linux philosophy is \n'laugh in the face of danger'. \n<br> Oops. Wrong one. \n<br>'Do it yourself'. \nThat's it.";
    input_dict["Contribution"] = "Linux";
    for x in result_dict.keys():
        for y in input_dict.keys():
            if(y in x):
                if("get_portrait" in x): assert(result_dict[x] == "images/LinusTorvalds.png");
                elif("get_logo" in x): assert(result_dict[x] == "images/LinuxLogo.png");
                else:assert(result_dict[x] == input_dict[y]);

##########################################################################################################
## Custom Test cases using custom Regex delimiters with custom function calls
##########################################################################################################

@pytest.fixture
def SpecialRegex1():
    TE = TemplateEngine(("_StArT_", "_eNd_"), "_StArT_self.FUNC_CALL()_eNd_");
    return TE;

@pytest.fixture
def SpecialRegex2():
    TE = TemplateEngine(("<<", ">>"), "<<self.FUNC_CALL()>>");
    return TE;

@pytest.fixture
def SpecialRegex3():
    TE = TemplateEngine(("\\[\\[", "\\]\\]"), "[[self.FUNC_CALL()]]");
    return TE;

@pytest.fixture
def SpecialRegex4():
    TE = TemplateEngine(("{\\[<{\\[", "}\\]>}\\]"), "{[<{[self.FUNC_CALL()}]>}]");
    return TE;

def test_SpecialCase1(SpecialRegex1, SpecialRegex2, SpecialRegex3, SpecialRegex4):

    print("Test cases using "
        "custom Regex delimiters in templates "
        "with custom function calls (commented/uncommented) "
        "for parsing file 1")

    for filex in ([1,2,3,4]):

        if(filex==1):TE = SpecialRegex1;
        if(filex==2):TE = SpecialRegex2;
        if(filex==3):TE = SpecialRegex3;
        if(filex==4):TE = SpecialRegex4; 
        input_dict = {};
        result_dict = TE.Root(f"TemplateFiles/Template_SpecialCase{filex}.html", f"GeneratedFiles/GuidoVanRossum_SpecialCase{filex}.html");
        input_dict["FullName"] = "Guido Van Rossum";
        input_dict["Position"] = "Python's Benevolent Dictator for life";
        input_dict["Quote"] = "In Python, every symbol you type is essential.";
        input_dict["Contribution"] = "Python"
        for x in result_dict.keys():
            if("#" not in x):
                for y in input_dict.keys():
                    if(y in x):
                        if("get_portrait" in x): assert(result_dict[x] == "images/GuidoVanRossum.png");
                        elif("get_logo" in x): assert(result_dict[x] == "images/PythonLogo.png");
                        else:assert(result_dict[x] == input_dict[y]);
            else:
                assert(result_dict[x] == "#Commented");


def test_SpecialCase2(SpecialRegex1, SpecialRegex2, SpecialRegex3, SpecialRegex4):

    print("Test cases using "
        "custom Regex delimiters in templates "
        "with custom function calls (commented/uncommented) "
        "for parsing file 2")

    for filex in ([1,2,3,4]):

        if(filex==1):TE = SpecialRegex1;
        if(filex==2):TE = SpecialRegex2;
        if(filex==3):TE = SpecialRegex3;
        if(filex==4):TE = SpecialRegex4; 
        input_dict = {};
        result_dict = TE.Root(f"TemplateFiles/Template_SpecialCase{filex}.html", f"GeneratedFiles/LinusTorvalds_SpecialCase{filex}.html");
        input_dict["FullName"] = "Linus Torvalds";
        input_dict["Position"] = "Creator of Linux and Git";
        input_dict["Quote"] = "The Linux philosophy is \n'laugh in the face of danger'. \n<br> Oops. Wrong one. \n<br>'Do it yourself'. \nThat's it.";
        input_dict["Contribution"] = "Linux";
        for x in result_dict.keys():
            if("#" not in x):
                for y in input_dict.keys():
                    if(y in x):
                        if("get_portrait" in x): assert(result_dict[x] == "images/LinusTorvalds.png");
                        elif("get_logo" in x): assert(result_dict[x] == "images/LinuxLogo.png");
                        else:assert(result_dict[x] == input_dict[y]);
            else:
                assert(result_dict[x] == "#Commented");

