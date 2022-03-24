# You will probably have to often manipulate data, saving them and loading them to/from a text file (json).
# Imagine you want to save your favourite "MyDevice" class:

# class MyDevice:
#     def __init__(self, length, height):
#         self.length = length
#         self.height = height
#         self.surface = self.length * self.height

# In optimeed, there is an easy automated way to convert the object to json.
# All you need to do is using "typehint", as shown in this tutorial.

from optimeed.core import json_to_obj, obj_to_json  # The imports that will convert the python object to text
from json import dumps, loads


class MyDevice:
    length: float  # length is now an attribute to be saved because we have type hinted it
    height: float  # height is now an attribute to be saved
    # surface will not be saved because it is not type hinted

    def __init__(self, length: float, height: float):  # We also need to typehint that, otherwise errors might occur (try it :p )
        self.length = length
        self.height = height
        self.surface = self.length * self.height

    def __str__(self):
        return "length: {} height: {} surface: {}".format(self.length, self.height, self.surface)


if __name__ == "__main__":
    theDevice = MyDevice(5, 5)
    print("Device: ", theDevice)
    device_as_dictionary = obj_to_json(theDevice)  # We have converted the object "theDevice" to a dictionary
    print("Device to dictionary: ", device_as_dictionary)
    dictionary_as_string = dumps(device_as_dictionary)  # Which we can directly be exported as string by using the in-built json library :)
    print("Dictionary to string: ", dictionary_as_string)

    # Now we can revert the operation
    dictionary_from_string = loads(dictionary_as_string)  # Now we convert a string to a dictionary
    print("Dictionary from string: ", dictionary_from_string)
    device_from_dictionary = json_to_obj(dictionary_from_string)  # And a dictionary to a Device
    print("Device from dictionary: ", device_from_dictionary)

# As you can see, everything seems good, we retrieved the original device ... Except for the surface (that was not typehinted) !
# Saving/loading data is always something sensitive, especially when dealing with python object.
# Optimeed simplify the life by doing it automatically if it is type hinted.
# So, be sure to have type hinted all the necessary data.

# You can also typeHint more complicate data (like myVar: Dict[str, float] if myVar is a dictionary where the keys are strings and the values are float ... or your own type ;))
# If you do not know the type by advance, you can use the class "SaveableObject", as shown on wiki.
