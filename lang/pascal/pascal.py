from talon import Context, Module, actions, settings

mod = Module()

ctx = Context()
ctx.matches = r"""
tag: user.pascal
mode: command
"""

ctx.tags = [
    'user.code_operators',
    'user.code_generic',
    'user.code_functions_gui',
    'user.code_imperative',
    'user.code_data_bool',
    'user.code_comment_line',
    'user.code_comment_block',
    'user.code_object_orientedcode_comment_block',
    'user.code_object_oriented',
    'user.code_operators_array',
    'user.code_operators_assignment',
    'user.code_operators_assignment',
    'user.code_operators_lambda',
    'user.code_operators_math',
    'user.code_operators_pointer']

ctx.lists["self.pascal_types"] = {
    "character": "char",
    "char": "char",
    "string": "string",
    "int": "Integer",
    "integer": "Integer",
    "double": "Double",
    "record": "Record",
    "float": "Float",
    "boolean": "Boolean",
}

ctx.lists["self.pascal_scope"] = {
    "global": "F",
    "local": "L",
    "input": "A",
}

ctx.lists["self.pascal_constness"] = {
    "constant": "const",
    "out": "out",
    "variable": "var",
}

ctx.lists["user.code_libraries"] = {
    "system math": "System.Math",
}

ctx.lists["user.code_functions"] = {
    "increase": "Inc",
    "decrease": "Dec",
}

mod.list("pascal_types", desc="Common Pascal types")
mod.list("pascal_constness", desc="Common Pascal types")
mod.list("pascal_scope", desc="Common Pascal types")


@mod.capture(rule="{self.pascal_types}")
def pascal_types(m) -> str:
    "Returns a string"
    return m.pascal_types


@mod.capture(rule="[<self.pascal_constness>] [<self.pascal_scopes>] <self.pascal_types>")
def pascal_variable(m) -> str:
    "Returns a string"
    text = " ".join(list(m)[:-1])
    text = text + "[|]: {}".format(list(m)[-1])
    return text


@ctx.action_class("user")
class UserActions:
    def code_operator_indirection(): actions.auto_insert("^")
    def code_operator_address_of(): actions.auto_insert("@")
    def code_operator_structure_dereference(): actions.auto_insert("^")
    def code_operator_lambda(): actions.auto_insert("")

    def code_operator_subscript():
        actions.insert("[]")
        actions.key("left")

    def code_operator_assignment(): actions.auto_insert(" := ")
    def code_operator_subtraction(): actions.auto_insert(" - ")

    def code_operator_subtraction_assignment():
        actions.insert("Dec()")
        actions.key("left")

    def code_operator_addition(): actions.auto_insert(" + ")

    def code_operator_addition_assignment():
        actions.insert("Inc()")
        actions.key("left")

    def code_operator_multiplication(): actions.auto_insert(" * ")
    def code_operator_multiplication_assignment(): actions.auto_insert("")

    def code_operator_exponent():
        actions.insert("Power(,)")
        actions.key("left")
        actions.key("left")

    def code_operator_division(): actions.auto_insert(" / ")
    def code_operator_division_assignment(): actions.auto_insert("")
    def code_operator_modulo(): actions.auto_insert(" mod ")
    def code_operator_modulo_assignment(): actions.auto_insert("")
    def code_operator_equal(): actions.auto_insert(" = ")
    def code_operator_not_equal(): actions.auto_insert(" <> ")
    def code_operator_greater_than(): actions.auto_insert(" > ")
    def code_operator_greater_than_or_equal_to(): actions.auto_insert(" >= ")
    def code_operator_less_than(): actions.auto_insert(" < ")
    def code_operator_less_than_or_equal_to(): actions.auto_insert(" <= ")
    def code_operator_and(): actions.auto_insert(" and ")
    def code_operator_or(): actions.auto_insert(" or ")
    def code_operator_bitwise_and(): actions.auto_insert(" and ")
    def code_operator_bitwise_and_assignment(): actions.auto_insert("")
    def code_operator_bitwise_or(): actions.auto_insert(" or ")
    def code_operator_bitwise_or_assignment(): actions.auto_insert("")
    def code_operator_bitwise_exclusive_or(): actions.auto_insert(" xor ")
    def code_operator_bitwise_exclusive_or_assignment(): actions.auto_insert("")
    def code_operator_bitwise_left_shift(): actions.auto_insert(" lsh ")
    def code_operator_bitwise_left_shift_assignment(): actions.auto_insert("")
    def code_operator_bitwise_right_shift(): actions.auto_insert(" rsh ")
    def code_operator_bitwise_right_shift_assignment(): actions.auto_insert("")
    def code_self(): actions.auto_insert("")
    def code_insert_null(): actions.auto_insert("nil")

    def code_insert_is_null():
        actions.insert(" and Assigned()")
        actions.key("left")

    def code_insert_is_not_null():
        actions.insert("Assigned()")
        actions.key("left")

    def code_state_if():
        actions.insert("if then")
        actions.edit.word_left()
        actions.key("space")
        actions.edit.left()

    def code_state_else_if():
        actions.insert("else if then")
        actions.edit.word_left()
        actions.key("space")
        actions.edit.left()

    def code_state_else():
        actions.insert("else")
        actions.key("enter")

    def code_state_switch(): actions.auto_insert("")

    def code_state_case():
        actions.insert("case of\nend;")
        actions.edit.word_left()
        actions.key("up")

    def code_state_for(): 
        actions.insert("for := to do")
        actions.edit.word_left()
        actions.edit.word_left()
        actions.edit.word_left()
        actions.key("space")
        actions.edit.left()

    def code_state_for_each():
        actions.insert("for in ")
        actions.key("left")
        actions.edit.word_left()
        actions.key("space")
        actions.edit.left()

    def code_state_while():
        actions.insert("while do")
        actions.edit.word_left()
        actions.key("space")
        actions.edit.left()

    def code_define_class():
        actions.insert("= class;")
        actions.edit.word_left()
        actions.edit.word_left()
        actions.key("space")
        actions.edit.left()

    def code_import():
        actions.insert(";")
        actions.edit.left()

    def code_comment_line_prefix(): actions.auto_insert("// ")
    def code_state_return(): actions.insert("Result := ")
    def code_insert_true(): actions.auto_insert("True")
    def code_insert_false(): actions.auto_insert("False")

    def code_comment_block():
        actions.insert("{")
        actions.key("enter")
        actions.key("enter")
        actions.insert("}")
        actions.edit.up()

    def code_comment_block_prefix(): actions.auto_insert("{")
    def code_comment_block_suffix(): actions.auto_insert("}")


@mod.action_class
class PascalFunctions:
    def pascal_insert_function(text: str, selection: str):
        """Insert public function"""
        if selection:
            text = text + "({})".format(selection)
        else:
            text = text + "()"

        actions.user.paste(text)
        actions.edit.left()

    def pascal_private_function(text: str):
        """Inserts private function declaration"""
        result = "function {}(): ;".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.insert(result)
        actions.key("left:4")

    def pascal_private_procedure(text: str):
        """Inserts private procedure declaration"""
        result = "procedure {}();".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.insert(result)
        actions.key("left:2")


# @mod.action_class
# class module_actions:
#     # TODO this could go somewhere else
#     def insert_cursor(text: str):
#         """Insert a string. Leave the cursor wherever [|] is in the text"""
#         if "[|]" in text:
#             end_pos = text.find("[|]")
#             s = text.replace("[|]", "")
#             actions.insert(s)
#             actions.key(f"left:{len(s) - end_pos}")
#         else:
#             actions.insert(text)
