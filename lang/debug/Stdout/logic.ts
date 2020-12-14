export const logic = (ctx: Context, value: string): void => {
    ctx.log(ctx.val(value));
};
