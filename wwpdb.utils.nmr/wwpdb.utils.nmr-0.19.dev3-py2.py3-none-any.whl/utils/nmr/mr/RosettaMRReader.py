##
# RosettaMRReader.py
#
# Update:
##
""" A collection of classes for parsing ROSETTA MR files.
"""
import sys
import os

from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker

try:
    from wwpdb.utils.nmr.mr.LexerErrorListener import LexerErrorListener
    from wwpdb.utils.nmr.mr.ParserErrorListener import ParserErrorListener
    from wwpdb.utils.nmr.mr.RosettaMRLexer import RosettaMRLexer
    from wwpdb.utils.nmr.mr.RosettaMRParser import RosettaMRParser
    from wwpdb.utils.nmr.mr.RosettaMRParserListener import RosettaMRParserListener
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (checkCoordinates,
                                                       REPRESENTATIVE_MODEL_ID)
    from wwpdb.utils.nmr.io.CifReader import CifReader
    from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
    from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from wwpdb.utils.nmr.NEFTranslator.NEFTranslator import NEFTranslator
except ImportError:
    from nmr.mr.LexerErrorListener import LexerErrorListener
    from nmr.mr.ParserErrorListener import ParserErrorListener
    from nmr.mr.RosettaMRLexer import RosettaMRLexer
    from nmr.mr.RosettaMRParser import RosettaMRParser
    from nmr.mr.RosettaMRParserListener import RosettaMRParserListener
    from nmr.mr.ParserListenerUtil import (checkCoordinates,
                                           REPRESENTATIVE_MODEL_ID)
    from nmr.io.CifReader import CifReader
    from nmr.ChemCompUtil import ChemCompUtil
    from nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from nmr.NEFTranslator.NEFTranslator import NEFTranslator


class RosettaMRReader:
    """ Accessor methods for parsing ROSETTA MR files.
    """

    def __init__(self, verbose=True, log=sys.stdout, cR=None, polySeqModel=None,
                 representativeModelId=REPRESENTATIVE_MODEL_ID,
                 coordAtomSite=None, coordUnobsRes=None,
                 labelToAuthSeq=None, authToLabelSeq=None,
                 ccU=None, csStat=None, nefT=None):
        self.__verbose = verbose
        self.__lfh = log

        self.__representativeModelId = representativeModelId

        if cR is not None and polySeqModel is None:
            ret = checkCoordinates(verbose, log, cR, polySeqModel,
                                   representativeModelId,
                                   testTag=False)
            polySeqModel = ret['polymer_sequence']

        self.__cR = cR
        self.__polySeqModel = polySeqModel
        self.__coordAtomSite = coordAtomSite
        self.__coordUnobsRes = coordUnobsRes
        self.__labelToAuthSeq = labelToAuthSeq
        self.__authToLabelSeq = authToLabelSeq

        # CCD accessing utility
        self.__ccU = ChemCompUtil(verbose, log) if ccU is None else ccU

        # BMRB chemical shift statistics
        self.__csStat = BMRBChemShiftStat(verbose, log, self.__ccU) if csStat is None else csStat

        # NEFTranslator
        self.__nefT = NEFTranslator(verbose, log, self.__ccU, self.__csStat) if nefT is None else nefT

    def parse(self, mrFilePath, cifFilePath=None):
        """ Parse ROSETTA MR file.
            @return: RosettaMRParserListener for success or None otherwise, ParserErrorListener, LexerErrorListener.
        """

        try:

            if not os.access(mrFilePath, os.R_OK):
                if self.__verbose:
                    self.__lfh.write(f"RosettaMRReader.parse() {mrFilePath} is not accessible.\n")
                return None, None, None

            if cifFilePath is not None:
                if not os.access(cifFilePath, os.R_OK):
                    if self.__verbose:
                        self.__lfh.write(f"RosettaMRReader.parse() {cifFilePath} is not accessible.\n")
                    return None, None, None

                if self.__cR is None:
                    self.__cR = CifReader(self.__verbose, self.__lfh)
                    if not self.__cR.parse(cifFilePath):
                        return None, None, None

            with open(mrFilePath) as ifp:

                ifs = InputStream(ifp.read())

                lexer = RosettaMRLexer(ifs)
                lexer.removeErrorListeners()

                lexer_error_listener = LexerErrorListener(mrFilePath)
                lexer.addErrorListener(lexer_error_listener)

                messageList = lexer_error_listener.getMessageList()

                if messageList is not None and self.__verbose:
                    for description in messageList:
                        self.__lfh.write(f"[Syntax error] line {description['line_number']}:{description['column_position']} {description['message']}\n")
                        if 'input' in description:
                            self.__lfh.write(f"{description['input']}\n")
                            self.__lfh.write(f"{description['marker']}\n")

                stream = CommonTokenStream(lexer)
                parser = RosettaMRParser(stream)
                parser.removeErrorListeners()
                parser_error_listener = ParserErrorListener(mrFilePath)
                parser.addErrorListener(parser_error_listener)
                tree = parser.rosetta_mr()

                walker = ParseTreeWalker()
                listener = RosettaMRParserListener(self.__verbose, self.__lfh, self.__cR, self.__polySeqModel,
                                                   self.__representativeModelId,
                                                   self.__coordAtomSite, self.__coordUnobsRes,
                                                   self.__labelToAuthSeq, self.__authToLabelSeq,
                                                   self.__ccU, self.__csStat, self.__nefT)
                walker.walk(listener, tree)

                messageList = parser_error_listener.getMessageList()

                if messageList is not None and self.__verbose:
                    for description in messageList:
                        self.__lfh.write(f"[Syntax error] line {description['line_number']}:{description['column_position']} {description['message']}\n")
                        if 'input' in description:
                            self.__lfh.write(f"{description['input']}\n")
                            self.__lfh.write(f"{description['marker']}\n")

                if self.__verbose:
                    if listener.warningMessage is not None:
                        print(listener.warningMessage)
                    print(listener.getContentSubtype())

            return listener, parser_error_listener, lexer_error_listener

        except IOError as e:
            if self.__verbose:
                self.__lfh.write(f"+RosettaMRReader.parse() ++ Error - {str(e)}\n")
            return None, None, None


if __name__ == "__main__":
    reader = RosettaMRReader(True)
    reader.parse('../../tests-nmr/mock-data-daother-7690/rosetta_rdc.test',
                 '../../tests-nmr/mock-data-daother-7690/D_800470_model_P1.cif.V4')
    # reader = RosettaMRReader(True)
    # reader.parse('../../tests-nmr/mock-data-daother-7690/rosetta_angle.test',
    #              '../../tests-nmr/mock-data-daother-7690/D_800470_model_P1.cif.V4')
    # reader = RosettaMRReader(True)
    # reader.parse('../../tests-nmr/mock-data-daother-7690/rosetta_dist.test',
    #              '../../tests-nmr/mock-data-daother-7690/D_800470_model_P1.cif.V4')
