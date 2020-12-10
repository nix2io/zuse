export const logic = (
    ctx: Context,
    name: string,
    value: Node | PrimativeTypes,
): unknown => ctx.set(ctx.val(name) as string, ctx.val(value as string));
