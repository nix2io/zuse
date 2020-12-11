export const logic = (ctx: Context, left: number, right: number): boolean =>
    ctx.val(left)! < ctx.val(right)!;
