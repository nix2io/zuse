export const logic = (ctx: Context, name: string): string =>
    ctx.get(ctx.val(name) as string);
