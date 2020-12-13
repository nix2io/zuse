from jinja2 import Template, Environment, FileSystemLoader
from json import loads
from json_minify import json_minify
from typing import List
import os


# Some constants
ROOT_DIR = os.path.join('..', '..')
DOCS_DIR = os.path.join(ROOT_DIR, 'docs/')
LANG_DIR = os.path.join(ROOT_DIR, "lang/")
SPECIFICATION_FILE = os.path.join(ROOT_DIR, "spec.jsonc")
JINJA_ENVIRONMENT = Environment(loader=FileSystemLoader("templates/"))
STYLES = {
    'nav_link_active': 'bg-gray-900 text-white px-3 py-2 rounded-md text-sm font-medium',
    'nav_link': 'text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium'
}

# Some functions
def read_json_file(path: str) -> object:
    '''
    Read and parse a json file
    '''
    with open(path) as f:
        content = loads(json_minify(f.read()))
        f.close()
        return content

def get_language_specification():
    '''
    Read and parse the language spec
    '''
    return read_json_file(SPECIFICATION_FILE)

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
        "styles": STYLES
    }, **kwargs})    

def create(template_name: str, target_file: str, *args, **kwargs):
    rendered = render(template_name, *args, **kwargs)
    with open(os.path.join(DOCS_DIR, target_file), 'w') as f:
        f.write(rendered)
        f.close()

# Get the language spec
language_specification = get_language_specification()

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
        func_spec_file = os.path.join(func_dir, 'spec.jsonc')
        func_spec = read_json_file(func_spec_file)
        func_attr = func_spec[1]

        group_functions.append({ "name": func_name, "description": func_spec[1].get('description', 'No Description')})

        # Create the function file

        create('function', 'fn/' + func_name.lower() + '.html', page_name=func_name, function={
            "name": func_name,
            "description": func_attr.get("description", "No Description"),
            "arguments": func_attr['arguments'],
            "returnType": func_attr["returnType"]
        })

    groups.append({
        'label': group[0].upper() + group[1:],
        'functions': group_functions
    })

# Create the cheat sheet
create('home', 'index.html')
create('cheat_sheet', 'cheat_sheet.html', page_name="Cheat Sheet", groups=[[group for i, group in enumerate(groups) if i % 2 == 0], [group for i, group in enumerate(groups) if i % 2 != 0]])

