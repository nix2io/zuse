# © Zuse Authors 2020
# Function Function

# Create an anonymous function.
fn Function (
    # Function arguments.
    ArrayOf(Argument) arguments,
    # Function return type.
    Type type,
    # Function logic.
    Any logic,
    # Function description.
    Text description
) { ctx.stdfunc.function(arguments, type, logic, description) }