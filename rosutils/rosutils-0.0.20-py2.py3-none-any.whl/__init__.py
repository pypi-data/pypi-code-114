#!/usr/bin/env python
import shlex
import argparse
import os
import shutil
import tempfile
import subprocess
import time
import xml.etree.ElementTree as ET
import stat
import re

def read_file_lines(filename, line_comment="#", skip_non_existent=True):
    if skip_non_existent and not os.path.exists(filename):
        return []

    result = []

    with open(filename, "r") as file:
        for line in file.readlines():
            # Skip comments
            line = line.strip()
            if not line:
                continue
            if line_comment and line.startswith(line_comment):
                continue

            result.append(line)

    return result


class ExternalPackageCheckout(object):
    def __init__(self, package_name, git_repository, git_ref, git_submodule=False):
        self.package_name = package_name
        self.git_repository = git_repository
        self.git_ref = git_ref
        self.git_submodule = git_submodule

    @classmethod
    def parse_line(cls, line, git_submodule=False):
        parser = argparse.ArgumentParser()
        parser.add_argument("--git")
        parser.add_argument("--checkout", default="master")
        parser.add_argument("package")
        args = parser.parse_args(shlex.split(line))

        return cls(args.package, args.git, args.checkout, git_submodule)

    def is_same_repo(self, other):
        return self.git_repository == other.git_repository and self.git_ref == other.git_ref

    def checkout(self, abspath, relpath):
        # Ensure output ends with a /, otherwise, we'll get nested paths
        if not abspath.endswith("/"):
            abspath += os.sep
        if relpath.endswith("/"):
            relpath = relpath[:-1]

        if self.git_submodule:
            print("Adding submodule repository {} @ {} for package {} into {}".format(self.git_repository,
                                                                                      self.git_ref,
                                                                                      self.package_name,
                                                                                      abspath))

            # Use linux-style on windows and linux alike
            # relpath = relpath.replace(os.path.sep, "/")

            git_command = ["git", "submodule", "add", "-f", self.git_repository, relpath]
            if subprocess.call(git_command) != 0:
                raise Exception("Failed to add submodule")

            git_command = ["git", "submodule", "init", "--", relpath]
            if subprocess.call(git_command) != 0:
                raise Exception("Failed to init submodule")

            wd = os.getcwd()
            os.chdir(abspath)
            git_command = ["git", "checkout", self.git_ref]
            if subprocess.call(git_command) != 0:
                os.chdir(wd)
                raise Exception("Failed to checkout submodule")
            else:
                os.chdir(wd)

        else:
            print("Cloning repository {} @ {} for package {} into {}".format(self.git_repository,
                                                                             self.git_ref,
                                                                             self.package_name,
                                                                             abspath))

            git_command = ["git", "clone", self.git_repository, "--branch", self.git_ref, abspath]

            # Perform git command
            if subprocess.call(git_command) != 0:
                raise Exception("Failed to clone git repo")


class PackageLocation(object):
    def __init__(self, location, is_external=False, name=None):
        self.location = location
        self.is_external = is_external

        if name:
            self.name = name
        else:
            # Load name from package.xml
            self.name = ET.parse(os.path.join(location, "package.xml")).getroot().find("name").text

    @property
    def setup_location(self):
        return os.path.join(self.location, "setup")

    @property
    def has_setup(self):
        return os.path.isdir(self.setup_location)

    @property
    def setup_data_location(self):
        return os.path.join(self.location, "setup", "data")

    @property
    def has_setup_data(self):
        return os.path.isdir(self.setup_data_location)

    def get_python_requirements(self):
        filenames = ["requirements.txt", "python_requirements.txt"]
        requirements = []
        for filename in filenames:
            requirements += read_file_lines(os.path.join(self.setup_location, filename))
        return requirements

    def get_external_packages(self):
        dependencies = []
        for line in read_file_lines(os.path.join(self.setup_location, "external_packages.txt")):
            dependencies.append(ExternalPackageCheckout.parse_line(line))
        for line in read_file_lines(os.path.join(self.setup_location, "internal_packages.txt")):
            dependencies.append(ExternalPackageCheckout.parse_line(line, git_submodule=True))
        return dependencies

    def get_ros_requirements(self):
        return read_file_lines(os.path.join(self.setup_location, "ros_requirements.txt"))

    def get_system_install_scripts(self):
        if not self.has_setup:
            return []

        filenames = [f for f in os.listdir(self.setup_location) if f.lower().endswith("install_system_dependencies.sh")]
        filenames = [os.path.join(self.setup_location, f) for f in filenames]
        filenames.sort()
        return filenames


def load_external_dependency(args, output_root, temporary_root):
    # For now, we only support git
    if not args.git:
        raise RuntimeError("No --git specified for dependent package {}".format(args.package))

    # Clear existing output directory
    output_root = os.path.join(output_root, args.package)
    if os.path.exists(output_root):
        shutil.rmtree(output_root)

    # Clear existing temporary directory
    temporary_directory = os.path.join(temporary_root, args.package)
    if os.path.exists(temporary_directory):
        shutil.rmtree(temporary_directory)

    try:
        # Git clone
        git_command = ["git", "clone", args.git, temporary_directory + os.sep]
        if subprocess.call(git_command) != 0:
            raise Exception("Failed to do git clone")

        # Git checkout
        wd = os.getcwd()
        os.chdir(temporary_directory)
        git_command = ["git", "checkout", args.checkout]
        if subprocess.call(git_command) != 0:
            raise Exception("Failed to do git checkout")
        os.chdir(wd)

        # Check if the package name exists in a src/ folder
        package_dir = os.path.join(temporary_directory, "src", args.package)
        if not os.path.isdir(package_dir):
            package_dir = os.path.join(temporary_directory, args.package)
        if not os.path.isdir(package_dir):
            raise RuntimeError("Could not find package {} inside repo {}".format(args.package, args.git))

        # Move entire tree
        print("Moving dir: {} to {}".format(package_dir, output_root))
        shutil.move(package_dir, output_root)

    except Exception as e:
        shutil.rmtree(temporary_directory)
        raise e

    # Delete temporary directory
    print("Deleting dir: " + temporary_directory)
    for i in range(3):
        try:
            shutil.rmtree(temporary_directory)
        except:
            time.sleep(1)
            continue

        break

    return PackageLocation(output_root, is_external=True)


def unique(container):
    y = []
    for x in container:
        if x not in y:
            y.append(x)
    return y


def resolve_duplicate_dependencies(external_dependencies):
    resolved_external_dependencies = []

    for package in unique(e.package for e in external_dependencies):
        # Find all dependencies of this package
        package_dependencies = [e for e in external_dependencies if e.package == package]

        assert len(package_dependencies) > 0
        dependency = package_dependencies[0]

        # If there is only one, we're good to go
        if len(package_dependencies) == 1:
            resolved_external_dependencies.append(dependency)
            continue

        # If there are more, then we need to ensure all are the same
        # TODO: Nice warnings
        assert all(p.git == dependency.git for p in package_dependencies)
        assert all(p.checkout == dependency.checkout for p in package_dependencies)

    return resolved_external_dependencies


def load_external_dependency_file(filename):
    external_dependencies = []

    for line in read_file_lines(filename):
        parser = argparse.ArgumentParser()
        parser.add_argument("--git")
        parser.add_argument("--checkout", default="master")
        parser.add_argument("package")
        args = parser.parse_args(shlex.split(line))

        external_dependencies.append(args)

    return external_dependencies


def get_packages(source_root, external_packages_root=None):
    packages = []

    for root, dirs, files in os.walk(source_root):
        if "package.xml" not in files:
            continue

        # Stop iteration here
        del dirs[:]

        packages.append(PackageLocation(root, is_external=not external_packages_root or root.startswith(external_packages_root)))

    return packages


def checkout_external_packages(packages, external_packages_root, tmp_root, root):
    resolved_packages = []
    unresolved_packages = sum([p.get_external_packages() for p in packages], [])

    package_to_cloned_repo = {}

    while unresolved_packages:
        external = unresolved_packages.pop()

        # Check if this has already been resolved
        if any(external.package_name == p.package_name for p in resolved_packages) or any(external.package_name == p.name for p in packages):
            # TODO: Check of version mismatch
            print("{} Already resolved. Ignoring any version mismatches.".format(external.package_name))
            continue

        # Check if this is already checked out
        is_same_repo = [external.is_same_repo(p) for p in resolved_packages]

        if any(is_same_repo):
            # Reuse this repository
            p = resolved_packages[is_same_repo.index(True)]
            package_to_cloned_repo[external.package_name] = package_to_cloned_repo[p.package_name]
            clone_path = package_to_cloned_repo[external.package_name]

            print("Reused repository {} for package {}".format(clone_path, external.package_name))
        else:
            # Clone repository
            clone_path = os.path.join(tmp_root, external.package_name)
            package_to_cloned_repo[external.package_name] = clone_path

            external.checkout(clone_path, os.path.relpath(clone_path, root))

        # Look for the package in there
        cloned_packages = get_packages(clone_path)
        resolved_package = next((p for p in cloned_packages if p.name == external.package_name), None)
        if resolved_package is None:
            raise RuntimeError("Could not find package {} in cloned repo at {}".format(external.package_name,
                                                                                       clone_path))

        # Add sub-dependencies
        unresolved_packages += resolved_package.get_external_packages()

        # Move entire tree into final location
        package_target_location = os.path.join(external_packages_root, external.package_name)
        print("Moving dir: {} to {}".format(resolved_package.location, package_target_location))
        shutil.move(resolved_package.location, package_target_location)

        # Mark as resolved
        resolved_packages.append(external)

    # Cleanup cloned repo
    for clone_path in package_to_cloned_repo.values():
        if os.path.exists(clone_path):
            # Delete temporary directory
            print("Deleting dir: {}".format(clone_path))
            for i in range(3):
                try:
                    shutil.rmtree(clone_path)
                except:
                    time.sleep(1)
                    continue
                break


def _parse_pip_requirement_package_name(requirement_string):
    sep_char = next(re.finditer("[^a-zA-Z0-9_-]", requirement_string), None)
    if not sep_char:
        return requirement_string
    else:
        return requirement_string[:sep_char.start()]


def write_python_requirements(packages, filename):
    resolved_dependencies = []

    with open(filename, "w") as file:
        for package in packages:
            requirements = package.get_python_requirements()

            if not requirements:
                continue

            file.write("\n# From package ")
            file.write(package.name)
            file.write("\n")

            for r in requirements:
                name = _parse_pip_requirement_package_name(r)
                if name in resolved_dependencies:
                    file.write("# Duplicate: ")
                else:
                    resolved_dependencies.append(name)

                file.write(r)
                file.write("\n")


def write_apt_requirements(packages, filename):
    with open(filename, "w") as file:
        for package in packages:
            for r in package.get_ros_requirements():
                file.write(r)
                file.write("\n")


def write_install_system_dependencies_scripts(packages, main_filename, output_root, relpath=None, standalone=False):
    with open(main_filename, "w") as file:
        file.write("#!/usr/bin/env bash\n")
        file.write("set -e\n\n")

        for package in packages:
            scripts = package.get_system_install_scripts()
            if not scripts:
                continue

            title = f"# From package {package.name} #"
            file.write("#" * len(title))
            file.write("\n")
            file.write(title)
            file.write("\n")
            file.write("#" * len(title))
            file.write("\n")

            for i, filename in enumerate(scripts):
                # Standalone version, where each script is inlined
                if standalone:
                    with open(filename, "r") as scriptfile:
                        file.write(scriptfile.read())
                        file.write("\n\n\n")

                    # Copy data files
                    if package.has_setup_data:
                        data_root = os.path.join(os.path.dirname(main_filename), "data")
                        os.makedirs(data_root, exist_ok=True)
                        shutil.copytree(package.setup_data_location, data_root, dirs_exist_ok=True)
                else:
                    # Create separate directory for package
                    package_output_root = os.path.join(output_root, package.name)
                    os.makedirs(package_output_root, exist_ok=True)

                    # Copy the file into the output package root
                    print(f"shutil.copy({filename}, {package_output_root})")
                    shutil.copy(filename, package_output_root)

                    # Copy data files
                    if package.has_setup_data:
                        data_root = os.path.join(package_output_root, "data")
                        os.makedirs(data_root, exist_ok=True)
                        shutil.copytree(package.setup_data_location, data_root, dirs_exist_ok=True)

                    # Write a pointer to the original file
                    if relpath is None:
                        line = os.path.abspath(filename)
                    else:
                        line = os.path.relpath(filename, relpath)
                    if " " in line:
                        line = '"' + line + '"'
                    file.write("chmod +x " + line + "\n")
                    file.write(line)
                    file.write("\n")


def main():
    parser = argparse.ArgumentParser(description="Utility to put external packages into the catkin workspace")
    parser.add_argument("-r", "--root", default=".")
    parser.add_argument("-s", "--source-root", default="src")
    parser.add_argument("-o", "--output-root", default=None)
    parser.add_argument("-c", "--clean", action="store_true")
    parser.add_argument("--no-checkout", action="store_true")
    parser.add_argument("--relative-paths", default=None)
    parser.add_argument("--standalone", action="store_true")
    args = parser.parse_args()

    source_root = os.path.abspath(args.source_root)
    if not os.path.isdir(source_root):
        print("Output directory {} does not exist or is not a directory".format(source_root))
        exit(1)

    if args.output_root:
        output_root = args.output_root
    else:
        output_root = os.path.join(source_root, "__rosutils__")

    root = os.path.realpath(args.root)
    output_root = os.path.realpath(output_root)
    external_packages_root = os.path.join(output_root, "external_packages")
    tmp_root = os.path.join(output_root, "tmp")

    # Perform clean
    if args.clean and os.path.exists(output_root):
        shutil.rmtree(output_root)

    # # Don't run more than once
    # if os.path.exists(output_root):
    #     print("Output directory {} already exists".format(output_root))
    #     exit(1)
    # os.makedirs(output_root)

    # Ensure output paths exists
    if not os.path.isdir(output_root): os.makedirs(output_root)
    if not os.path.isdir(external_packages_root): os.makedirs(external_packages_root)
    if not os.path.isdir(tmp_root): os.makedirs(tmp_root)

    if not args.no_checkout:
        # Find internal packages (before adding externals)
        packages = [p for p in get_packages(source_root, external_packages_root) if not p.is_external]

        # Checkout the packages
        checkout_external_packages(packages, external_packages_root, tmp_root, root)

    # Find packages
    packages = get_packages(source_root, external_packages_root)

    write_python_requirements(packages, os.path.join(output_root, "python_requirements.txt"))
    write_apt_requirements(packages, os.path.join(output_root, "apt_requirements.txt"))
    write_install_system_dependencies_scripts(
        packages,
        os.path.join(output_root, "install_system_dependencies.sh"),
        os.path.join(output_root, "install_system_dependencies"),
        args.relative_paths,
        args.standalone
    )

    # Write packages
    with open(os.path.join(output_root, "all_packages.txt"), "w") as file_all:
        with open(os.path.join(output_root, "internal_packages.txt"), "w") as file_internal:
            with open(os.path.join(output_root, "external_packages.txt"), "w") as file_external:
                for pkg in packages:
                    line = pkg.name + "\n"
                    file_all.write(line)
                    if pkg.is_external:
                        file_external.write(line)
                    else:
                        file_internal.write(line)

    for pkg in packages:
        print("{} ({}) ({})".format(pkg.name, pkg.location, "external" if pkg.is_external else "internal"))


if __name__ == "__main__":
    main()
