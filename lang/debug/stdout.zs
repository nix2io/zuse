# © Zuse Authors 2020
# Stdout Function

# Print a value to stdout.
fn (
    # Value to print to stdout.
    Any value
) {
    ctx.stdout(value);
} -> [
    Test(["hi there"], inLog="hi there")
]