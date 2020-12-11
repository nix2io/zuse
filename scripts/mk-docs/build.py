from jinja2 import Template, Environment, FileSystemLoader
from os import path, listdir, mkdir
from json import loads
from json_minify import json_minify
from typing import List


# Some constants
ROOT_DIR = path.join('..', '..')
DOCS_DIR = path.join(ROOT_DIR, 'docs/')
LANG_DIR = path.join(ROOT_DIR, "lang/");
SPECIFICATION_FILE = path.join(ROOT_DIR, "spec.jsonc");
JINJA_ENVIRONMENT = Environment(loader=FileSystemLoader("templates/"))


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
    group_folder = path.join(LANG_DIR, group_name + '/')
    return [name for name in listdir(group_folder) if path.isdir(path.join(group_folder, name))]

def render(template_name: str, *args, **kwargs):
    template_path = 'templates/{}.j2'.format(template_name)
    with open(template_path) as f:
        template = f.read()
        f.close()
    return JINJA_ENVIRONMENT.from_string(template).render(*args, **kwargs)    

def create(template_name: str, target_file: str, *args, **kwargs):
    rendered = render(template_name, *args, **kwargs)
    with open(path.join(DOCS_DIR, target_file), 'w') as f:
        f.write(rendered)
        f.close()

# Get the language spec
language_specification = get_language_specification()

# Create the docs dir
# mkdir(DOCS_DIR)

groups = language_specification['groups']

groups = []






create('index', 'index.html', groups=[[group for i, group in enumerate(groups) if i % 2 == 0], [group for i, group in enumerate(groups) if i % 2 != 0]])

