# © Zuse Authors 2020
# Reciprocal Function

# Return the reciprocal of a number.
fn Number (
    # Value to get the reciprocal of.
    Number value
) { value ^ -1 } -> [
    Test([2], .5),
    Test([4], .25)
]