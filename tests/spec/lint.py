from yaml import safe_load
import os
from typing import List

# Some constants
ROOT_DIR = os.path.join('..', '..')
LANG_DIR = os.path.join(ROOT_DIR, "lang/")
SPECIFICATION_FILE = os.path.join(ROOT_DIR, "spec.yaml")

# Some functions
def read_yaml_file(path: str) -> object:
    '''
    Read and parse a yaml file
    '''
    with open(path) as f:
        content = safe_load(f.read())
        f.close()
        return content

def get_language_specification():
    '''
    Read and parse the language spec
    '''
    return read_yaml_file(SPECIFICATION_FILE)

def get_group_functions(group_name: str) -> List[str]:
    '''
    Returns a list of functions from a group name
    '''
    group_folder = os.path.join(LANG_DIR, group_name + '/')
    return [name for name in os.listdir(group_folder) if os.path.isdir(os.path.join(group_folder, name))]

language_specification_base = get_language_specification()

# TODO: lint the language specification base file

lanugage_specification = {}
language_paths = {}
for group_name in language_specification_base['groups']:
    group_functions = get_group_functions(group_name)
    for func in group_functions:
        func_path = os.path.join(LANG_DIR, group_name, func, "spec.yaml")
        with open(func_path) as f:
            lanugage_specification[func] = safe_load(f.read())
            language_paths[func] = func_path
            f.close()



from pprint import pprint


class Position:
    def __init__(self) -> None:
        self.file: str = None
    
    def set_file(self, file: str) -> str:
        self.file = file
        return file

class LintError(Exception):
    def __init__(self, position: Position, msg) -> None:
        super().__init__('ERROR PARSING {}: {}'.format(position.file, msg))
        self.position = position
        self.msg = msg


linted_funcs = set()


def isNodeLike(node):
    if type(node) is not list:
        return False, False
    if len(node) == 0:
        return False, False
    if all(map(lambda x: isNodeLike(x)[0], node)):
        return True, True
    
    if type(node[1]) is dict and type(node[0]) is str:
        return True, False
    return False, False

def lint_func(obj, position: Position, no_recursion=False):
    print()
    print('linting...')
    pprint(obj)
    print()

    isNode, isArray = isNodeLike(obj)
    if not isNode:
        return
    
    nodes = obj
    if not isArray:
        nodes = [obj]
    
    for node in nodes:
        name, args = node
        # Verify all the arguments from the function
        spec = lanugage_specification.get(name)
        if spec is None:
            raise LintError(position, name + " is not a valid function")
        # verify arguments
        spec_attr = spec[1]
        spec_arguments = spec_attr['arguments']

        for arg in spec_arguments:

            # Lint the argument
            if not no_recursion:
                
                lint_func(arg, position, no_recursion=True)


            _, arg_args = arg
            

            arg_name = arg_args['name']
            if arg_name not in args.keys() and 'default' not in arg_args:
                raise LintError(position, arg_name + ' not in args for ' + name)
        
        for key in args.keys():
            if key not in [v['name'] for _, v in spec_arguments]:
                raise LintError(position, key + " is not a valid arg for " + name)

        print(args)
        print()


position = Position()

for name, func in lanugage_specification.items():
    position.set_file(language_paths[name])
    try:
        lint_func(func, position)
    except LintError as e:
        print("::error file={},line={},col={}::{}".format(e.position.file, 5, 1, e.msg))
