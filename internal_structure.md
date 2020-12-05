# Internal Representation
This covers how parsers should represent function structures.

## The Block

> **_NOTE_**  "The Block" is not the final name.

The Block is a peice of code that represents a function getting called with it's appropriate arguments.

### Structure

```json5
[
  // function identifier
  "BlockName",
  // function arguments
  {
    "argument_1": "foo",
    "argument_2": "bar",
    ...
  }
]
```

The structure is an array consisting of two elements, the [**function identifier**](#function-identifier) and the [**arguments**](#function-arguments).

### Function Identifier

The function identifier is what tells the interpreter which function to run. The function identifier should always be the first _(0th)_ element in the array.

### Function Arguments

The function arguments is an object that contain the arguments for the function when it is run. The arguments should always come after the function identifier in the array.

#### Functions with no arguments.

> **_NOTE_**  This is WIP. I am not sure if I want to require an arguments object if the function takes no arguments. 

If the function takes no arguments, you still need to include the function arguments object as an empty object: `{}`.

### Examples

#### Hello World Example

```json5
[
  // print to console
  "Print",
  {
    // text argument
    "text": [
      // text datatype
      "Text",
      {
        // value of the text
        "value": "Hello World"
      }
    ]
  }
]
```

