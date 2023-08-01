import os
import shutil

AUTOMATOR_PATH = os.path.expanduser("~/Library/Workflows/Applications")
SCRIPT_DIRS = {}


def get_scripts(path):
    ret = []
    for root, dirs, _ in os.walk(path):
        for file_name in dirs:
            if file_name.endswith(".workflow"):
                ret.append(os.path.join(root, file_name))
                break
    
    return ret

def iter_scripts(script_dirs):
    scripts = []
    for v in script_dirs.values():
        scripts += v
    return scripts

def toggle_script(script_path):
    path, tail = os.path.split(path)

def main():
    print("Disablemator Copyright 2023 lololol")
    print("Automator Script Dir: {}".format(AUTOMATOR_PATH))

    # Check if the folder exists
    if os.path.exists(AUTOMATOR_PATH) and os.path.isdir(AUTOMATOR_PATH):
        while True:
            # Get all the folders on the first level
            all_dirs = set([item for item in os.listdir(AUTOMATOR_PATH) if os.path.isdir(os.path.join(AUTOMATOR_PATH, item))])

            if not "Disabled" in all_dirs:
                os.makedirs(os.path.join(AUTOMATOR_PATH, "Disabled"))
                print("Creating 'Disabled' Directory...")

            for d in all_dirs:
                SCRIPT_DIRS[d] = get_scripts(os.path.join(AUTOMATOR_PATH, d))

            scripts = iter_scripts(SCRIPT_DIRS)
            print("Found {} scripts".format(len(scripts)))
            print("=====================================")
            print("Select the index to toggle\n<(*) = Enabled>")
            print("-------------------------------------")

            i = 0
            for script in scripts:
                parent, child = os.path.split(script)
                parent, folder = os.path.split(parent)
                _, disabled = os.path.split(parent)
                disabled = disabled == "Disabled"

                if disabled:
                    print("{}) {}".format(i, child))
                else:
                    print("{}) {} (*)".format(i, child))
                i += 1

            index = int(input("-------------------------------------\n"))
            script = scripts[index]
            child_parent, child = os.path.split(script)
            folder_parent, folder = os.path.split(child_parent)
            disabled_parent, disabled = os.path.split(folder_parent)
            disabled = disabled == "Disabled"

            if disabled:
                shutil.move(script, os.path.join(AUTOMATOR_PATH, folder, child))
            else:
                shutil.move(script, os.path.join(folder_parent, "Disabled", folder, child))



    else:
        print("Couldn't find Automator Directory :( Maybe wrong version?")
        os._exit(0)





if __name__ == "__main__":
    main()