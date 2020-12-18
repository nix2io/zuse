# © Zuse Authors 2020
# Less than Function

# Returns true if the left is greater than the right.
fn Boolean (
    # Left hand expression to compare.
    Text left,
    # Right hand expression to compare.
    Text right
) { ctx.stdfunc.lt(left, right) } -> [
    Test([1, 2], true),
    Test([2, 1], false),
    Test([1, 1], false)
]