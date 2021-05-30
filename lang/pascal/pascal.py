from talon import Context, Module, actions, settings

mod = Module()

ctx = Context()
ctx.matches = r"""
mode: user.pascal
mode: command
and code.language: pascal
"""

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
