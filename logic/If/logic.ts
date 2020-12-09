export const logic = (
    ctx: Context,
    statement: boolean,
    ifTrue: unknown,
    ifFalse: unknown,
): unknown =>
    ctx.val(statement) ? ctx.val(ifTrue as any) : ctx.val(ifFalse as any);
