export const logic = (
    _: Context,
    name: Node<"Text"> | string,
    type: Node<"Type"> | string,
): any => [
    "Argument",
    {
        name,
        type,
    },
];
