def logic(ctx, arguments, returnType, logic, description):
    return [
        'Function',
        {
            'arguments': arguments,
            'returnType': returnType,
            'logic': logic,
            'description': description
        }
    ]