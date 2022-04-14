# Personal-Programming-Laguage

# 1. do simple calculation using () and + - * /

# 2. do power operation using ^

# 3. make variales 
        key word: 'BS'
        start with: lowercase/uppercase letters
        in the middle: '_' , letters, 'numbers'

For example:
    BS a = 5
    1 + (BS a = 5)

# 4. make boolean and comparation 
    False = 0
    True = 1

# 5. add if condition
    IF 1 THEN 2 ELIF 2 THEN 3 ELSE 4

# 6. add FOR loop and WHILE loop
    FOR <var_name> = <start_value> TO <end_value> THEN <expr>

    BS result = 1
    FOR i = 5 TO 0 STEP -1 THEN BS result = result * i
    FOR i = 1 TO 9 THEN 2^i


    WHILE <condition> THEN <expr>
    BS result = 5
    WHILE result > 0 THEN BS result = result -1
# 7. add FUNC 
    FUN add(a,b) -> a + b
    add(1,2)

    BS some_func = add
    some_func(1,2)

    FUN (a) -> a + 6
    BS some_func = FUN(a) -> a + 6
    some_func(12)

    FUN test(a) -> a / 0
    test(123)

    # Runtime Error: Division by zero

# 8. add String type
    "Text"
    "Text with \"quotes\"" -> Text with "quotes"
    "Text with \\ backslashes \\"   -> Text with \ backslashes \
    "Text \nwith \nnewlines"    ->  text 
                                    with
                                    newlines 

# 9. add List
    []
    [1, 2, 3]

    add
    [1, 2, 3] + 4 => [1, 2, 3, 4]
    
    concat
    [1, 2, 3] * [3, 4, 5] => [1, 2, 3, 4, 5]
    
    remove
    [1, 2, 3] - 1   => [1, 3]
    [1, 2, 3] - 0   => [2, 3]
    [1, 2, 3] - -1  => [1, 2]
    [1, 2, 3] - -2  => [1, 3]

    get
    [1, 2, 3] / 0  => 1
    [1, 2, 3] / 1  => 2
    [1, 2, 3] / -1  => 3


# 10. built-in Functions

    PRINT
    PRINT_RET
    INPUT
    INPUT_INT
    CLEAR
    IS_NUMBER
    IS_STRING
    IS_LIST
    IS_FUNCTION
    APPEND
    POP
    EXTEND

# 11. Multi-lines statements
    PRINT("world")
    PRINT("Hello"); PRINT("World")

    IF <expr> THEN
        <expr1>
        <expr2>
        <expr3>
    END
    
    FOR <expr> THEN
        <expr1>
        <expr2>
        <expr3>
    END

    FUN <name>()
        <expr1>
        <expr2>
        <expr3>
    END


    1 + 2; 3 + 4;
    BS result = IF 5 == 5 THEN "math works" ELSE "no";

    IF 5 == 5 THEN; PRINT("math"); PRINT("works") ELSE PRINT("broken")

# 12. RETURN , BREAK, CONTINUE
    FUN add(a,b)
        RETURN a + b
    END

    FUN example()
        #do stuff
        IF ...  THEN
            RETURN
        END
        #do more stuff
    END

    IF condition THEN RETURN


    FOR i = 0 TO 10
        IF somecodition THEN
            BREAK
        END

        IF someothercondition THEN
            CONTINUE
        END
    END


    FUN myfuncA() -> myvalue
    
    FUN myfuncB() 
        # statement1
        # statement2
        RETURN myvalue
    END

    FUN put5() -> 5

    FUN test()
        RETURN 5
    END
# Quit key word:  QSL >886