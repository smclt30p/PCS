import os
import subprocess
import sys
import tarfile


def main():

    if len(sys.argv) < 3:
        print("Invalid parameters! Found {} expected 3".format(len(sys.argv)))
        sys.exit(1)

    print("Creating update package from {} to {} for PCS\n".format(sys.argv[1], sys.argv[2]))

    try:

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

    old_ver = sys.argv[1].replace("v", "").replace(".", "")
    new_ver = sys.argv[2].replace("v", "").replace(".", "")

    if len(sys.argv) == 4:
        path = "{}/{}_{}.tar.xz".format(sys.argv[3], old_ver, new_ver)
    else:
        path = "update/{}_{}.tar.xz".format(old_ver, new_ver)


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

    print("\nUpdate package {} created.".format(path))

if __name__ == "__main__":
    main()