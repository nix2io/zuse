def logic(ctx, condition, ifTrue, ifFalse):
    return ctx.val(ifTrue) if ctx.val(condition) else ctx.val(ifFalse)