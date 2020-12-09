export const logic = (
    _: Context,
    args: Node[],
    returnType: Node,
    logic: () => any,
    description: string,
): any => [
    "Function",
    {
        arguments: args,
        returnType,
        logic,
        description,
    },
];
