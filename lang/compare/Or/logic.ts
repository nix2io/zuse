export const logic = (ctx: Context, left: boolean, right: boolean): boolean =>
    (ctx.val(left) as boolean) || (ctx.val(right) as boolean);
