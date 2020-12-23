# © Zuse Authors 2020
# Or Function

# Returns true if either the left or right value is true.
fn (
    # Left hand boolean expression.
    Boolean left,
    # Right hand boolean expression.
    Boolean right
): Boolean {
    return ctx.stdfunc.or(
        left=left,
        right=right
    );
} -> [
    Test(arguments=[true, true], returns=true),
    Test(arguments=[true, false], returns=true),
    Test(arguments=[false, true], returns=true),
    Test(arguments=[false, false], returns=false)
]