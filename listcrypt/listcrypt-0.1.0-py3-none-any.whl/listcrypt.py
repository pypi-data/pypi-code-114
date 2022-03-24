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

    range_finder(data:str) -> tuple:
        Finds the closest and furthest out the data ranges depending on each characters integer equivalent.

    create_dictionary(key:str, method:str, character_range:tuple, key_segment_lengths=6) -> dict
        Uses 'bits' of your key to alter the order of a list of characters.
        That list is then converted to a dictionary for more efficient 
        character retrieval during encryption/decryption.        

    encrypt(key:'any data type', data:'any data type') -> dict
        Encrypts the data by changing each character through indexing a uniquely generated dictionary from the key
    
    decrypt(key:"any data type", data_dictionary:dict) -> "origional data"
        Decrypts the data by changing each character through indexing a uniquely generated dictionary from the key

    file_manager(key:str, path:str, method:str, encrypted_data=None, encrypted_file_path=None, metadata_removal=True, remove_old_file=True) -> bool or bytes
        Allows for easy encryption and decryption of files
'''


import hashlib
import ast



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



def range_finder(data:str) -> tuple:
    '''
    This function finds the closest and furthest out the data ranges depending on 
    each characters integer equivalent.

    :function:: range_finder(data:str) -> tuple

    Args:
        data (str): The data to be encrypted

    Returns:
        tuple: The lowest and highest integer in the data given

    '''

    #Puts each characters integer equivalent into a list, without repeats for the same characters
    the_range = [item for item in range(1114111) if chr(item) in data]

    low = min(the_range)
    high = max(the_range)

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
    
    create_dictionary(key:str, method:str, character_range:tuple, key_segment_lengths=6) -> dict

    Args:
        key (str): The password used to change the order of your dictionary

        method (str): 'encryption' and 'decryption' are the options, they determine
            the order of key:value pair in your dictionary

        character_range (tuple): Defines the range of characters to ensure
            they are all included in the list

        key_segment_lengths (int): Determines the size of each section of integers
            taken from the key

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

    # These two if statements determine the order of key:value in the dictionary
    if method.lower() == "encryption":
        encryption_dictionary = {new_list[count]:count for count in range(len(new_list))}
        return encryption_dictionary

    if method.lower() == "decryption":
        decryption_dictionary = dict(enumerate(new_list))
        return decryption_dictionary
    

def encrypt(key:'any data type', data:'any data type') -> dict:
    '''
    Encrypts the data by changing each character through indexing a uniquely generated dictionary from the key

    :function:: encrypt(key:'any data type', data:'any data type') -> dict

    Args:
        key (any data type):
            Used to create a unique dictionary for encrypting the data 
        data: (any data type):
            The data to be encrypted
        
    Returns:
        dict: The encrypted data, along with metadata for decrypting the data
    
    '''

    #Converts the keys data type to 'str'
    key = convert_data(key,key)[0]

    #Finds the origional type of the data to convert back to after decryption
    data,data_type = convert_data(key, data)
    exportable_data = {"type":data_type}

    #Puts a random string at the start of the data before encryption to verify no data corruption at decryption
    exportable_data["confirmation_data"] = "--&*(@!^#$--"
    data = exportable_data["confirmation_data"] + data

    #Finding the range of the data, for boundaries when creating the unique dicitonary
    character_range = range_finder(data)
    exportable_data["char_range"] = character_range
    
    #Creates a dicitonary unique to encryption based on the key and character_range
    dictionary = create_dictionary(key, "encryption", character_range)

    #Encrypts the data
    encrypted_data = "".join([chr(dictionary[item]) for item in data])

    #Encoding the data for easier copiability if copying the data in a raw format
    exportable_data["data"] = encrypted_data.encode()

    return exportable_data


def decrypt(key:"any data type", data_dictionary:dict) -> "origional data":
    '''
    Decrypts the data by changing each character through indexing a uniquely generated dictionary from the key

    :function:: decrypt(key:"any data type", data_dictionary:dict) -> "origional data"

    Args:
        key (any data type):
            Used to create a unique dictionary for encrypting the data 
        data_dictionary: (any data type):
            The dictionary holding the data and metadata required to decrypt the data

    Returns:
        The origional data
            
    '''


    #Converts the keys data type to 'str'
    key = convert_data(key,key)[0]

    #Converts the dicitionary to easier to read and use variables
    confirmation_data = data_dictionary["confirmation_data"]
    origional_data_type = data_dictionary["type"]
    character_range = data_dictionary["char_range"]
    data = data_dictionary["data"].decode()

    #Creates a dicitonary unique to decryption based on the key and character_range
    dictionary = create_dictionary(key, "decryption", character_range)

    #Decrypts the data
    decrypted_data = "".join([dictionary[ord(item)] for item in data])

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
            with open(encrypted_file_path, "w")as f:
                f.write(str(encrypted_data))

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
        if encrypted_file_path:
            with open(encrypted_file_path, "r")as file:
                encrypted_data = ast.literal_eval(file.read())
            

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
        file_name = "test.txt"
        key = "example key"
        method = "encryption"

        file_manager(key, file_name, method, encrypted_file_path="file")

    #Example use of the 'encrypt()' and 'decrypt()' functions
    if False:
        data = "This is example data"
        key = "example key"

        e = encrypt(key, data)
        d = decrypt(key, e)
        
