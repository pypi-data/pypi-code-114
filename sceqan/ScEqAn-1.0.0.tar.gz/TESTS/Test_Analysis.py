import pytest

from ScEqAn.Analysis import DynamicProgramAnalysis


def test_DynamicProgramAnalysis1():

    DynamicProgramAnalysis("InputFiles/Expression.txt", "OutputFiles/Expression.log").Run(Debug = False);
    ReferenceFile = open("InputFiles/Reference.log", 'r').readlines();
    CreatedFile = open("OutputFiles/Expression.log", 'r').readlines();
    assert len(ReferenceFile) == len(CreatedFile);
    for line_no in range(len(CreatedFile)):
        assert ReferenceFile[line_no] == CreatedFile[line_no]
        
def test_DynamicProgramAnalysis2():

    DynamicProgramAnalysis("InputFiles/Expression.txt", "OutputFiles/Expression.log").Run(Debug = True);
    ReferenceFile = open("InputFiles/Reference.log", 'r').readlines();
    CreatedFile = open("OutputFiles/Expression.log", 'r').readlines();
    assert len(ReferenceFile) == len(CreatedFile);
    for line_no in range(len(CreatedFile)):
        assert ReferenceFile[line_no] == CreatedFile[line_no]
        
def test_DynamicProgramAnalysis3(capsys):

    DynamicProgramAnalysis("InputFiles/Expression1.txt", "OutputFiles/Expression1.log").Run(Debug = False);
    CreatedFile = open("OutputFiles/Expression1.log", 'r').read();
    captured = capsys.readouterr()
    assert "is not defined" in CreatedFile;
    
    assert "'hello' is not defined" in captured.out;
    assert "no comma found !" in captured.out;
    assert "uncontrolled inputs :" in captured.out;
    assert "unsatisfied variables :" in captured.out;
    
