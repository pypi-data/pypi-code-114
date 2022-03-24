'''
Cryptographic module that alters the order of a list of characters with a key
to use for indexing against the built in 'ord()' and 'chr()' functions. The list
can only be put in that order with  a single key, making it a cryptographicaly 
secure method of encrypting sensitive data.


Functions:
    hash(data: str) -> str:
        Simple hashing function, utilizes the builtin hashlib module

    data_verification(key:str, data:str) -> bool:
        Verifies that your data will be encrypted and decrypted without error

    convert_data(key:str, data:'any data type') -> str and str:
        Converts the data to a string format to allow for encryption

    range_finder(data:str, processes=cpu_count()) -> tuple
        Finds the closest and furthest out the data ranges depending on each characters integer equivalent.
    
        Nested Function:
            append_character_range(current_segment:int, character_range:list) -> bool            
                Appends unique characters in the data to the shared 'character_range' list

    create_dictionary(key:str, method:str, character_range:tuple, key_segment_lengths=6) -> dict
        Uses 'bits' of your key to alter the order of a list of characters.
        That list is then converted to a dictionary for more efficient 
        character retrieval during encryption/decryption.        

    segment_data(data:str, segments:int) -> list
        Splits the data evenly amongst the amount of 'segments' required        

    pull_metadata(data:bytes) -> dict
        Pulls metadata from the encrypted bytes and puts it in a dictionary for easy readibility and manipulation

    encrypt(key:'any data type', data:'any data type', processes=cpu_count()) -> bytes    
        Encrypts the data by changing each character through indexing a uniquely generated dictionary from the key
        
        Nested Function:
            multiprocess_decryption(data:str, segment:int, shared_dictionary:dict) -> bool
                Takes chuncks of data and adds them to a shared dictionary,
                with the keys being the segments origional position for concatenation
                after encryption            
        
    decrypt(key:"any data type", encrypted_data:bytes, processes=cpu_count()) -> "origional data"
        Decrypts the data by changing each character through indexing a uniquely generated dictionary from the key
        
        Nested_Function:
            multiprocess_encryption(data:str, segment:int, shared_dictionary:dict) -> bool
                Takes chuncks of data and adds them to a shared dictionary,
                with the keys being the segments origional position for concatenation
                after decryption


    file_manager(key:str, path:str, method:str, encrypted_data=None, encrypted_file_path=None, metadata_removal=True, remove_old_file=True) -> bool or bytes
        Allows for easy encryption and decryption of files
'''


import hashlib
import ast
from multiprocessing import Process, Manager, cpu_count
import math


def hash(data) -> str:
    '''
    Returns the Hashed Value of your data

    :function:: hash(data:str) -> str

    Args:
        data (str): Any String Value Will Work

    Returns:
        str: The Hashed Value of The Data
    '''
    return hashlib.sha256(data.encode()).hexdigest()


def data_verification(key:str, data:str) -> bool:
    '''
    Verifies the data will be encrypted and decrypted without error by testing a small chunck
    of said data, returning true if the origional chunk of data matches the decrypted version
    of the same data

    Args:
        key (str):
            The key used to encrypt the data

        data (str or bytes):
            The data that will be encrypted

    Returns:
        bool:
            This will return true if the data was encrypted and decrypted without error, otherwise
            it will return False
    '''

    #Finds the center of the data and takes the following ten characters to encrypt/decrypt
    size = len(data)/2
    sample_data = data[round(size):round(size+10)]

    encrypted_data = encrypt(key, sample_data)

    decrypted_data = decrypt(key, encrypted_data)

    #Returns true if the origional chunck of data matches the decrypted version of the data
    return sample_data == decrypted_data


def convert_data(key:str, data:'any data type') -> str and str:
    '''
    Converts the data to a string format to allow for encryption

    :function:: data_converter(key:str, data:'any data type') -> str and str

    Args:
        key (str):
            The key used to encrypt the data

        data ('any data type'):
            The data that will be encrypted

    Returns:
        str:
            The string version of the supplied data
        str:
            The origional format of the converted data
    '''

    #This block of code converts the data to a str, no matter the origional type
    if type(data) == str:
        return data, 'str'
    if type(data) == bytes:
        try:
            data = data.decode('utf-8')
            if data_verification(key, data) and type(data) == str:
                return data, 'utf-8'
        except Exception:
            try:
                data = data.decode('ISO-8859-1')
                if data_verification(key, data) and type(data) == str:
                    return data, 'ISO-8859-1'
            except Exception:
                #Common way of decoding certain image files
                import base64
                data = (base64.b64encode(data.read())).decode()
                if data_verification(key, data) and type(data) == str:
                    return data, 'base64'
    if type(data) != str or bytes:
        return str(data), 'ast'



def range_finder(data:str, processes=cpu_count()) -> tuple:
    '''
    This function finds the closest and furthest out the data ranges depending on each characters integer equivalent.

    :function:: range_finder(data:str) -> tuple

    Args:
        data (str): 
            The data to be encrypted
        processes (int, preset:All available CPU cores):
            The amount of processes allowed to run simultaneously, the more allowed,
            the faster the decryption

    Returns:
        tuple: The lowest and highest integer in the data given

    '''

    #Puts each characters integer equivalent into a list, without repeats for the same characters
    total_characters = 1114111

    #More data then 'total_characters', so it's faster to check if each character is in the data
    if len(data) > total_characters:
        #Creates a dictionary that is shared across independent processes 
        character_range = Manager().list()

        #The amount of cores on your CPU allowed to work simultaneously
        cores = processes
    
        #Divides the 'total_characters' variable into even segments
        segment_length = round(total_characters/cores)
        #Finds the exact amount left over from rounding the divison of total characters
        left_over = (total_characters-segment_length*(cores-1))+1
    

        def append_character_range(current_segment:int, character_range:list) -> bool:
            '''
            Appends unique characters in the data to the shared 'character_range' list

            :function:: append_character_range(current_segment:int, character_range:list) -> bool

            Args:
                current_segment (int):
                    The current segment of 'total_characters' that is being checked
                character_range (list):
                    Special list created by 'multiprocessing.Manager()' to be shared across
                    multiple independent processes

            Returns:
                bool: True if the function runs successfully, otherwise Error
            '''
            #Checks wether any characters in the current segment of 'total_characters' are unique to the rest of the data
            new_range = [item for item in range(current_segment-segment_length,current_segment) if chr(item) in data]
            #Add them to the 'characte_range' list if they're unique to the data
            character_range += new_range

            return True

        #Created to hold all the process objects, to check whether they have finished their tasks
        still_alive = []

        #Starts the multiple process on the 'append_character_range' function, and adds each process object to the still alive list
        for current_segment in range(segment_length,segment_length*(cores-1),segment_length):
            p = Process(target=append_character_range, args=(current_segment, character_range))
            p.start()
            still_alive.append(p)

        #Runs the first segment on the main process
        append_character_range(left_over, character_range)

        #Waits until all processes finish their tasks
        while still_alive:
            removal = [item for item in still_alive if not item.is_alive()]
            [still_alive.remove(item) for item in removal]

    #Less data than total printable characters, so its faster to just add all the data to the list
    else:
        character_range = [ord(char) for char in data]

    low = min(character_range)
    high = max(character_range)

    #Ensures a more secure dataset by spreading out the possible encrypted characters to atleast a range of 100
    if high-low < 100:
        current = high-low
        add = int((100-current)/2)
        if low-add < 0:
            add *= 2
            add -= low
            low -= low
        else:
            low -= add
        high += add
        
    return (low, high)


def create_dictionary(key:str, method:str, character_range:tuple, key_segment_lengths=6) -> dict:
    '''
    Uses 'bits' of your key to alter the order of a list of characters.
    That list is then converted to a dictionary for more efficient 
    character retrieval during encryption/decryption.
    
    :function:: create_dictionary(key:str, method:str, character_range:tuple, key_segment_lengths=6) -> dict

    Args:
        key (str):
            The password used to change the order of your dictionary

        method (str):
            'encryption' and 'decryption' are the options, they determine the 
            order of key:value pair in your dictionary

        character_range (tuple):
            Defines the range of characters to ensure they are all included in the list

        key_segment_lengths (int):
            Determines the size of each section of integers taken from the key

    Returns:
        dict: The dictionary used for encrypting the data    

    '''

    #Hash the key and convert it to an integer
    key = hash(key)
    key = "".join([str(ord(char)) for char in key])

    #Split the key into sections and appends each to a list
    key_bits = [int(key[segment:segment+key_segment_lengths]) for segment in range(0, len(key), key_segment_lengths)]

    #Puts all the characters within the range of the required characters from the data in a list
    old_list = [chr(item) for item in range(character_range[0],character_range[1]+1)]

    new_list = []

    #Takes the groups of bits from the key integer and uses them
    #to randomize the order of the characters in a list
    while old_list:
        for integer,item in zip(key_bits,old_list):
            prior_bit = key_bits[key_bits.index(integer)-1]
            new_list.insert(integer-prior_bit, item)
            old_list.remove(item)

    # These two if statements determine the order of the key:value pair in the dictionary
    if method.lower() == "encryption":
        encryption_dictionary = {new_list[count]:count for count in range(len(new_list))}
        return encryption_dictionary

    if method.lower() == "decryption":
        decryption_dictionary = dict(enumerate(new_list))
        return decryption_dictionary
  

def segment_data(data:str, segments:int) -> list:
    '''
    Splits the data evenly amongst the amount of 'segments' required

    :function:: segment_data(data:str, segments:int) -> list

    Args:
        data (str):
            The data to evenly split
        segments (int):
            The amount of splits you want in the data

    Returns:
        list: A list of evenly distributed items from the data
    '''
    #Finds the approximate len each segment should be 
    segment_lengths = math.ceil(len(data)/segments)

    #Splits the data into segments
    segmented_data = [data[size:size+segment_lengths] for size in range(0,segment_lengths*segments,segment_lengths)]

    return segmented_data


def pull_metadata(data:bytes) -> dict:
    '''
    Pulls metadata from the encrypted bytes and puts it in a dictionary for easy readibility and manipulation

    :function:: pull_metadata(data:bytes) -> dict

    Args:
        data (bytes):
            The ouput of running the enryption function

    Returns:
        dict: A dictionary of the metadata and encrypted data
    '''
    data = data.decode()

    metadata_dictionary = {}

    #Pulling metadata from the encrypted data and transfering to dictonary
    metadata_dictionary["type"] = data[:data.index("(")]
    data = data[data.index("(")+1:]

    metadata_dictionary["range"] = ast.literal_eval(data[:data.index(")")])
    data = data[data.index(")")+1:]

    metadata_dictionary["data"] = data

    return metadata_dictionary


def encrypt(key:'any data type', data:'any data type', processes=cpu_count()) -> bytes:
    '''
    Encrypts the data by changing each character through indexing a uniquely generated dictionary from the key

    :function:: encrypt(key:'any data type', data:'any data type') -> dict

    Args:
        key (any data type):
            Used to create a unique dictionary for encrypting the data 
        data (any data type):
            The data to be encrypted
        processes (int, preset:All available CPU cores):
            The amount of processes allowed to run simultaneously, the more allowed,
            the faster the decryption

    Returns:
        bytes: The encrypted data, along with metadata for decrypting the data
    
    '''
    #Converts the keys data type to 'str'
    key = convert_data(key,key)[0]

    #Finds the origional type of the data to convert back to after decryption
    data,data_type = convert_data(key, data)
    metadata = data_type

    #Puts a random string at the start of the data before encryption to verify no data corruption during decryption
    confirmation_data = "39"
    data = confirmation_data+data

    #Finding the range of the data, for boundaries when creating the unique dicitonary
    character_range = range_finder(data)
    metadata += f"({character_range[0]},{character_range[1]})"

    #Creates a dicitonary unique to encryption based on the key and character_range
    dictionary = create_dictionary(key, "encryption", character_range)
    
    #Creates a dictionary that is shared across independent processes
    shared_dictionary = Manager().dict()

    #Splits the data into segments for even distribution across CPU cores
    segments = processes
    segmented_data = segment_data(data, segments)
    
    #Leaving out the first segment for the main process to run after it starts the child processes
    child_segmented_data = segmented_data[1:]

    def multiprocess_encryption(data:str, segment:int, shared_dictionary:dict) -> bool:
        '''
        Takes chuncks of data and adds them to a shared dictionary,
        with the keys being the segments origional position for concatenation
        after encryption

        :function:: multiprocess_encryption(data:str, segment:int, shared_dictionary:dict) -> bool

        Args:
            data (str):
                The string of data to be encrypted
            segment (int):
                The origional location of the data in the list variable 'segmented_data',
                so it can be concatenated back into the correct order from the dictionary
            shared_dictionary (dict):
                Special dictionary created by 'multiprocessing.Manager()' to be shared across
                multiple independent processes

        Returns:
            bool: True if the function runs successfully, otherwise Error
        '''
        #Encrypts the data
        encrypted_data = "".join([chr(dictionary[item]) for item in data])
        #Adds the data to the shared_dictionary
        shared_dictionary[segment] = encrypted_data

        return True

    #Starting multiple process for the 'multiprocess_encryption' function
    for data_segment,process in zip(child_segmented_data, range(1,segments)):
        Process(target=multiprocess_encryption, args=(data_segment, process, shared_dictionary)).start()

    #Encrypts the first segment of data with the main process
    multiprocess_encryption(segmented_data[:1][0], 0, shared_dictionary)

    #Waits until all processes have finished and terminated
    while len(shared_dictionary) != segments:
        continue

    #Adds the confirmation string to the data
    encrypted_data = "".join([shared_dictionary[count] for count in range(segments)])

    #Encoding the data for easier copiability if copying the data in a raw format
    metadata = (metadata+encrypted_data).encode()
    
    return metadata


def decrypt(key:"any data type", encrypted_data:bytes, processes=cpu_count()) -> "origional data":
    '''
    Decrypts the data by changing each character through indexing a uniquely generated dictionary from the key

    :function:: decrypt(key:"any data type", encrypted_data:bytes, processes=cpu_count()) -> "origional data type"

    Args:
        key (any data type):
            Used to create a unique dictionary for encrypting the data 
        encrypted_data (bytes):
            The encrypted bytes returned by the 'encrypt' function
        processes (int, preset:All available CPU cores):
            The amount of processes allowed to run simultaneously, the more allowed,
            the faster the decryption

    Returns:
        The origional data
            
    '''


    #Converts the keys data type to 'str'
    key = convert_data(key,key)[0]

    #Converts the dictionary to variables for manipulation
    confirmation_data = "39" #Can be any random string of your choice. I recommend never changing it
    metadata_dictionary = pull_metadata(encrypted_data)
    origional_data_type = metadata_dictionary["type"]
    character_range = metadata_dictionary["range"]
    data = metadata_dictionary["data"]

    #Creates a dicitonary unique to decryption based on the key and character_range
    dictionary = create_dictionary(key, "decryption", character_range)

    #Creates a dictionary that is shared across independent processes
    shared_dictionary = Manager().dict()

    #Splits the data into segments for even distribution across cpu cores
    segments = processes
    segmented_data = segment_data(data, segments)

    #Leaving out the first segment for the main process to run after it starts the child processes
    child_segmented_data = segmented_data[1:]

    def multiprocess_decryption(data:str, segment:int, shared_dictionary:dict) -> bool:
        '''
        Takes chuncks of data and adds them to a shared dictionary,
        with the keys being the segments origional position for concatenation
        after encryption

        :function:: multiprocess_decryption(data:str, segment:int, shared_dictionary:dict) -> bool

        Args:
            data (str):
                The string of data to be decrypted
            segment (int):
                The origional location of the data in the list variable 'segmented_data',
                so it can be concatenated back into the correct order from the dictionary
            shared_dictionary (dict):
                Special dictionary created by 'multiprocessing.Manager()' to be shared across
                multiple independent processes

        Returns:
            bool: True if the function runs successfully, otherwise Error
        '''

        #Decrypts the data
        decrypted_data = "".join([dictionary[ord(item)] for item in data])
        #Adds the data to the shared_dictionary
        shared_dictionary[segment] = decrypted_data

    #Starting multiple process for the 'multiprocess_decryption' function
    for data_segment,process in zip(child_segmented_data, range(1,segments)):
        Process(target=multiprocess_decryption, args=(data_segment, process, shared_dictionary)).start()

    #Encrypts the first segment of data with the main process
    multiprocess_decryption(segmented_data[:1][0], 0, shared_dictionary)
    
    #Waits until all processes have finished and terminated
    while len(shared_dictionary) != segments:
        continue

    #Concatenating the data from the shared dictionary, into one string
    decrypted_data = "".join([shared_dictionary[count] for count in range(segments)])

    #Pulls confirmation text from data to verify successful decryption
    pulled_confirmation = decrypted_data[:len(confirmation_data)]

    #If True the origional data is returned, otherwise the function returns False
    if pulled_confirmation == confirmation_data:
        decrypted_data = decrypted_data[len(confirmation_data):]

        #Converting data back to origional type
        if origional_data_type == 'str':
            return decrypted_data
        if origional_data_type == 'ast':
            return ast.literal_eval(decrypted_data)
        if origional_data_type != 'base64':
            return decrypted_data.encode(origional_data_type)
        if origional_data_type == 'base64':
            return base64.decodebytes(decrypted_data)

        return decrypted_data
    
    else:
        return False


def file_manager(key:str, path:str, method:str, encrypted_data=None, encrypted_file_path=None, metadata_removal=True, remove_old_file=True) -> bool or bytes:
    '''
    This function allows for easy encryption and decryption of files

    :function:: file_manager(key:str, path:str, method:str, encrypted_data=None, encrypted_file_path=None, metadata_removal=True, remove_old_file=True) -> bool or bytes

    Args:
        key (str):
            The key used for the encryption and decryption of the file

        path (str):
            The path to the file is to be encrypted when using the encryption method, the path to the
            new location of the decrypted file when using the decryption method

        method (str):
            Can either be in 'encryption' or 'decryption' mode

        encrypted_data (bytes, *optional):
            Use this option when you encrypted a file and stored it in a database instead of
            just in a path on your machine

        encrypted_file_path (str, *optional):
            In encryption mode, specifiy the path to which
            you want to the encrypted file to be stored, if this argument is not used in encryption
            mode, the data will be returned by the function. In 'decryption' mode, the path to the
            already encrypted file path should be specified, to allow the program to open and read
            said file

        metadata_removal (bool, preset:'True'):
            Removes metadata from image files to reduce the size of the file, this doesn't affect
            the quality of the image

        remove_old_file (bool, preset:'True'):
            When set to True, this will delete either the old decrypted file after it decrypts successfully,
            or the origional file after it encrypts successfully. This isn't necessary if you use the same
            path and file name for both 'path' and 'encrypted_file_path'

    Returns:
        bool:
            This is returned by the 'decryption' method if the file or data is decrypted successfully
            and it is written to a new file path

        bytes:
            Returned by the 'encryption' method when an encrypted file path is not specified.
            This is the encrypted version of the file specified in the 'path' argument


    '''
    method = method.lower()

    if method == "encryption" or method == "e":
        #Attempts to remove meta data from images to reduce storage size
        if metadata_removal:
            try:
                from PIL import Image
                image = Image.open(path)
                data = list(image.getdata())
                image_without_exif = Image.new(image.mode, image.size)
                image_without_exif.putdata(data)
                image_without_exif.save(path)
            except:
                pass

        # Allows for opening both string and byte files without issue
        try:
            with open(path, "r")as file:
                encrypted_file = file.read()
        except:
            with open(path, "rb")as file:
                encrypted_file = file.read()

        encrypted_data = encrypt(key, encrypted_file)
        

        # Returns the encrypted data if a file path is not supplied
        if encrypted_file_path:
            with open(encrypted_file_path, "wb")as f:
                f.write(encrypted_data)

            #Removes origional file
            if remove_old_file and path != encrypted_file_path:
                import os
                try:
                    os.remove(path)
                except Exception:
                    print(f"Failed to remove path: '{path}'")
            return True
        else:
            return encrypted_data

    if method == "decryption" or method == "d":
        if encrypted_file_path and not encrypted_data:
            with open(encrypted_file_path, "rb")as file:
                encrypted_data = file.read()
        else:
            raise TypeError("Missing required argument 'encrypted_file_path' or 'encrypted_data'")

        decrypted_data = decrypt(key, encrypted_data)

        #Returns False if decryption process fails
        if not decrypted_data:
            return False

        # Allows for opening both string and byte files without issue
        if type(decrypted_data) == str:
            with open(path, "w")as file:
                file.write(decrypted_data)
        if type(decrypted_data) == bytes:
            with open(path, "wb")as file:
                file.write(decrypted_data)

        #Removes encrypted file
        if remove_old_file and path != encrypted_file_path:
            import os
            try:
                os.remove(encrypted_file_path)
            except Exception:
                print(f"Failed to remove path: '{encrypted_file_path}'")

        return True


if __name__=="__main__":
    #Example use of the 'file_manager()' function
    if False:
        file_name = "file.txt"
        key = "example key"
        method = "encryption"

        file_manager(key, file_name, method, encrypted_file_path="file")

    #Example use of the 'encrypt()' and 'decrypt()' functions
    if False:
        data = "example data"
        key = "example key"

        e = encrypt(key, data)
        d = decrypt(key, e)
