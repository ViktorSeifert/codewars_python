from collections import defaultdict


openers = ["(", "[", "{"]
closers = [")", "]", "}"]


class AtomDescription(object):
    def __init__(self, parent, name=""):
        self.name = name
        self.count = 1
        self.parent = parent

    def mul(self, number):
        self.count *= number


class CompoundAtomDescription(object):
    def __init__(self, parent=None):
        self.children = []
        self.parent = parent

    def add_child_atom_with_name(self, name):
        atom = AtomDescription(self, name)
        self.children.append(atom)

    def add_to_last_child_name(self, string):
        self.children[-1].name += string

    def add_compound_child(self):
        child = CompoundAtomDescription(self)
        self.children.append(child)
        return child

    def multiply_count(self, number):
        self.children[-1].mul(number)

    def mul(self, number):
        for child in self.children:
            child.mul(number)

    def flat_child_list(self):
        return ChildOnlyIterator(self)


class ChildOnlyIterator(object):
    def __init__(self, compound_def):
        self.compound_def = compound_def

    def __iter__(self):
        for child in self.compound_def.children:
            if isinstance(child, AtomDescription):
                yield child
            else:
                for grandchild in ChildOnlyIterator(child):
                    yield grandchild


class FormulaProcessor(object):
    def __init__(self):
        self.atoms = CompoundAtomDescription()

    def process(self, formula):
        for token in self.split_formula(formula):
            if token.isupper():
                self.atoms.add_child_atom_with_name(token)
            elif token.islower():
                self.atoms.add_to_last_child_name(token)
            elif token in openers:
                self.step_down()
            elif token in closers:
                self.step_up()
            elif token.isdigit():
                self.atoms.multiply_count(int(token))

    def step_down(self):
        self.atoms = self.atoms.add_compound_child()

    def step_up(self):
        self.atoms = self.atoms.parent

    def counts(self):
        result = defaultdict(lambda: 0)

        for atom in self.atoms.flat_child_list():
            result[atom.name] += atom.count

        return result

    @staticmethod
    def split_formula(formula):
        result = [""]

        for token in formula:
            if not (token.isdigit() and result[-1].isdigit()):
                result.append("")

            result[-1] += token

        return result


def parse_molecule(formula):
    fp = FormulaProcessor()
    fp.process(formula)
    return fp.counts()


print(parse_molecule("K4[ON(SO3)2]2"))
print(parse_molecule("C6H12O6"))
