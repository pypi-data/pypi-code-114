# Generated from CyanaMRParser.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("m\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2\3\2")
        buf.write("\7\2\35\n\2\f\2\16\2 \13\2\3\2\3\2\3\3\6\3%\n\3\r\3\16")
        buf.write("\3&\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\6\5\62\n\5\r\5")
        buf.write("\16\5\63\3\6\3\6\3\6\3\6\3\6\3\6\3\7\6\7=\n\7\r\7\16\7")
        buf.write(">\3\7\6\7B\n\7\r\7\16\7C\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\6\nW\n\n\r\n\16")
        buf.write("\nX\3\n\6\n\\\n\n\r\n\16\n]\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\2\2\r\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\2\2\2k\2\36\3\2\2\2\4$\3\2\2\2\6(\3\2\2\2")
        buf.write("\b\61\3\2\2\2\n\65\3\2\2\2\f<\3\2\2\2\16E\3\2\2\2\20J")
        buf.write("\3\2\2\2\22V\3\2\2\2\24_\3\2\2\2\26d\3\2\2\2\30\35\5\4")
        buf.write("\3\2\31\35\5\b\5\2\32\35\5\f\7\2\33\35\5\22\n\2\34\30")
        buf.write("\3\2\2\2\34\31\3\2\2\2\34\32\3\2\2\2\34\33\3\2\2\2\35")
        buf.write(" \3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2\37!\3\2\2\2 \36")
        buf.write("\3\2\2\2!\"\7\2\2\3\"\3\3\2\2\2#%\5\6\4\2$#\3\2\2\2%&")
        buf.write("\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'\5\3\2\2\2()\7\3\2\2)*")
        buf.write("\7\5\2\2*+\7\5\2\2+,\7\3\2\2,-\7\5\2\2-.\7\5\2\2./\7\4")
        buf.write("\2\2/\7\3\2\2\2\60\62\5\n\6\2\61\60\3\2\2\2\62\63\3\2")
        buf.write("\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\t\3\2\2\2\65\66\7")
        buf.write("\3\2\2\66\67\7\5\2\2\678\7\5\2\289\7\4\2\29:\7\4\2\2:")
        buf.write("\13\3\2\2\2;=\5\16\b\2<;\3\2\2\2=>\3\2\2\2><\3\2\2\2>")
        buf.write("?\3\2\2\2?A\3\2\2\2@B\5\20\t\2A@\3\2\2\2BC\3\2\2\2CA\3")
        buf.write("\2\2\2CD\3\2\2\2D\r\3\2\2\2EF\7\3\2\2FG\7\4\2\2GH\7\4")
        buf.write("\2\2HI\7\3\2\2I\17\3\2\2\2JK\7\3\2\2KL\7\5\2\2LM\7\5\2")
        buf.write("\2MN\7\3\2\2NO\7\5\2\2OP\7\5\2\2PQ\7\4\2\2QR\7\4\2\2R")
        buf.write("S\7\4\2\2ST\7\3\2\2T\21\3\2\2\2UW\5\24\13\2VU\3\2\2\2")
        buf.write("WX\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y[\3\2\2\2Z\\\5\26\f\2[")
        buf.write("Z\3\2\2\2\\]\3\2\2\2][\3\2\2\2]^\3\2\2\2^\23\3\2\2\2_")
        buf.write("`\7\3\2\2`a\7\4\2\2ab\7\4\2\2bc\7\3\2\2c\25\3\2\2\2de")
        buf.write("\7\3\2\2ef\7\5\2\2fg\7\5\2\2gh\7\4\2\2hi\7\4\2\2ij\7\4")
        buf.write("\2\2jk\7\3\2\2k\27\3\2\2\2\n\34\36&\63>CX]")
        return buf.getvalue()


class CyanaMRParser ( Parser ):

    grammarFileName = "CyanaMRParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "Integer", "Float", "Simple_name", "SPACE", 
                      "COMMENT", "LINE_COMMENT" ]

    RULE_cyana_mr = 0
    RULE_distance_restraints = 1
    RULE_distance_restraint = 2
    RULE_torsion_angle_restraints = 3
    RULE_torsion_angle_restraint = 4
    RULE_rdc_restraints = 5
    RULE_rdc_parameter = 6
    RULE_rdc_restraint = 7
    RULE_pcs_restraints = 8
    RULE_pcs_parameter = 9
    RULE_pcs_restraint = 10

    ruleNames =  [ "cyana_mr", "distance_restraints", "distance_restraint", 
                   "torsion_angle_restraints", "torsion_angle_restraint", 
                   "rdc_restraints", "rdc_parameter", "rdc_restraint", "pcs_restraints", 
                   "pcs_parameter", "pcs_restraint" ]

    EOF = Token.EOF
    Integer=1
    Float=2
    Simple_name=3
    SPACE=4
    COMMENT=5
    LINE_COMMENT=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Cyana_mrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CyanaMRParser.EOF, 0)

        def distance_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Distance_restraintsContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Distance_restraintsContext,i)


        def torsion_angle_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Torsion_angle_restraintsContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Torsion_angle_restraintsContext,i)


        def rdc_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Rdc_restraintsContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Rdc_restraintsContext,i)


        def pcs_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Pcs_restraintsContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Pcs_restraintsContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_cyana_mr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCyana_mr" ):
                listener.enterCyana_mr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCyana_mr" ):
                listener.exitCyana_mr(self)




    def cyana_mr(self):

        localctx = CyanaMRParser.Cyana_mrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_cyana_mr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CyanaMRParser.Integer:
                self.state = 26
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 22
                    self.distance_restraints()
                    pass

                elif la_ == 2:
                    self.state = 23
                    self.torsion_angle_restraints()
                    pass

                elif la_ == 3:
                    self.state = 24
                    self.rdc_restraints()
                    pass

                elif la_ == 4:
                    self.state = 25
                    self.pcs_restraints()
                    pass


                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 31
            self.match(CyanaMRParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Distance_restraintsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def distance_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Distance_restraintContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Distance_restraintContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_distance_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance_restraints" ):
                listener.enterDistance_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance_restraints" ):
                listener.exitDistance_restraints(self)




    def distance_restraints(self):

        localctx = CyanaMRParser.Distance_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_distance_restraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 33
                    self.distance_restraint()

                else:
                    raise NoViableAltException(self)
                self.state = 36 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Distance_restraintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Integer)
            else:
                return self.getToken(CyanaMRParser.Integer, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Simple_name)
            else:
                return self.getToken(CyanaMRParser.Simple_name, i)

        def Float(self):
            return self.getToken(CyanaMRParser.Float, 0)

        def getRuleIndex(self):
            return CyanaMRParser.RULE_distance_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance_restraint" ):
                listener.enterDistance_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance_restraint" ):
                listener.exitDistance_restraint(self)




    def distance_restraint(self):

        localctx = CyanaMRParser.Distance_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_distance_restraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(CyanaMRParser.Integer)
            self.state = 39
            self.match(CyanaMRParser.Simple_name)
            self.state = 40
            self.match(CyanaMRParser.Simple_name)
            self.state = 41
            self.match(CyanaMRParser.Integer)
            self.state = 42
            self.match(CyanaMRParser.Simple_name)
            self.state = 43
            self.match(CyanaMRParser.Simple_name)
            self.state = 44
            self.match(CyanaMRParser.Float)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Torsion_angle_restraintsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def torsion_angle_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Torsion_angle_restraintContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Torsion_angle_restraintContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_torsion_angle_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTorsion_angle_restraints" ):
                listener.enterTorsion_angle_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTorsion_angle_restraints" ):
                listener.exitTorsion_angle_restraints(self)




    def torsion_angle_restraints(self):

        localctx = CyanaMRParser.Torsion_angle_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_torsion_angle_restraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 46
                    self.torsion_angle_restraint()

                else:
                    raise NoViableAltException(self)
                self.state = 49 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Torsion_angle_restraintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self):
            return self.getToken(CyanaMRParser.Integer, 0)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Simple_name)
            else:
                return self.getToken(CyanaMRParser.Simple_name, i)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Float)
            else:
                return self.getToken(CyanaMRParser.Float, i)

        def getRuleIndex(self):
            return CyanaMRParser.RULE_torsion_angle_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTorsion_angle_restraint" ):
                listener.enterTorsion_angle_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTorsion_angle_restraint" ):
                listener.exitTorsion_angle_restraint(self)




    def torsion_angle_restraint(self):

        localctx = CyanaMRParser.Torsion_angle_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_torsion_angle_restraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(CyanaMRParser.Integer)
            self.state = 52
            self.match(CyanaMRParser.Simple_name)
            self.state = 53
            self.match(CyanaMRParser.Simple_name)
            self.state = 54
            self.match(CyanaMRParser.Float)
            self.state = 55
            self.match(CyanaMRParser.Float)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rdc_restraintsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rdc_parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Rdc_parameterContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Rdc_parameterContext,i)


        def rdc_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Rdc_restraintContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Rdc_restraintContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_rdc_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRdc_restraints" ):
                listener.enterRdc_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRdc_restraints" ):
                listener.exitRdc_restraints(self)




    def rdc_restraints(self):

        localctx = CyanaMRParser.Rdc_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_rdc_restraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 57
                    self.rdc_parameter()

                else:
                    raise NoViableAltException(self)
                self.state = 60 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 63 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 62
                    self.rdc_restraint()

                else:
                    raise NoViableAltException(self)
                self.state = 65 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rdc_parameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Integer)
            else:
                return self.getToken(CyanaMRParser.Integer, i)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Float)
            else:
                return self.getToken(CyanaMRParser.Float, i)

        def getRuleIndex(self):
            return CyanaMRParser.RULE_rdc_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRdc_parameter" ):
                listener.enterRdc_parameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRdc_parameter" ):
                listener.exitRdc_parameter(self)




    def rdc_parameter(self):

        localctx = CyanaMRParser.Rdc_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_rdc_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(CyanaMRParser.Integer)
            self.state = 68
            self.match(CyanaMRParser.Float)
            self.state = 69
            self.match(CyanaMRParser.Float)
            self.state = 70
            self.match(CyanaMRParser.Integer)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rdc_restraintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Integer)
            else:
                return self.getToken(CyanaMRParser.Integer, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Simple_name)
            else:
                return self.getToken(CyanaMRParser.Simple_name, i)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Float)
            else:
                return self.getToken(CyanaMRParser.Float, i)

        def getRuleIndex(self):
            return CyanaMRParser.RULE_rdc_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRdc_restraint" ):
                listener.enterRdc_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRdc_restraint" ):
                listener.exitRdc_restraint(self)




    def rdc_restraint(self):

        localctx = CyanaMRParser.Rdc_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_rdc_restraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(CyanaMRParser.Integer)
            self.state = 73
            self.match(CyanaMRParser.Simple_name)
            self.state = 74
            self.match(CyanaMRParser.Simple_name)
            self.state = 75
            self.match(CyanaMRParser.Integer)
            self.state = 76
            self.match(CyanaMRParser.Simple_name)
            self.state = 77
            self.match(CyanaMRParser.Simple_name)
            self.state = 78
            self.match(CyanaMRParser.Float)
            self.state = 79
            self.match(CyanaMRParser.Float)
            self.state = 80
            self.match(CyanaMRParser.Float)
            self.state = 81
            self.match(CyanaMRParser.Integer)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pcs_restraintsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pcs_parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Pcs_parameterContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Pcs_parameterContext,i)


        def pcs_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Pcs_restraintContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Pcs_restraintContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_pcs_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPcs_restraints" ):
                listener.enterPcs_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPcs_restraints" ):
                listener.exitPcs_restraints(self)




    def pcs_restraints(self):

        localctx = CyanaMRParser.Pcs_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_pcs_restraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 83
                    self.pcs_parameter()

                else:
                    raise NoViableAltException(self)
                self.state = 86 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 89 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 88
                    self.pcs_restraint()

                else:
                    raise NoViableAltException(self)
                self.state = 91 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pcs_parameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Integer)
            else:
                return self.getToken(CyanaMRParser.Integer, i)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Float)
            else:
                return self.getToken(CyanaMRParser.Float, i)

        def getRuleIndex(self):
            return CyanaMRParser.RULE_pcs_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPcs_parameter" ):
                listener.enterPcs_parameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPcs_parameter" ):
                listener.exitPcs_parameter(self)




    def pcs_parameter(self):

        localctx = CyanaMRParser.Pcs_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_pcs_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(CyanaMRParser.Integer)
            self.state = 94
            self.match(CyanaMRParser.Float)
            self.state = 95
            self.match(CyanaMRParser.Float)
            self.state = 96
            self.match(CyanaMRParser.Integer)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pcs_restraintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Integer)
            else:
                return self.getToken(CyanaMRParser.Integer, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Simple_name)
            else:
                return self.getToken(CyanaMRParser.Simple_name, i)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Float)
            else:
                return self.getToken(CyanaMRParser.Float, i)

        def getRuleIndex(self):
            return CyanaMRParser.RULE_pcs_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPcs_restraint" ):
                listener.enterPcs_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPcs_restraint" ):
                listener.exitPcs_restraint(self)




    def pcs_restraint(self):

        localctx = CyanaMRParser.Pcs_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_pcs_restraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(CyanaMRParser.Integer)
            self.state = 99
            self.match(CyanaMRParser.Simple_name)
            self.state = 100
            self.match(CyanaMRParser.Simple_name)
            self.state = 101
            self.match(CyanaMRParser.Float)
            self.state = 102
            self.match(CyanaMRParser.Float)
            self.state = 103
            self.match(CyanaMRParser.Float)
            self.state = 104
            self.match(CyanaMRParser.Integer)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





