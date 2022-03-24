'''
This class is used for the fileInfoEx method of File class.
Its fields, such as VOCNAME, are defined as the list index of the return value
split by the \xff character from the server. The index values are from 0 to 22.
The field LIST_COUNT is the total item count of the list. It is a fixed value.
'''
class FileInfoEx:
    IS_FILEVAR = 0
    VOCNAME = 1
    PATHNAME = 2
    TYPE = 3
    HASHALG = 4
    MODULUS = 5
    MINMODULUS = 6
    GROUPSIZE = 7
    LARGERECORDSIZE = 8
    MERGELOAD = 9
    SPLITLOAD = 10
    CURRENTLOAD = 11
    NODENAME = 12
    IS_AKFILE = 13
    CURRENTLINE = 14
    PARTNUM = 15
    STATUS = 16
    RECOVERYTYPE = 17
    RECOVERYID = 18
    IS_FIXED_MODULUS = 19
    NLSMAP = 20
    ENCRYPTION = 21 #In fact 22 in server side
    REPSTATUS = 22 #In fact 24 in server side
    LIST_COUNT = 23
