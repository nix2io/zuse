export const logic = (ctx: Context, left: number, right: number): number =>
    (ctx.val(left) as number) / (ctx.val(right) as number);
