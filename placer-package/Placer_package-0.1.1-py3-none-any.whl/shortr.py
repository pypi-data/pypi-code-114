yes = ["YES", "Yes", "yes", "Y", "y", "Yes!", "yes!", "Ja", "ja"]
no = ["NO", "No", "no", "N", "n", "No!", "no!", "Nej", "nej"]
stop = ["STOP", "Stop", "stop", "Stop!", "stop!"]
cancel = ["CANCEL", "Cancel", "cancel"]
all_lists = yes + no + stop + cancel

def s(var):



    if var in all_lists:
        if var in yes:
            var = "yes"

        if var in no:
            var = "no"

        if var == stop:
            var = "stop"

        if var in cancel:
            var = "cancel"


    return var





def sf(var):

    if var == s(var):
        var = "error"

    return var
