class Node:
    def __init__(self, _type, args):
        self.type = _type
        self.args = args
    
    def __repr__(self):
        return '{}({})'.format(self.type, str(self.args))

    def run(self, ctx):

        node = ctx.get(self.type)
        
        node_type = node[0]
        if node_type != 'Function':
            raise Exception(node_type + ' was used as a function')

        func_args = node[1]
        func = func_args.get('logic')

        # do some arg type validation
        
        if callable(func):
            result = func(ctx, **self.args)
        else:
            result = func.run(ctx)

        
        # validate the result

        return result

class Context:
    def __init__(self, std_funcs, config = {"logFunc": print}):
        self.symbols = {}
        self.std_funcs = std_funcs
        self.config = config
    
    def get(self, name):
        val = self.symbols.get(name) or self.std_funcs.get(name)
        if val is None:
            raise Exception(name + ' does not exist')
        return val

    def set_symbol(self, name, value):
        self.symbols[name] = value
        return value

    def val(self, node_or_value):
            return node_or_value.run(self) if isinstance(node_or_value, Node) else node_or_value

    def log(self, value):
        self.config['logFunc'](value)