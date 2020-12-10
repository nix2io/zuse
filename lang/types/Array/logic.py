def logic(ctx, value: list):
    values = []
    for i in value:
        val = ctx.val(i)
        if isinstance(i, Node) and i.type == "Return":
            return val
        values.append(val)
    return values