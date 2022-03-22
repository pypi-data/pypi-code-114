import os.path
import platform
import getpass


def os_name():
    return platform.system()


def get_user():
    return getpass.getuser()


class UEPath:
    """A platform dependent path class."""
    engine_binaries_path = ""
    engine_samples_path = ""
    unreal_version = ""

    def __init__(self, unreal_version):
        os_type = os_name()
        user = get_user()

        root_path = ""
        binary_dir = ""
        self.unreal_version = unreal_version

        if os_type.lower() == "windows":
            root_path = "E:\\"
            binary_dir = "Win64"
        if os_type.lower() == "darwin":
            root_path = "/Users/{User}/Applications/Epic/".format(User=user)
            binary_dir = "Mac"
        if os_type.lower() == "linux":
            root_path = "/home/{User}/Applications/Epic/".format(User=user)
            binary_dir = "Linux"

        self.engine_binaries_path = os.path.normpath(os.path.join(root_path,
                                                                  "UE_{UnrealVersion}_Source".format(
                                                                      UnrealVersion=unreal_version),
                                                                  "Engine",
                                                                  "Binaries",
                                                                  binary_dir))

        self.engine_samples_path = os.path.normpath(os.path.join(root_path,
                                                                 "UE_{UnrealVersion}_Source".format(
                                                                     UnrealVersion=unreal_version),
                                                                 "Samples"))

    def fix_paths(self, data):
        if os_name() != "windows":
            data = data.replace("E:", "~/Applications")
            data = data.replace("\\", "/")
        data = data.replace("4.27", self.unreal_version)
        return data
