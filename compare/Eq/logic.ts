const logic = (ctx: Context, left: unknown, right: unknown): boolean =>
    ctx.val(left as any) == ctx.val(right as any);
