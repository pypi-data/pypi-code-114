from tljh.hooks import hookimpl
import os, traceback, shutil

@hookimpl
def tljh_new_user_create(username):
    f = open("/etc/passwd")
    for row in f.readlines():
        if username in row:
            pid, path = row.strip().split("::")
            path = path.split("/")[1]
            break
    home = f"/{path}/{username}"
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", file=f)
    os.system(f"echo NEW USER: {username} HOME: {home} >> tljh-new-user.log")

    if os.path.isdir('new_user_data'):
        os.system(f"echo ' ' copying new_user_data >> tljh-new-user.log")
        try:
            shutil.copytree("new_user_data", home, dirs_exist_ok=True)
            os.system(f"chown -R {username}:{username} {home}")
        except:
            f=open("tljh-new-user.log", 'a')
            print (traceback.format_exc(), file=f)
            f.close()
    else:
        os.system(f"echo ' ' no new_user_data directory found, nothing to copy >> tljh-new-user.log")

    if os.path.exists('new_user_script'):
        os.system(f"echo ' ' executing new_user_script {home} >> tljh-new-user.log")
        err = os.system(f"./new_user_script {home} >> tljh-new-user.log 2>&1")
        os.system(f"echo ' ' script returns {err} >> tljh-new-user.log")
        if err:
            raise Exception("new_user_script error {err}")
    else:
        os.system(f"echo ' ' no new_user_script found >> tljh-new-user.log")
