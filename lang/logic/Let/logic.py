def logic(ctx, name: str, value: any) -> any:
    return ctx.set_symbol(
        ctx.val(name),
        ctx.val(value)
    )
