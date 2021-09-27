class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        if self.Root is not None:
            node = self.FindNode(ParentNode)
        else:
            return
        node.Children.append(NewChild)
        NewChild.Parent = node
        return
        # ваш код добавления нового дочернего узла существующему ParentNode

    def DeleteNode(self, NodeToDelete):
        if self.Root is not None:
            node = self.FindNode(NodeToDelete)
            if node == self.Root:
                self.Root = None
            else:
                node.Parent.Children.remove(node)
                del node
            return
        else:
            return
        # ваш код удаления существующего узла NodeToDelete

    def GetAllNodes(self):

        def appendnodetolist(x, s):
            s.append(x)
            for children in x.Children:
                appendnodetolist(children, s)
            return s

        if self.Root is not None:
            lst = []
            lst = appendnodetolist(self.Root, lst)
            return lst
        else:
            return [None]
        # ваш код выдачи всех узлов дерева в определённом порядке

    def FindNodesByValue(self, val):

        def findtreenodes(x, neededval, s):  # Воспользуемся рекурсией!
            if x.NodeValue == neededval:
                s.append(x)
            for children in x.Children:
                findtreenodes(children, neededval, s)
            return s

        if self.Root is not None:
            lst = []
            lst = findtreenodes(self.Root, val, lst)
            return lst
        else:
            return []
        # ваш код поиска узлов по значению

    def MoveNode(self, OriginalNode, NewParent):
        x = self.FindNode(OriginalNode)
        if x != self.Root:
            y = self.FindNode(NewParent)
            y.Children.append(x)
            x.Parent.Children.remove(x)
            x.Parent = y
            return
        else:
            return
        # ваш код перемещения узла вместе с его поддеревом --
        # в качестве дочернего для узла NewParent

    def Count(self):

        def countnodes(x, k):
            k.append(None)
            for child in x.Children:
                countnodes(child, k)
            return len(k)

        if self.Root is not None:
            length = []
            return countnodes(self.Root, length)
        else:
            return 0
        # количество всех узлов в дереве

    def LeafCount(self):

        def countleaves(x, k):
            if not x.Children:
                k.append(None)
            for children in x.Children:
                countleaves(children, k)
            return len(k)

        if self.Root is not None:
            leaves = []
            return countleaves(self.Root, leaves)
        else:
            return 0
        # количество листьев в дереве

    def FindNode(self, val):

        def findtreenode(x, needednode):
            lst = [x]
            while lst:
                for elem in lst:
                    if elem == needednode:
                        return elem
                    else:
                        lst.extend(elem.Children)
                    lst.remove(elem)

        if self.Root is not None:
            return findtreenode(self.Root, val)
        else:
            return


def form_ast(token_list):
    ast_tree = SimpleTree(SimpleTreeNode(None, None))
    cur_node = ast_tree.Root

    while token_list:
        el = token_list.pop(0)

        if el[1] == '(':
            cur_node.Children.append(SimpleTreeNode(None, cur_node))
            cur_node = cur_node.Children[0]

        elif el[1] == ')':
            cur_node = cur_node.Parent

        elif el[0] == 'число':
            cur_node.NodeValue = int(el[1])
            cur_node = cur_node.Parent

        elif el[0] == 'операция':
            cur_node.NodeValue = el[1]
            cur_node.Children.append(SimpleTreeNode(None, cur_node))
            cur_node = cur_node.Children[1]

    return ast_tree
