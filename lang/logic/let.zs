# © Zuse Authors 2020
# Let Function

# Define a variable
fn (
    # Variable name
    Text name,
    # Variable value.
    Any value
): Any {
    return ctx.let(
        name=name,
        value=value
    );
} -> [
    Test(["foo", "bar"], "bar", createdSymbols=[["foo", "bar"]])
]
