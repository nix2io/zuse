def logic(ctx, left: int, right: int) -> int:
    return ctx.val(left) % ctx.val(right)