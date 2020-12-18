# © Zuse Authors 2020
# Less than or equal to Function

# Returns true if the left is less than or equal to the right.
fn Boolean (
    # Left hand expression to compare.
    Text left,
    # Right hand expression to compare.
    Text right
) { left < right || left == right } -> [
    Test([1, 2], true),
    Test([2, 1], false),
    Test([1, 1], true)
]