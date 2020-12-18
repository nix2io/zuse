# © Zuse Authors 2020
# And Function

# Returns true if both values are true.
fn Boolean (
  # Left hand boolean expression.
  Boolean left,
  # Right hand boolean expression.
  Boolean right
) { native; } -> [
  Test(arguments=[true, true], returns=true),
  Test(arguments=[true, false], returns=false),
  Test(arguments=[false, true], returns=false),
  Test(arguments=[false, false], returns=false)
]
