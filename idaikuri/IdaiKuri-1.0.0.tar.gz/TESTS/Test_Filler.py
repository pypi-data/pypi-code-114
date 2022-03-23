from IdaiKuri.Filler import FillerTemplateEngine as TemplateEngine
from IdaiKuri.Filler import Interface
import pytest

##########################################################################################################
## Default Test cases using default Regex delimiters without custom function calls 
##########################################################################################################

@pytest.fixture
def DefaultRegex1():
    TE = TemplateEngine();
    TE.InFile("TemplateFiles/Template_DefaultCase1.html", True); 
    return TE;

def test_DefaultCase1(DefaultRegex1):

    print("Test cases using "
        "default Regex delimiters in templates "
        "without custom function calls "
        "for creating file 1")

    TE = DefaultRegex1;  
    temp_vars = TE.VARS();
    temp_vars.Portrait = "images/GuidoVanRossum.png";
    temp_vars.Logo = "images/PythonLogo.png";
    temp_vars.FullName = "Guido Van Rossum";
    temp_vars.Position = "Python's Benevolent Dictator for life";
    temp_vars.Quote = "In Python, every symbol you type is essential.";
    temp_vars.Author = "Guido van Rossum";
    result_dict = TE.OutFile(temp_vars, "GeneratedFiles/GuidoVanRossum_DefaultCase1.html");
    input_dict = temp_vars.__dict__;
    for x in result_dict.keys():
        for y in input_dict.keys():
            if(y in x):
                assert(result_dict[x] == input_dict[y]);

    file = open("GeneratedFiles/GuidoVanRossum_DefaultCase1.html", 'r');
    content = file.readlines();
    assert(content[11] == """        <img src="images/GuidoVanRossum.png" height="150" width="150">\n""")
    assert(content[12] == """        <img src="images/PythonLogo.png" height="150" width="150">\n""")

    assert(content[14] == """    <h2>Guido Van Rossum</h2>\n""")
    assert(content[15] == """    <h4>Python's Benevolent Dictator for life</h4>\n""")
    assert(content[16] == """    <p>In Python, every symbol you type is essential.</p>\n""")
    assert(content[17] == """    <p>&mdash;Guido van Rossum</p>\n""")


def test_DefaultCase2(DefaultRegex1):

    print("Test cases using "
        "default Regex delimiters in templates "
        "without custom function calls "
        "for creating file 2")

    TE = DefaultRegex1;
    temp_vars = TE.VARS();
    temp_vars.Portrait = "images/LinusTorvalds.png";
    temp_vars.Logo = "images/LinuxLogo.png";
    temp_vars.FullName = "Linus Torvalds";
    temp_vars.Position = "Creator of Linux and Git";
    temp_vars.Quote = "The Linux philosophy is \n'laugh in the face of danger'. \n<br> Oops. Wrong one. \n<br>'Do it yourself'. \nThat's it.";
    temp_vars.Author = "Linus Torvalds";
    result_dict = TE.OutFile(temp_vars, "GeneratedFiles/LinusTorvalds_DefaultCase1.html");
    input_dict = temp_vars.__dict__;
    for x in result_dict.keys():
        for y in input_dict.keys():
            if(y in x):
                assert(result_dict[x] == input_dict[y]);

    file = open("GeneratedFiles/LinusTorvalds_DefaultCase1.html", 'r');
    content = file.readlines();
    assert(content[11] == """        <img src="images/LinusTorvalds.png" height="150" width="150">\n""")
    assert(content[12] == """        <img src="images/LinuxLogo.png" height="150" width="150">\n""")

    assert(content[14] == """    <h2>Linus Torvalds</h2>\n""")
    assert(content[15] == """    <h4>Creator of Linux and Git</h4>\n""")
    assert(content[16] == """    <p>The Linux philosophy is \n""")
    assert(content[17] == """'laugh in the face of danger'. \n""")
    assert(content[18] == """<br> Oops. Wrong one. \n""")
    assert(content[19] == """<br>'Do it yourself'. \n""")
    assert(content[20] == """That's it.</p>\n""")
    assert(content[21] == """    <p>&mdash;Linus Torvalds</p>\n""")

##########################################################################################################
## Default Test cases using default Regex delimiters with custom function calls
##########################################################################################################

class AdvancedTemplate(TemplateEngine):

    @Interface
    def get_portrait(self, name):

        return "images/"+name.replace(" ","")+".png";

    @Interface
    def get_logo(self, contrib):

        return "images/"+contrib+"Logo.png"

@pytest.fixture
def DefaultRegex2():
    TE = AdvancedTemplate();
    TE.InFile("TemplateFiles/Template_DefaultCase2.html", True); 
    return TE;

def test_DefaultCase3(DefaultRegex2):

    print("Test cases using "
        "default Regex delimiters in templates "
        "with custom function calls "
        "for creating file 1")

    TE = DefaultRegex2;  
    temp_vars = TE.VARS();
    temp_vars.FullName = "Guido Van Rossum";
    temp_vars.Position = "Python's Benevolent Dictator for life";
    temp_vars.Quote = "In Python, every symbol you type is essential.";
    temp_vars.Contribution = "Python"
    result_dict = TE.OutFile(temp_vars, "GeneratedFiles/GuidoVanRossum_DefaultCase2.html");
    input_dict = temp_vars.__dict__;
    for x in result_dict.keys():
        for y in input_dict.keys():
            if(y in x):
                if("get_portrait" in x): assert(result_dict[x] == "images/GuidoVanRossum.png");
                elif("get_logo" in x): assert(result_dict[x] == "images/PythonLogo.png");
                else:assert(result_dict[x] == input_dict[y]);

    file = open("GeneratedFiles/GuidoVanRossum_DefaultCase2.html", 'r');
    content = file.readlines();
    assert(content[11] == """        <img src="images/GuidoVanRossum.png" height="150" width="150">\n""")
    assert(content[12] == """        <img src="images/PythonLogo.png" height="150" width="150">\n""")

    assert(content[14] == """    <h2>Guido Van Rossum</h2>\n""")
    assert(content[15] == """    <h4>Python's Benevolent Dictator for life</h4>\n""")
    assert(content[16] == """    <p>In Python, every symbol you type is essential.</p>\n""")
    assert(content[17] == """    <p>&mdash;Guido Van Rossum</p>\n""")


def test_DefaultCase4(DefaultRegex2):

    print("Test cases using "
        "default Regex delimiters in templates "
        "with custom function calls "
        "for creating file 2")

    TE = DefaultRegex2;
    temp_vars = TE.VARS();
    temp_vars.FullName = "Linus Torvalds";
    temp_vars.Position = "Creator of Linux and Git";
    temp_vars.Quote = "The Linux philosophy is \n'laugh in the face of danger'. \n<br> Oops. Wrong one. \n<br>'Do it yourself'. \nThat's it.";
    temp_vars.Contribution = "Linux";
    result_dict = TE.OutFile(temp_vars, "GeneratedFiles/LinusTorvalds_DefaultCase2.html");
    input_dict = temp_vars.__dict__;
    for x in result_dict.keys():
        for y in input_dict.keys():
            if(y in x):
                if("get_portrait" in x): assert(result_dict[x] == "images/LinusTorvalds.png");
                elif("get_logo" in x): assert(result_dict[x] == "images/LinuxLogo.png");
                else:assert(result_dict[x] == input_dict[y]);

    file = open("GeneratedFiles/LinusTorvalds_DefaultCase2.html", 'r');
    content = file.readlines();
    assert(content[11] == """        <img src="images/LinusTorvalds.png" height="150" width="150">\n""")
    assert(content[12] == """        <img src="images/LinuxLogo.png" height="150" width="150">\n""")

    assert(content[14] == """    <h2>Linus Torvalds</h2>\n""")
    assert(content[15] == """    <h4>Creator of Linux and Git</h4>\n""")
    assert(content[16] == """    <p>The Linux philosophy is \n""")
    assert(content[17] == """'laugh in the face of danger'. \n""")
    assert(content[18] == """<br> Oops. Wrong one. \n""")
    assert(content[19] == """<br>'Do it yourself'. \n""")
    assert(content[20] == """That's it.</p>\n""")
    assert(content[21] == """    <p>&mdash;Linus Torvalds</p>\n""")

##########################################################################################################
## Custom Test cases using custom Regex delimiters with custom function calls
##########################################################################################################

class SpecialTemplate(TemplateEngine):

    @Interface
    def get_portrait(self, name):

        return "images/"+name.replace(" ","")+".png";

    @Interface
    def get_logo(self, contrib):

        return "images/"+contrib+"Logo.png"

@pytest.fixture
def SpecialRegex1():
    TE = SpecialTemplate(("_StArT_", "_eNd_"), "_StArT_self.FUNC_CALL()_eNd_");
    TE.InFile("TemplateFiles/Template_SpecialCase1.html", True);
    print(""); 
    return TE;

@pytest.fixture
def SpecialRegex2():
    TE = SpecialTemplate(("<<", ">>"), "<<self.FUNC_CALL()>>");
    TE.InFile("TemplateFiles/Template_SpecialCase2.html", True);
    print("");  
    return TE;

@pytest.fixture
def SpecialRegex3():
    TE = SpecialTemplate(("\\[\\[", "\\]\\]"), "[[self.FUNC_CALL()]]");
    TE.InFile("TemplateFiles/Template_SpecialCase3.html", True); 
    print(""); 
    return TE;

@pytest.fixture
def SpecialRegex4():
    TE = SpecialTemplate(("{\\[<{\\[", "}\\]>}\\]"), "{[<{[self.FUNC_CALL()}]>}]");
    TE.InFile("TemplateFiles/Template_SpecialCase4.html", True); 
    return TE;

def test_SpecialCase1(SpecialRegex1, SpecialRegex2, SpecialRegex3, SpecialRegex4):

    print("Test cases using "
        "custom Regex delimiters in templates "
        "with custom function calls (commented/uncommented) "
        "for creating file 1")

    for filex in ([1,2,3,4]):

        if(filex==1):TE = SpecialRegex1;
        if(filex==2):TE = SpecialRegex2;
        if(filex==3):TE = SpecialRegex3;
        if(filex==4):TE = SpecialRegex4; 

        temp_vars = TE.VARS();
        temp_vars.FullName = "Guido Van Rossum";
        temp_vars.Position = "Python's Benevolent Dictator for life";
        temp_vars.Quote = "In Python, every symbol you type is essential.";
        temp_vars.Contribution = "Python"
        result_dict = TE.OutFile(temp_vars, f"GeneratedFiles/GuidoVanRossum_SpecialCase{filex}.html");
        input_dict = temp_vars.__dict__;
        for x in result_dict.keys():
            if("#" not in x):
                for y in input_dict.keys():
                    if(y in x):
                        if("get_portrait" in x): assert(result_dict[x] == "images/GuidoVanRossum.png");
                        elif("get_logo" in x): assert(result_dict[x] == "images/PythonLogo.png");
                        else:assert(result_dict[x] == input_dict[y]);
            else:
                assert(result_dict[x] == "");

        file = open(f"GeneratedFiles/GuidoVanRossum_SpecialCase{filex}.html", 'r');
        content = file.readlines();
        assert(content[11] == """        <img src="images/GuidoVanRossum.png" height="150" width="150">\n""")
        assert(content[12] == """        <img src="images/PythonLogo.png" height="150" width="150">\n""")

        assert(content[14] == """    <h2>Guido Van Rossum</h2>\n""")
        assert(content[15] == """    <h4>Python's Benevolent Dictator for life</h4>\n""")
        assert(content[16] == """    <p>In Python, every symbol you type is essential.</p>\n""")
        assert(content[17] == """    <p>&mdash;</p>\n""")


def test_SpecialCase2(SpecialRegex1, SpecialRegex2, SpecialRegex3, SpecialRegex4):

    print("Test cases using "
        "custom Regex delimiters in templates "
        "with custom function calls (commented/uncommented) "
        "for creating file 2")

    for filex in ([1,2,3,4]):

        if(filex==1):TE = SpecialRegex1;
        if(filex==2):TE = SpecialRegex2;
        if(filex==3):TE = SpecialRegex3;
        if(filex==4):TE = SpecialRegex4; 

        temp_vars = TE.VARS();
        temp_vars.FullName = "Linus Torvalds";
        temp_vars.Position = "Creator of Linux and Git";
        temp_vars.Quote = "The Linux philosophy is \n'laugh in the face of danger'. \n<br> Oops. Wrong one. \n<br>'Do it yourself'. \nThat's it.";
        temp_vars.Contribution = "Linux";
        result_dict = TE.OutFile(temp_vars, f"GeneratedFiles/LinusTorvalds_SpecialCase{filex}.html");
        input_dict = temp_vars.__dict__;
        for x in result_dict.keys():
            if("#" not in x):
                for y in input_dict.keys():
                    if(y in x):
                        if("get_portrait" in x): assert(result_dict[x] == "images/LinusTorvalds.png");
                        elif("get_logo" in x): assert(result_dict[x] == "images/LinuxLogo.png");
                        else:assert(result_dict[x] == input_dict[y]);
            else:
                assert(result_dict[x] == "");

        file = open(f"GeneratedFiles/LinusTorvalds_SpecialCase{filex}.html", 'r');
        content = file.readlines();
        assert(content[11] == """        <img src="images/LinusTorvalds.png" height="150" width="150">\n""")
        assert(content[12] == """        <img src="images/LinuxLogo.png" height="150" width="150">\n""")

        assert(content[14] == """    <h2>Linus Torvalds</h2>\n""")
        assert(content[15] == """    <h4>Creator of Linux and Git</h4>\n""")
        assert(content[16] == """    <p>The Linux philosophy is \n""")
        assert(content[17] == """'laugh in the face of danger'. \n""")
        assert(content[18] == """<br> Oops. Wrong one. \n""")
        assert(content[19] == """<br>'Do it yourself'. \n""")
        assert(content[20] == """That's it.</p>\n""")
        assert(content[21] == """    <p>&mdash;</p>\n""")

