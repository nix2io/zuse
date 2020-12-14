export const logic = (ctx: Context, value: number, base: number): number =>
    Math.round(
        (Math.log(ctx.val(value) as number) /
            Math.log(ctx.val(base) as number)) *
            100000,
    ) / 100000;
