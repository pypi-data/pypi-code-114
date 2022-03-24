# It seems that data are annoying to export ...
# How about exporting a set of data, to a file???
# How about loading it back ???
# Actually ... it is easier ;) Optimeed provides high-level class to do so, using the objects defined in optimeed.core.collection

from optimeed.core import ListDataStruct  # We already know this class


class MyDevice:
    length: float  # length is now an attribute to be saved because we have type hinted it
    height: float  # height is now an attribute to be saved
    surface: float

    def __init__(self, length: float, height: float):  # We also need to typehint that, otherwise errors might occur (try it :p )
        self.length = length
        self.height = height
        self.surface = self.length * self.height

    def __str__(self):
        return "length: {} height: {} surface: {}".format(self.length, self.height, self.surface)


# Generate the DataBase

theDataStruct = ListDataStruct()
for xi in range(10):
    for yi in range(10):
        theDataStruct.add_data(MyDevice(xi, yi))

print(theDataStruct.get_data_at_index(12))  # -> displays the 12th data, which has a length of 1 and a height of 2.

# We save it to a file ... see how easy it is !
theDataStruct.save("tutorial_6bis_test_file.json")
# You can open the created file if you are curious ... this is plain text ;)

# Now we want to get it back ... nothing easier!!
newDataStruct = ListDataStruct.load("tutorial_6bis_test_file.json")
print(newDataStruct.get_data_at_index(12))  # The same thing as before ... Magic!
