import re, json
import process_data

dataPatterns = [r"""Hardware\semergency\sreport""",
                r"""CameraCommunicationError""",
                r"""DrawerLockFailed"""]
                #Add Retries

def ParseFile(fullFilePath):
    '''
    gets the matching regex patterns and keeps them in a list
    '''
    return process_data.ParseFileRegexPatternList(fullFilePath, dataPatterns, completeOnlyLine=True)