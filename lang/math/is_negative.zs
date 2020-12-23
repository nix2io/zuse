# © Zuse Authors 2020
# Is Negative function

# Return true if the given value is negative.
fn (
    # Number to check if negative or not.
    Number value
): Boolean {
    return !IsPositive(
        value=value
    );
} -> [
    Test([1], false),
    Test([0], false),
    Test([-1], true)
]