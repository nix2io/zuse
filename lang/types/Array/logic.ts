export const logic = (ctx: Context, value: Node[]): unknown => {
    const vals = [];
    for (const val of value) {
        const computedValue = ctx.val(val);
        if (val.type == "Return") return computedValue;
        vals.push(computedValue);
    }
    return vals;
};
