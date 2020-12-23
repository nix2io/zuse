# © Zuse Authors 2020
# Array Function

# Create an array of items.
fn (
    # Contents of the array.
    _array value
): ArrayOf(Any) {
    return ctx.stdfunc.array(value);
}