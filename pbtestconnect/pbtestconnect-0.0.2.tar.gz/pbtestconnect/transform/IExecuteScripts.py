from typing import BinaryIO


class IExecuteScripts:
    def execute(self, context: dict, inputStream: BinaryIO, outputStream: BinaryIO) -> None:
        """Interface for script execution. Any output should be written to outputStream.
        
        Keyword arguments:

        context - a dictionary containing Connect Transform contextual information.  
        inputStream - a file like binary stream. input data into your script must be
        read from this stream. 
        outputStream - a file like binary stream. output data from your script, if applicable,
        should be written to this stream.
        """
        pass




