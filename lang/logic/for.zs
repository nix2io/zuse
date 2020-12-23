# © Zuse Authors 2020
# For Function

# For loop.
fn (
  # Initiation expression.
  Expression init,
  # End expression.
  Expression end,
  # Increment expression.
  Expression increment,
  # Body expression
  Expression body
) {
  init();
  while end() {
    body();
    increment();
  }
}
