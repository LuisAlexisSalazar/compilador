# -*- coding: utf-8 -*-
from queue import LifoQueue

from anytree import Node, RenderTree
from anytree.exporter import DotExporter

from ll1.functions import parse_bnf, pprint_table

from tools.tool import print_color
from termcolor import colored


class Stack(LifoQueue):
    """Symbol stack."""

    def peek(self):
        """Returns top of stack."""
        if len(self.queue) == 0:
            return None
        return self.queue[len(self.queue) - 1]


def parse(grammar, words, catch_bugs=False):
    """Parse function"""
    grammar = parse_bnf(grammar)
    table, ambiguous = grammar.parsing_table(is_clean=True)

    pprint_table(grammar, table)
    if ambiguous:
        raise Warning("Ambiguous grammar")

    error_list = []

    words.append("$")
    word = words.pop(0)
    stack = Stack()

    stack.put(("$", None))
    # ------------------
    key = 0
    root = Node(0, display_name=grammar.start)
    # ----------------
    stack.put((grammar.start, root))

    top_stack = stack.peek()
    while True:
        # print(f"Current_word:{word},  Stack:{stack.queue}")
        if top_stack[0] == "$" and word == "$":
            if not error_list:
                return True, root, None
            else:
                return False, root, error_list

        if grammar.is_terminal(top_stack[0]):
            if top_stack[0] == word:
                # print(f"Consume input: {word}")
                stack.get()
                word = words.pop(0)
            else:
                error_list.append(f"Expected {top_stack[0]}")
                while word != top_stack[0]:
                    if word == "$":
                        return False, root, error_list
                    word = words.pop(0)
        else:
            rule = table.get((top_stack[0], word))
            stack.get()
            if rule:
                # print(f"Rule: {rule}")
                symbols = rule.body[::-1]

                for symbol in symbols:

                    # ------------------
                    key += 1
                    node = Node(key, parent=top_stack[1], display_name=symbol)
                    # ------------------
                    if symbol != "#":
                        stack.put((symbol, node))
            else:
                error_list.append(f"Unexpected character:{word}. Expected: {grammar.first(top_stack[0])}")
                follow = grammar.follow(top_stack[0]) + ["$"]
                if catch_bugs:
                    print(colored("Error! Sync set -> ", "red"),end="")
                    print_color(f"{follow}", "magenta")
                while word not in follow:
                    # print(f"Skipped: {word}")
                    word = words.pop(0)
        top_stack = stack.peek()


def parse_tree(grammar, words):
    result, tree, errors = parse(grammar, words, True)
    if not result:
        print_color("No pertenece a la gramatica", "red")
        return
    else:
        print_color("Exito si pertenece a la gramatica", "blue")
        # --print console
        # for pre, fill, node in RenderTree(tree):
        #     print(f"{pre}{node.name}")

        DotExporter(tree, nodeattrfunc=lambda node: 'label="{}"'.format(node.display_name)).to_picture("graph.png")
        # DotExporter(tree).to_picture("out.png")
        # --Safe
        # DotExporter(tree).to_dotfile('tree.dot')
        # In cmd "dot -Tpng tree.dot > output.png"
