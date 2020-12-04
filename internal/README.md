Define a text value
```js
Text({
  value: "hello there"
})
// what we want to move to in the future
Text("hello there")


// internally represented as
[
  "Text",
  {
    "value": "hello there"
  }
]
```

Define a function
```js
// write a function to return "Hello {theName}"

Function({
  arguments: [
    Argument({
      name: "theName",
      type: Type({
        type: "text"
      })
    })
  ],
  returnType: Type({
    type: "text"
  }),
  code: Return({
    value: Concat({
      value_left: Text({
        value: "Hello "
      }),
      value_right: Var({
        name: "theName"
      })
    })
  })
})
// what we want to move to
Function(
  [
    Argument(
      "theName",
      Type("text")
    )
  ],
  Type("text"),
  Return(
    Concat(
      Text("Hello "),
      Var("theName")
    )
  )
})

// internal representation
[
  "Function",
  {
    "arguments": [
      [
        "Argument",
        {
          "name": "theName",
          "type": [
            "Type",
            {
              "type": "text"
            }
          ]
        }
      ]
    ],
    "returnType": [
      "Type",
      {
        "type": "Text"
      }
    ],
    "code": [
      "Return",
      {
        "value": [
          "Concat",
          {
            "value_left": [
              "Text",
              {
                "value": "Hello "
              }
            ],
            "value_right": [
              "Var",
              {
                "name": "theName"
              }
            ]
          }
        ]
      }
    ]
  }
]

```
