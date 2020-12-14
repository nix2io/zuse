from jinja2 import Template, Environment, FileSystemLoader
from yaml import safe_load
from typing import List
import os


# Some constants
ENV = 'prod'
ROOT_DIR = os.path.join('..', '..')
DOCS_DIR = os.path.join(ROOT_DIR, 'docs/')
LANG_DIR = os.path.join(ROOT_DIR, "lang/")
SPECIFICATION_FILE = os.path.join(ROOT_DIR, "spec.yaml")
JINJA_ENVIRONMENT = Environment(loader=FileSystemLoader("templates/"))
STYLES = {
    'nav_link_active': 'px-3 py-2 transition-colors duration-200 relative block text-pink-500',
    'nav_link': 'px-3 py-2 transition-colors duration-200 relative block hover:text-gray-300 text-gray-500'
}

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

def render(template_name: str, *args, **kwargs):
    template_path = 'templates/{}.j2'.format(template_name)
    with open(template_path) as f:
        template = f.read()
        f.close()
    return JINJA_ENVIRONMENT.from_string(template).render(*args, **{**{
        "page_name": "Home",
        "styles": STYLES,
        "ROOT_URL": 'https://nix2io.github.io/zuse/' if ENV != 'dev' else ''
    }, **kwargs})    

def create(template_name: str, target_file: str, *args, **kwargs):
    rendered = render(template_name, *args, **kwargs)
    with open(os.path.join(DOCS_DIR, target_file), 'w') as f:
        f.write(rendered)
        f.close()

def type_to_py(_type: list) -> str:
    if type(_type) is str:
        # built in types
        if _type == '_string':
            return 'str'
        if _type == '_number':
            return 'int'
        if _type == '_boolean':
            return 'bool'
        if _type == '_array':
            return 'list'
        if _type == '_any':
            return 'any'
        # types
        if _type == 'Text':
            return 'Text'
        if _type == 'Number':
            return 'Number'
        if _type == 'Boolean':
            return 'Boolean'
        if _type == 'Null':
            return 'Null'
        if _type == 'Any':
            return 'Any'
        return '_type'

    if type(_type) is not list:
        raise Exception(_type + ' is not a list')

    node_type = _type[0]
    node_args = _type[1]
    if node_type == 'ArrayOf':
        return 'Array of {}'.format(type_to_py(node_args['type']))
    if node_type == 'Union':
        return '{} or {}'.format(type_to_py(node_args['typeLeft']), type_to_py(node_args['typeRight']))

    if node_type != 'Type':
        raise Exception(node_type + ' is not a Type')
    

    typeName = node_args['typeName']
    return type_to_py(typeName)

def format_value(val):
    if type(val) is str:
        return '"' + val + '"'
    if type(val) is bool:
        return 'true' if val else 'false'
    if val is None:
        return 'null'
    return str(val)

# Get the language spec
language_specification = get_language_specification()

if (ENV != 'dev'):
    # Create the docs dir
    os.mkdir(DOCS_DIR)
    # Create the fn dir
    os.mkdir(os.path.join(DOCS_DIR, 'fn/'))

groups = []
for group in language_specification['groups']:
    # Get this group's functions
    group_function_names = get_group_functions(group)
    group_functions = []
    for func_name in group_function_names:
        func_dir = os.path.join(LANG_DIR, group + '/', func_name + '/')
        func_spec_file = os.path.join(func_dir, 'spec.yaml')
        func_spec = read_yaml_file(func_spec_file)
        func_attr = func_spec[1]

        group_functions.append({ "name": func_name, "description": func_spec[1].get('description', 'No Description')})

        args = [{"name": arg[1]['name'], "type": type_to_py(arg[1]['type']), "description": arg[1].get('description', 'No description')} for arg in func_attr['arguments']]

        test_attr = func_attr['tests'][0][1]
        example = {
            "args": ", ".join([format_value(arg) for arg in test_attr['arguments']]),
            "returns": format_value(test_attr['returns'])
        }

        # Create the function file

        create('function', 'fn/' + func_name.lower() + '.html', page_name=func_name, function={
            "name": func_name,
            "description": func_attr.get("description", "No Description"),
            "arguments": args,
            "returnType": func_attr["returnType"],
            "arg_names": ", ".join([arg['name'] for arg in args]),
            "returns": func_attr.get('returns', 'No return description'),
            "example": example
        })

    groups.append({
        'label': group[0].upper() + group[1:],
        'functions': group_functions
    })

# Create the cheat sheet
create('home', 'index.html')
create('cheat_sheet', 'cheat_sheet.html', page_name="Cheat Sheet", groups=[[group for i, group in enumerate(groups) if i % 2 == 0], [group for i, group in enumerate(groups) if i % 2 != 0]])

