import os
import subprocess
import sys
import tarfile


def getCurrentBranch():

    output = subprocess.check_output(["git", "branch"])
    for branch in str(output).strip("b'\\n").split("\\n"):

        if branch.startswith("*"):
            return branch.replace("*", "").strip()


def main():

    if len(sys.argv) < 4:
        print("mkupdate.py [version 1] [version 2] [destination]")
        sys.exit(1)

    print("Creating update package from {} to {} for PCS\n".format(sys.argv[1], sys.argv[2]))

    try:

        currentBranch = getCurrentBranch()

        subprocess.check_output(["git", "checkout", sys.argv[2]])
        data = subprocess.check_output(["git", "diff", "--name-only", sys.argv[1], sys.argv[2]])

    except subprocess.CalledProcessError as e:
        print("Git failed to diff the tags! Remember, you need git for this!", str(e))
        return

    changedFiles = str(data).strip("'b\\n").split("\\n")

    if len(changedFiles) is 0:
        print("No files were changed!")
        return

    for file in changedFiles:
        print("Updating: ", file)

    path = "{}/{}_{}.tar.xz".format(sys.argv[3], sys.argv[1].replace("v", "").replace(".", ""),
                                    sys.argv[2].replace("v", "").replace(".", ""))

    print("\nCreating update package {}\n".format(path))

    try:
        tar = tarfile.open(path, mode="x:xz")
    except FileExistsError as e:
        print("Update package already exists! Deleting...\n")
        os.remove(path)
        tar = tarfile.open(path, mode="x:xz")

    for file in changedFiles:
        print("Adding to archive " + file)
        try:
            tar.add(file)
        except FileNotFoundError:
            print("WARNING: {} not found!".format(file))
            continue

    print("\nFinishing update package creation...")

    tar.close()

    try:
        subprocess.check_output(["git", "checkout", currentBranch])
    except subprocess.CalledProcessError:
        print("Checkout to old branch failed !!! Checkout manually!")

    print("\nUpdate package {} created.".format(path))

if __name__ == "__main__":
    main()