def logic(ctx, left: bool, right: bool) -> bool:
    return ctx.val(left) and ctx.val(right)