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
): Any {
    return ctx.stdfunc._if(
        condition=condition,
        ifTrue=ifTrue,
        ifFalse=ifFalse
    );
} -> [
    Test([true, "foo", "bar"], "foo"),
    Test([false, "foo", "bar"], "bar")
]