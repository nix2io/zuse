from jinja2 import Template, Environment, FileSystemLoader
from json import loads
from json_minify import json_minify
from typing import List
import shutil
import os


# Some constants
ROOT_DIR = os.path.join('..', '..')
DOCS_DIR = os.path.join(ROOT_DIR, 'docs/')
LANG_DIR = os.path.join(ROOT_DIR, "lang/")
SPECIFICATION_FILE = os.path.join(ROOT_DIR, "spec.jsonc")
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
    group_folder = os.path.join(LANG_DIR, group_name + '/')
    return [name for name in os.listdir(group_folder) if os.path.isdir(os.path.join(group_folder, name))]

def render(template_name: str, *args, **kwargs):
    template_path = 'templates/{}.j2'.format(template_name)
    with open(template_path) as f:
        template = f.read()
        f.close()
    return JINJA_ENVIRONMENT.from_string(template).render(*args, **kwargs)    

def create(template_name: str, target_file: str, *args, **kwargs):
    rendered = render(template_name, *args, **kwargs)
    with open(os.path.join(DOCS_DIR, target_file), 'w') as f:
        f.write(rendered)
        f.close()

def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                shutil.copy2(s, d)

# Get the language spec
language_specification = get_language_specification()

# Create the docs dir
# mkdir(DOCS_DIR)

groups = []
for group in language_specification['groups']:
    # Get this group's functions
    group_function_names = get_group_functions(group)
    group_functions = []
    for func_name in group_function_names:
        func_dir = os.path.join(LANG_DIR, group + '/', func_name + '/')
        func_spec_file = os.path.join(func_dir, 'spec.jsonc')
        func_spec = read_json_file(func_spec_file)

        group_functions.append({ "name": func_name, "description": func_spec[1].get('description', 'Undocumented Function')})

    groups.append({
        'label': group[0].upper() + group[1:],
        'functions': group_functions
    })

# Create the cheat sheet
create('home', 'index.html')
create('cheat_sheet', 'cheat_sheet.html', groups=[[group for i, group in enumerate(groups) if i % 2 == 0], [group for i, group in enumerate(groups) if i % 2 != 0]])

# Copy all the assets
copytree('assets/', os.path.join(DOCS_DIR, 'assets/'))
