mode: user.pascal
mode: command
and code.language: pascal
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

action(user.code_operator_indirection): "^"
action(user.code_operator_address_of): "@"
action(user.code_operator_structure_dereference): "^"
action(user.code_operator_lambda): ""
action(user.code_operator_subscript):
    insert("[]")
    key(left)
action(user.code_operator_assignment): " := "
action(user.code_operator_subtraction): " - "
action(user.code_operator_subtraction_assignment):
    insert("Dec()")
    key(left)
action(user.code_operator_addition): " + "
action(user.code_operator_addition_assignment):
    insert("Inc()")
    key(left)
action(user.code_operator_multiplication): " * "
action(user.code_operator_multiplication_assignment): ""
action(user.code_operator_exponent):
    insert("Power(,)")
    key(left)
    key(left)
action(user.code_operator_division): " / "
action(user.code_operator_division_assignment): ""
action(user.code_operator_modulo): " mod "
action(user.code_operator_modulo_assignment): ""
action(user.code_operator_equal): " = "
action(user.code_operator_not_equal): " <> "
action(user.code_operator_greater_than): " > "
action(user.code_operator_greater_than_or_equal_to): " >= "
action(user.code_operator_less_than): " < "
action(user.code_operator_less_than_or_equal_to): " <= "
action(user.code_operator_and): " and "
action(user.code_operator_or): " or "
action(user.code_operator_bitwise_and): " and "
action(user.code_operator_bitwise_and_assignment): ""
action(user.code_operator_bitwise_or): " or "
action(user.code_operator_bitwise_or_assignment): ""
action(user.code_operator_bitwise_exclusive_or): " xor "
action(user.code_operator_bitwise_exclusive_or_assignment): ""
action(user.code_operator_bitwise_left_shift): " lsh "
action(user.code_operator_bitwise_left_shift_assignment): ""
action(user.code_operator_bitwise_right_shift): " rsh "
action(user.code_operator_bitwise_right_shift_assignment): ""
action(user.code_self): ""
action(user.code_null): "nil"
action(user.code_is_null):
    insert(" and Assigned()")
    key(left)
action(user.code_is_not_null):
    insert("Assigned()")
    key(left)
action(user.code_state_if):
    insert("if then")
    edit.word_left()
    key(space)
    edit.left()
action(user.code_state_else_if):
    insert("else if then")
    edit.word_left()
    key(space)
    edit.left()
action(user.code_state_else):
    insert("else")
    key(enter)
action(user.code_state_switch): ""
action(user.code_state_case):
    insert("case of\nend;")
    edit.word_left()
    key(up)
action(user.code_state_for): 
    insert("for := to do")
    edit.word_left()
    edit.word_left()
    edit.word_left()
    key(space)
    edit.left()
action(user.code_state_for_each):
    insert("for in ")
    key(left)
    edit.word_left()
    key(space)
    edit.left()
action(user.code_state_while):
    insert("while do")
    edit.word_left()
    key(space)
    edit.left()
action(user.code_type_class):
    insert("= class;")
    edit.word_left()
    edit.word_left()
    key(space)
    edit.left()
action(user.code_import):
    insert(";")
    edit.left()
action(user.code_from_import): ""
action(user.code_comment): "// "
action(user.code_state_return):
	insert("Result := ")
action(user.code_true): "True"
action(user.code_false): "False"
action(user.code_block_comment):
    insert("{")
    key(enter)
    key(enter)
    insert("}")
    edit.up()
action(user.code_block_comment_prefix): "{"
action(user.code_block_comment_suffix): "}"

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
