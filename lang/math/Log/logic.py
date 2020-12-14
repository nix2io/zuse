from math import log
def logic(ctx, value, base):
    return log(ctx.val(value), ctx.val(base))