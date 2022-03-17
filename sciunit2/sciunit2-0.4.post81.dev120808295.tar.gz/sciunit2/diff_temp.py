import subprocess
from subprocess import PIPE
import sys

"""
This function parses the result of rsync command
and outputs in the following format:
 Files only in e1:
 Files only in e2:
 Files with changed size:
 Files with changed modified time:
 Files with changed permissions:

Detail on output format of rsync could be found at:
 https://linux.die.net/man/1/rsync 
"""


def parse_rsync(out):
    # each line starts with YXcstpoguax followed by file/dir name
    out_str = out.decode("utf-8").strip()
    lines = out_str.split("\n")
    new_e1 = set()
    new_e2 = set()
    size_changed = set()
    time_changed = set()
    perms_changed = set()
    for line in lines:
        splits = line.split()
        YXcstpoguax = splits[0].strip()
        file_name = splits[1].strip()
        update_type = YXcstpoguax[0]
        file_type = YXcstpoguax[1]
        # TODO: size of YXcstpoguax might not be 11 letters long,
        #  as in '*deleting'
        file_size = YXcstpoguax[3]
        modified_time = YXcstpoguax[4]
        file_perms = YXcstpoguax[5]

        if update_type == '*':  # contains a message
            # case 1: *deleting (file is present in e2, not e1)
            # these are the new files in e2
            if YXcstpoguax[1:] == "deleting":
                new_e2.add(file_name)

        # '.' is for changed but not being updated
        # '>' local change to take place
        elif update_type == '.' or update_type == '>':
            if file_type == 'f':  # it is a file
                # case 1: '>f+++++++++'
                # case 2: '.f.stp.....'
                if YXcstpoguax[2] == '+':  # new file in e1
                    new_e1.add(file_name)
                if file_size == 's':  # size of file changed
                    size_changed.add(file_name)
                if modified_time == 't':  # modified time of file changed
                    time_changed.add(file_name)
                if file_perms == 'p':  # permissions of file changed
                    perms_changed.add(file_name)
        else:  # rest of the cases not handled right now
            continue

    return new_e1, new_e2, size_changed, time_changed, perms_changed


if len(sys.argv) != 3:
    print("less than 3 arguments")
    dir1 = "/home/raza/Downloads/HANDWorkflow_threshold_5000"
    dir2 = "/home/raza/Downloads/HANDWorkflow_threshold_50000"
else:
    dir2 = sys.argv[1].strip()
    dir1 = sys.argv[2].strip()
print("comparing diff between {0} and {1}".format(dir1, dir2))

# prefix = "/home/raza/Downloads/diff_example/Diff/"
# dir1 = prefix + dir1
# dir2 = prefix + dir2

cmd = "rsync -nai --delete {0}/ {1}/".format(dir1, dir2)
# p = subprocess.Popen(cmd, shell=True, cwd=prefix, stderr=PIPE, stdout=PIPE)
p = subprocess.Popen(cmd, shell=True, stderr=PIPE, stdout=PIPE)
out, err = p.communicate()
p_return_code = p.wait()
if p_return_code != 0:
    print("error executing diff command!: " + err.__str__())

# process output by rsync command
try:
    new_dir1, new_dir2, size_changed, time_changed, perms_changed = \
        parse_rsync(out)
    output = "Differences in executions " + dir1 + " and " + dir2 + ":\n\n" + \
             "Files only in " + dir1 + ":\n" + '\n'.join(new_dir1) + "\n\n" + \
             "Files only in " + dir2 + ":\n" + '\n'.join(new_dir2) + "\n\n" + \
             "Files with changed size:\n" + '\n'.join(size_changed) + "\n\n" + \
             "Files with changed modified time:\n" + '\n'.join(time_changed) + "\n\n" + \
             "Files with changed permissions:\n" + '\n'.join(perms_changed) + "\n\n"
except Exception:
    output = "error executing diff command!"

print(output)
