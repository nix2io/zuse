# © Zuse Authors 2020
# Var Function

# Get the value of a variable
fn Any (
    # Variable name.
    Text name
) { ctx.var(name) } -> [
    Test(["foo_1"], "bar")
]