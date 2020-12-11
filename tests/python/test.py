# (c) 2020 Zuse Authors
# Run the tests for the python native functions
from os import path, listdir
from json import loads
from json_minify import json_minify
from typing import List
from importlib import import_module
from dependencies import Context
import pytest

# Define some paths
ROOT_DIR = path.join('..', '..')
SPECIFICATION_FILE = path.join(ROOT_DIR, "spec.jsonc");
LANG_DIR = path.join(ROOT_DIR, "lang/");
TEMP_FILE = "tmp_logic.py";

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

# Get the language spec
language_specification = get_language_specification()

# Create the temp file
temp_file_content = "from dependencies import Context, Node\n"

for group in language_specification['groups']:
    group_functions = get_group_functions(group)
    for func_name in group_functions:
        func_dir = path.join(LANG_DIR, group + '/', func_name + '/')
        func_logic_file = path.join(func_dir, 'logic.py')
        if (path.exists(func_logic_file)):
            with open(func_logic_file) as f:
                func_logic = f.read().replace(
                    'def logic(',
                    'def {}_logic('.format(func_name.lower())
                    )
                f.close()
                temp_file_content += func_logic + "\n"

# Write the temp file
with open(TEMP_FILE, 'w') as f:
    f.write(temp_file_content)
    f.close()

# Import the new temp file's functions
logic_functions = import_module('tmp_logic')

# Create the mock context
mockContext = Context({
    "foo_1": "bar"
})

params = []

for group in language_specification['groups']:
    group_functions = get_group_functions(group)
    for func_name in group_functions:
        func_dir = path.join(LANG_DIR, group + '/', func_name + '/')
        func_spec_file = path.join(func_dir, 'spec.jsonc')
        func_spec = read_json_file(func_spec_file)

        # ignore tests without logic files
        try:
            logic_func = logic_functions.__getattribute__(func_name.lower() + "_logic")
        except AttributeError as e:
            continue
        test_spec = func_spec[1]['tests']
        # add the function and attributes to the params to test
        for i, (_, testAttr) in enumerate(test_spec):
            params.append((logic_func, testAttr))
            

@pytest.mark.parametrize("logic,attr", params)
def test_func(logic, attr):
    args = attr['arguments']
    returns = attr['returns']
    created_symbols = attr.get('createdSymbols', [])

    actual = logic(mockContext, *args)

    # Check the values
    assert actual == returns

    # Check for created symbols
    for (symbol_name, symbol_value) in created_symbols:
        actual = mockContext.get(symbol_name)
        assert actual == symbol_value
