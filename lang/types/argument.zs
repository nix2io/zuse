# © Zuse Authors 2020
# Argument Function

# The type for a function argument.
fn Argument (
    # Name of the argument.
    Text name,
    # Type of the argument.
    Type type,
    # Default argument value.
    Any default,
    # Description of the argument.
    Text description
) { ["Argument", ctx.args] } -> [
    Test(
        ["arg", "Text"],
        ["Argument",
            {"name": "arg", "type": ["Type", {"typeName": "Text"}]}
        ]
    )
]