# © Zuse Authors 2020
# Not Function

# Returns the opposite of a boolean expression.
fn Boolean (
    # Boolean expression to reverse.
    Boolean value
) { false if value else true } -> [
    Test([true], false),
    Test([false], true)
]