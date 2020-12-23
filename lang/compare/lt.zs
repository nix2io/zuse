# © Zuse Authors 2020
# Less than Function

# Returns true if the left is less than the right.
fn (
    # Left hand expression to compare.
    Text left,
    # Right hand expression to compare.
    Text right
): Boolean {
    return ctx.stdfunc.lt(
        left=left,
        right=right
    );
} -> [
    Test([1, 2], true),
    Test([2, 1], false),
    Test([1, 1], false)
]