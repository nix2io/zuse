def logic(ctx, name, _type):
    return [
        'Argument',
        {
            'name': name,
            'type': _type,
        }
    ]