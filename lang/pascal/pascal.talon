tag: user.pascal
mode: command
-
tag(): user.code_operators
tag(): user.code_comment
tag(): user.code_block_comment
tag(): user.code_generic

settings():
    user.code_private_function_formatter = "PUBLIC_CAMEL_CASE"
    user.code_protected_function_formatter = "PUBLIC_CAMEL_CASE"
    user.code_public_function_formatter = "PUBLIC_CAMEL_CASE"
    user.code_private_variable_formatter = "PUBLIC_CAMEL_CASE"
    user.code_protected_variable_formatter = "PUBLIC_CAMEL_CASE"
    user.code_public_variable_formatter = "PUBLIC_CAMEL_CASE"


state begin: "begin"
state end: "end"
state begin end:
    insert("begin")
    key(enter)
    key(enter)
    insert("end")
    edit.up()

^funky <user.text>$: user.pascal_private_function(text)
^procedure <user.text>$: user.pascal_private_procedure(text)

state over right: "override;"
state override: "override;"
state virtual: "virtual;"
state abstract: "abstract;"
state overload: "overload;"
state public: "public"
state protected: "protected"
state private: "private"
state strict: "strict"

state interface: "interface"
state implementation: "implementation"
state type: "type"
state uses: 
    insert("uses")
    key(enter)
    insert("  ;")
    edit.left()


state constant: "const"
state variable: "var"
state out: "out"

state exit: "EXIT;"    
state continue: "CONTINUE;"    
state break: "BREAK;"    

type <user.pascal_types>: "{pascal_types}"
# <user.pascal_variable> <phrase>: 
#     user.insert_cursor("{pascal_variable}", "{phrase}")