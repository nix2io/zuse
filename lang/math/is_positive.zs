# © Zuse Authors 2020
# Is Positive function

# Return true if the given value is positive.
fn (
    # Number to check if positive or not.
    Number value
): Boolean {
    return value > 0;
} -> [
    Test([1], true),
    Test([0], false),
    Test([-1], false)
]