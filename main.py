import os
import sys


def set_action_output(name: str, value: str):
    sys.stdout.write(f'::set-output name={name}::{value}\n')


def main():
    path = os.environ["INPUT_PATH"]
    extension = os.environ["INPUT_TYPE"]

    # dir_path = os.path.dirname(os.path.realpath(__file__))
    # # f=open("output.txt", "w")

    path_count = 0
    # path_list = []
    paths = ''
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(f'{extension}'):
                # print(root + '/' + str(file) + '\n')
                # path_list.append(root + '/' + str(file) + '\n')
                paths = paths + root + '/' + str(file) + ' '
                path_count = path_count + 1
            # f.write(root+'\\'+str(file)+"\n")

    set_action_output('path_count', path_count)
    # for line in path_list:
        # set_action_output('paths', line)
    # print(tuple(path_list))
    set_action_output('paths', paths)
    print(paths)
    # f.close()

    sys.exit(0)


if __name__ == "__main__":
    main()
