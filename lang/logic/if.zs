# © Zuse Authors 2020
# If Function

# If statement
fn (
    # Boolean expression for the condition.
    Boolean condition,
    # Expression to be run if true.
    Any ifTrue,
    # Expression to be run if false.
    Any ifFalse
): Any {} -> [
    Test([true, "foo", "bar"], "foo"),
    Test([false, "foo", "bar"], "bar")
]