# © Zuse Authors 2020
# Not Function

# Returns the opposite of a boolean expression.
fn (
    # Boolean expression to reverse.
    Boolean value
): Boolean {
    if value {
        return false;
    } else {
        return true;
    }
} -> [
    Test([true], false),
    Test([false], true)
]