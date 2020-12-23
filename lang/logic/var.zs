# © Zuse Authors 2020
# Var Function

# Get the value of a variable
fn (
    # Variable name.
    Text name
): Any {
    return ctx.var(
        name=name
    );
} -> [
    Test(["foo_1"], "bar")
]