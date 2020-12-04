# Internal

I want people to be able to define functions like this

```js
// xLang
Set(
  Text("sayHello"),
  Function(
    // input arguments
    Argument(
      Text("name"),
      Type(Text),
    ),
    // return type
    Type(Text),
    // code
    Code(
      Return(
        Concat(
          Text("Hello "),
          Var(
            Text("name")
          )
        )
      )
    )
  )
)

// represented internally something like this

{
  "type": "set",
  "variableName": {
    "type": "text",
    "value": "sayHello"
  },
  "arguments": [
    {
      "type": "argument",
      "name": {
        "type": "text",
        "value": "name"
      },
      // improve this type
      "type": {
        "type": "type",
        "typeName": "text"
      }
    }
  ],
  "code": {
    "type": "code",
    "code": [
      {
        "type": "return",
        "returnValue": {
          "type": "concat",
          
        }
      }
    ]
  }
}

```
This is the equivilent of 
```ts
// Typescript
const sayHello = (name: string): string => {
  return "Hello " + name;
}
```


