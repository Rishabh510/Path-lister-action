import os
import sys


def set_action_output(name: str, value: str):
    sys.stdout.write(f'::set-output name={name}::{value}\n')


def main():
    # yaml_path = os.environ["INPUT_PATH"]
    # strict = os.environ["INPUT_STRICT"] == "true"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    # f=open("output.txt", "w")

    path_count = 0
    path_list = []
    paths = ""
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.yml'):
                # print(root + '/' + str(file) + '\n')
                path_list.append('/' + str(file) + '\n')
                paths = paths + root + "/" + str(file) + "\n"
                path_count = path_count + 1
            # f.write(root+'\\'+str(file)+"\n")

    set_action_output('path_count', path_count)
    # for line in path_list:
        # set_action_output('paths', line)
    set_action_output('paths', paths)

    # f.close()

    sys.exit(0)


if __name__ == "__main__":
    main()
