import os
import sys


def set_action_output(name: str, value: str):
    sys.stdout.write(f'::set-output name={name}::{escape(value)}\n')


def main():
    # yaml_path = os.environ["INPUT_PATH"]
    # strict = os.environ["INPUT_STRICT"] == "true"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    # f=open("output.txt", "w")

    for root, dirs, files in os.walk(dir_path):
    	for file in files:
    		if file.endswith('.yml'):
                _path = root+'\\'+str(file)+'\n';
    			print(root+'\\'+str(file)+'\n')
                set_action_output('paths', _path)
    			# f.write(root+'\\'+str(file)+"\n")

    # f.close()

    sys.exit(0)


if __name__ == "__main__":
    main()
