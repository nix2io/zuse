export const logic = (ctx: Context, value: number): number => Math.cos(ctx.val(value) as number)