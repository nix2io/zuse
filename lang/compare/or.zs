# © Zuse Authors 2020
# Or Function

# Returns true if either the left or right value is true.
fn Boolean (
    # Left hand boolean expression.
    Boolean left,
    # Right hand boolean expression.
    Boolean right
) { ctx.stdfunc.or(left, right) } -> [
    Test(arguments=[true, true], returns=true),
    Test(arguments=[true, false], returns=true),
    Test(arguments=[false, true], returns=true),
    Test(arguments=[false, false], returns=false)
]