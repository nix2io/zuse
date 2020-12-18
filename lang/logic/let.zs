# © Zuse Authors 2020
# Let Function

# Define a variable
fn Any (
    # Variable name
    Text name,
    # Variable value.
    Any value
) { ctx.let(name, value) } -> [
    Test(["foo", "bar"], "bar", createdSymbols=[["foo", "bar"]])
]
