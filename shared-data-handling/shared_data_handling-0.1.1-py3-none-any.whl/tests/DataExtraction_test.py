import unittest
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")


from shared_data_handling.process_data import FindFiles, ParseFileBeginMidEndRegexPattern, ParseFileSingleRegexPattern, ParseFolder, ParseFolderRegexPatternList

class TestSingleStringPattern(unittest.TestCase):

    def testFindFiles(self):
        data = FindFiles('./tests/testdata')
        self.assertGreaterEqual(len(data),0)

    def testFolderDoesnotExist(self):
        with self.assertRaises(Exception) as context:
            data = ParseFolder(
                rootdir = "bla",
                regexPatternAsVerboseString = r"""test\sstring (?P<Test>.*)""",
                firstMatchOnly=False)
        
        self.assertTrue('File or Folder not expected to exist', context.exception)

    def testParseFileSingleRegexPatternFirstMatchOnly(self):
        data = ParseFileSingleRegexPattern(
            fullFilePath="./tests/testdata/normalCases/syslog",
            regexPatternAsVerboseString=r"""(?P<Tests>.*)""",
            firstMatchOnly=True,
            verboseTracing=False)
        self.assertEqual(len(data),1)
        
    def testParseFileSingleRegexPatternMultipleMatches(self):
        data = ParseFileSingleRegexPattern(
            fullFilePath="./tests/testdata/normalCases/syslog",
            regexPatternAsVerboseString=r"""(?P<Tests>.*)""",
            firstMatchOnly=False,
            verboseTracing=False)
        self.assertGreater(len(data),1)

    def testParseFileBeginMidEndRegexPatternFirstMatchOnlyWithMultipleMiddles(self):
        data = ParseFileBeginMidEndRegexPattern(
            fullFilePath="./tests/testdata/encapsulation/syslog",
            regexPatternAsVerboseStringBegin= r"""(?P<FirstEntry>first)""",
            regexPatternAsVerboseListMiddle=[r"""(?P<MiddleEntry>middle)"""],
            regexPatternAsVerboseStringEnd=r"""(?P<LastEntry>last)""",
            firstMatchOnly=False,
            verboseTracing=True)
        print(data)
        self.assertIsNotNone(data[0]['MiddleEntry_0'])
        self.assertIsNotNone(data[0]['MiddleEntry_1'])
        self.assertEqual(len(data),1)

    def testParseFileBeginMidEndRegexPatternFirstMatchOnlyWithSingleMiddle(self):
        data = ParseFileBeginMidEndRegexPattern(
            fullFilePath="./tests/testdata/encapsulation/syslog",
            regexPatternAsVerboseStringBegin= r"""(?P<FirstEntry>first)""",
            regexPatternAsVerboseListMiddle=[r"""(?P<MiddleEntry>middle2)"""],
            regexPatternAsVerboseStringEnd=r"""(?P<LastEntry>last)""",
            firstMatchOnly=False,
            verboseTracing=False)
        print(data)
        self.assertIsNotNone(data[0]['MiddleEntry_0'])
        #Dictionary MiddleEntry_1 must not exists
        with self.assertRaises(KeyError) as cm:
            data[0]['MiddleEntry_1']
        self.assertEqual(len(data),1)

    def test_pattern(self):
        data = ParseFolder(
            rootdir = "./tests/testdata",
            regexPatternAsVerboseString = r"""test(?P<Test>.*)""",
            firstMatchOnly=False)
        self.assertGreaterEqual(len(data), 1, "Single entry in dictionary")

    def testFirstResultReturnOnly(self):
        data = ParseFolder(
            rootdir = "./tests/testdata/firstOccuranceOnly",
            regexPatternAsVerboseString = r"""test (?P<Test>.*)""",
            firstMatchOnly=True)
        self.assertEqual(len(data), 1, "Single entry in dictionary")

class TestMultiStringListPattern(unittest.TestCase):
    def test_pattern(self):
        data = ParseFolderRegexPatternList(
            rootdir = "./tests/testdata/normalCases",
            regexPatternAsVerboseStringList = [r"""test\sstring (?P<Test1>.*)""", 
                                            r"""test (?P<Test2>.*)"""],
            firstMatchOnly=False)
        self.assertEqual(len(data), 2, "Single entry in dictionary")
        self.assertEqual(len(data[0]), 3, "Two duplicate entries and a single match")
