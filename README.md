# MyScheme

```
类似 Scheme 的方言，只有浮点数据类型。
仅支持基本算术运算。
提供条件判断、函数等基本功能。
可用于娱乐和学习目的。

A scheme-like dialect, with only floating point data types.
Only basic arithmetic operations are supported.
Basic functions such as conditional judgment and functions are available.
Can be used for entertainment and learning purposes.
```

## Grammar

1. `定义变量或函数` `Defining variables or functions` `(define var|fuc [expression|number]:{only for var}|[lambda]:{only for function})`
2. `IO` `(input|output none|expression)`
3. `条件判断` `Conditional judgment` `(if number|expression [number|expression]:{true condition} [number|expression]:{false condition})` 
4. `Lambda` `(lambda (var ...) number|expression`
5. `begin` `(begin whatever ... [final]:{only return final value})`
6. `Exit` `(exit number|expression)`

`数字，例如 123、-123、+123、1.23e10 等。`
`表达式，例如 (+ 数字|表达式 数字|表达式)`

`number such as 123, -123, +123, 1.23e10, etc.`
`expression such as (+ number|expression number|expression)`

`请注意，任何用括号括起来的内容都必须是位置 0 处的运算符或函数名称。如果兄弟中没有运算符或函数名称，则不能将所有数字都括在括号中。`

`Note that anything enclosed in parentheses must be an operator or function name at position 0. You cannot enclose all the numbers in parentheses if there are no operators or function names in the siblings.`


## Fibonacci

```
(define fib
    (lambda (n)
        (if n 
            (if (- n 1)
                (+ (fib ((- n 1))) (fib ((- n 2))))
                1
            )     
            0
        )
    )
)

(define for
    (lambda (n fuc)
        (if n
            (begin
                (output (fuc (n)))
                (for ((- n 1)))
            )
            0
        )
    )
)

(for ((input) fib))

(exit 0)
```
```
python .\myscheme.py --file .\fibonacci.txt
10
```
```
55.0
34.0
21.0
13.0
8.0
5.0
3.0
2.0
1.0
1.0
```

```
函数式编程中函数是一等公民，可以作为变量或者参数使用。
斐波那契代码中的实现是不是蛮有趣的？虽然写起来很麻烦，我调试了好久。
```

```
代码逻辑并不复杂，可能有潜在的bug，但作为娱乐和学习用途还是够够的。
喜欢的话就点个star吧！
谢谢啦~
```

```
Functions are first-class citizens in functional programming and can be used as variables or parameters.
Isn't the implementation in Fibonacci code quite interesting? Although it is troublesome to write, I debugged it for a long time.
```

```
The code logic is not complicated and there may be potential bugs, but it is enough for entertainment and learning purposes.
If you like it, please give it a star!
Thank you~
```