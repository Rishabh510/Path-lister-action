import os
import sys


def set_action_output(name: str, value: str):
    with open(os.environ["GITHUB_OUTPUT"], "a") as myfile:
        myfile.write(f"{name}={value}\n")

def main():
    path = os.environ["INPUT_PATH"]
    extension = os.environ["INPUT_TYPE"]

    path_count = 0
    paths = ''
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(f'{extension}'):
                paths = paths + root + '/' + str(file) + ' '
                path_count = path_count + 1

    set_action_output('path_count', path_count)
    set_action_output('paths', paths)
    print(paths)

    sys.exit(0)


if __name__ == "__main__":
    main()
