# © Zuse Authors 2020
# Greater than Function

# Returns true if the left is greater than the right.
fn (
    # Left hand expression to compare.
    Number left,
    # Right hand expression to compare.
    Number right
): Boolean {} -> [
    Test([2, 1], true),
    Test([1, 2], false),
    Test([1, 1], false)
]