# Standard Functions

This is a list of the standard functions in the Zuse language.

#### Table of Contents

- [Type Functions](#type-functions)
  - [Type](#type)
- [Logic](#logic)
  - [Let](#let)
  - [Var](#var)
  - [Return](#return)
  - [If](#if)
  - [For](#for)

## Type Functions

These functions help define types.

### Type

The type function is used to specifiy a type.

Right now these are used for function argument types and return types.

#### Arguments

| Name       | Type                   | Description                   |
|------------|------------------------|-------------------------------|
| `typeName` | [`Text`](./types#text) | The name of the type as text. |

> **_NOTE_**  Not sure if I want to keep the name `typeName`, might just change it to `type` 

#### Example

In this example, it is defining a type of number

```json5
[
  "Type",
  {
    "typeName": [
      "Text",
      {
        "value": "Number"
      }
    ]
  }
]
```

----

### Either

Either allows you to specifiy two types. This is the same as the `|` in typescript.

#### Arguments

| Name         | Type                 | Description                   |
|--------------|----------------------|-------------------------------|
| `type_left`  | [`Any`](./types#any) | First type                    |
| `type_right` | [`Any`](./types#any) | Second type                   |

#### Example

```json5
// Either a Text type or a Number type
[
  "Either",
  {
    "type_left": [
      "Type",
      {
        "typeName": [
          "Text",
          {
            "value": "Text"
          }
        ]
      }
    ],
    "type_right": [
      "Type",
      {
        "typeName": [
          "Text",
          {
            "value": "Number"
          }
        ]
      }
    ]
  }
]
```

## Logic

### Let

Let is used to define a variable in the scope.

#### Arguments

| Name       | Type                   | Description                   |
|------------|------------------------|-------------------------------|
| `name`     | [`Text`](./types#text) | The name of the variable      |
| `value`    | [`Any`](./types#any)   | The value of the variable     |

#### Example

```json5
// let foo = "bar"
[
  "Let",
  {
    "name": [
      "Text",
      {
        "value": "foo"
      }
    ],
    "value": [
      "Text",
      {
        "value": "bar"
      }
    ]
  }
]
```

----

### Var

Var is used to retrive the value of a defined variable

#### Arguments

| Name       | Type                   | Description                   |
|------------|------------------------|-------------------------------|
| `name`     | [`Text`](./types#text) | The name of the variable      |

#### Example

```json5
// get the contents of the variable "foo"
[
  "Var",
  {
    "name": [
      "Text",
      {
        "value": "foo"
      }
    ]
  }
]
```

----

### Return

Return a value for a function.

This can only be called in a function.

#### Arguments

| Name       | Type                 | Description         |
|------------|----------------------|---------------------|
| `value`    | [`Any`](./types#any) | The value to return |

> **_NOTE_**  Not sure if I want to have the default value return `Null` or some like `void`.

#### Example

```json5
[
  "Return",
  {
    "value": [
      "Text",
      {
        "value": "Text getting returned"
      }
    ]
  }
]
```

----

### If

If statement in Zuse.

#### Arguments

| Name        | Type                         | Description                     |
|-------------|------------------------------|---------------------------------|
| `condition` | [`Boolean`](./types#boolean) | Condition to check whether true |
| `true`      | Code                         | Code if cond is true            |
| `false`     | Code                         | Code if cond is false           |

> **_NOTE_**  Might change these names.

#### Example

```json5
[
  "If",
  {
    "condition": [
      "Boolean",
      {
        "value": true
      }
    ],
    "true": [
      "Text",
      {
        "value": "Condition met"
      }
    ],
    "false": [
      "Text",
      {
        "value": "Condition was not met"
      }
    ]
  }
]
```

----

### For

The for operator allows you to iterate over things.

#### Arguments

| Name    | Type                              | Description                    |
|---------|-----------------------------------|--------------------------------|
| `item`  | Either(Type(Array), Type(Object)) | Array or object                |
| `logic` | Code                              | Logic to be run over each item |

#### Examples

Here is an example for iterating over an object. 

> **_NOTE_**  This very simple example is very long and it would be nice to be able to shorten it.

The for loop is based on the python for loop.

The function arguments work like this

If given **one** argument:

|         | Object | List  |
|---------|--------|-------|
| 1st Arg | Value  | Value |

If given **two** arguments:

|         | Object | List  |
|---------|--------|-------|
| 1st Arg | Key    | Index |
| 2nd Arg | Value  | Value |


```json5
[
  "For",
  {
    "item": [
      "Object",
      {
        "value": {
          "foo": [
            "Text",
            {
              "value": "bar"
            }
          ],
          "key": [
            "Text",
            {
              "value": "pair"
            }
          ]
        }
      }
    ],
    "code": [
      "Function",
      {
        "arguments": [
          "Array",
          {
            "value": [
              [
                "Argument",
                [
                  {
                    "name": [
                      "Text",
                      {
                        "value": "key"
                      }
                    ],
                    "type": [
                      "Type",
                      {
                        "typeName": [
                          "Text",
                          {
                            "value": "Text"
                          }
                        ]
                      }
                    ]
                  }
                ]
              ],
              [
                "Argument",
                [
                  {
                    "name": [
                      "Text",
                      {
                        "value": "value"
                      }
                    ],
                    "type": [
                      "Type",
                      {
                        "typeName": [
                          "Text",
                          {
                            "value": "Text"
                          }
                        ]
                      }
                    ]
                  }
                ]
              ]
            ]
          }
        ],
        "logic": [
          "Log",
          {
            "value": [
              "Add",
              {
                "values": [
                  "Array",
                  {
                    "value": [
                      [
                        "Var",
                        {
                          "name": [
                            "Text",
                            {
                              "value": "key"
                            }
                          ]
                        }
                      ],
                      [
                        "Text",
                        {
                          "value": " is set to "
                        }
                      ],
                      [
                        "Var",
                        {
                          "name": [
                            "Text",
                            {
                              "value": "key"
                            }
                          ]
                        }
                      ]
                    ]
                  }
                ]
              }
            ]
          }
        ]
      }
    ]
  }
]
```

Future syntax:

```js
For(
  Object(
    {
      "foo": Text("bar"),
      "key": Text("pair")
    }
  ),
  Function(
    Array(
      Argument(
        Text("key"),
        Type(Text)
      ),
      Argument(
        Text("value"),
        Type(Text)
      )
    )
    Type(
      Null()
    ),
    Log(
      Add(
        Var(
          Text("key")
        ),
        Text(" is set to "),
        Var(
          Text("value")
        )
      )
    )
  )
)
```
