# © Zuse Authors 2020
# Equals Function

# Returns true if both values are equal.
fn (
    # Left hand expression to compare.
    Any left,
    # Right hand expression to compare.
    Any right
): Boolean {} -> [
    Test(["foo", "foo"], true),
    Test(["foo", "bar"], false)
]