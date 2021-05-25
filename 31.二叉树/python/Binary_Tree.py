from graphviz import Digraph
from random import sample
import uuid

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BTree:
    def __init__(self, val=None, left=None, right=None):
        self.val = val    # 数据域
        self.left = left    # 左子树
        self.right = right  # 右子树
        self.dot = Digraph(comment='Binary Tree')

    # 前序遍历
    def preorder(self):
        array = []
        if self.val is not None:
            print(self.val, end=' ')
            array.append(self.val)
        if self.left is not None:
            array.append(self.left.preorder())
        if self.right is not None:
            array.append(self.right.preorder())
        return array

    # 中序遍历
    def inorder(self):

        if self.left is not None:
            self.left.inorder()
        if self.val is not None:
            print(self.val, end=' ')
        if self.right is not None:
            self.right.inorder()

    # 后序遍历
    def postorder(self):

        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        if self.val is not None:
            print(self.val, end=' ')

    # 层序遍历
    def levelorder(self):
        # 返回某个节点的左孩子
        def LChild_Of_Node(node):
            return node.left if node.left is not None else None
        # 返回某个节点的右孩子
        def RChild_Of_Node(node):
            return node.right if node.right is not None else None
        
        # 层序遍历列表
        level_order = []
        # 是否添加根节点中的数据
        if self.val is not None:
            level_order.append([self])
        # 二叉树的高度
        height = self.height()
        if height >= 1:
            # 对第二层及其以后的层数进行操作, 在level_order中添加节点而不是数据
            for _ in range(2, height + 1):
                level = []  # 该层的节点
                for node in level_order[-1]:
                    # 如果左孩子非空，则添加左孩子
                    if LChild_Of_Node(node):
                        level.append(LChild_Of_Node(node))
                    # 如果右孩子非空，则添加右孩子
                    if RChild_Of_Node(node):
                        level.append(RChild_Of_Node(node))
                # 如果该层非空，则添加该层
                if level:
                    level_order.append(level)
            # 取出每层中的数据
            for i in range(0, height):  # 层数
                for index in range(len(level_order[i])):
                    level_order[i][index] = level_order[i][index].val

        return level_order

    # 二叉树的高度
    def height(self):
        # 空的树高度为0, 只有root节点的树高度为1
        if self.val is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        elif self.left is None and self.right is not None:
            return 1 + self.right.height()
        elif self.left is not None and self.right is None:
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())

    # 二叉树的叶子节点
    def leaves(self):

        if self.val is None:
            return None
        elif self.left is None and self.right is None:
            print(self.val, end=' ')
        elif self.left is None and self.right is not None:
            self.right.leaves()
        elif self.right is None and self.left is not None:
            self.left.leaves()
        else:
            self.left.leaves()
            self.right.leaves()

    # 利用Graphviz实现二叉树的可视化
    def print_tree(self, save_path='./Binary_Tree.gv', label=False):

        # colors for labels of nodes
        colors = ['skyblue', 'tomato', 'orange',
                  'purple', 'green', 'yellow', 'pink', 'red']

        # 绘制以某个节点为根节点的二叉树
        def print_node(node, node_tag):
            # 节点颜色
            color = sample(colors, 1)[0]
            if node.left is not None:
                left_tag = str(uuid.uuid1())            # 左节点的数据
                self.dot.node(left_tag, str(node.left.val),
                              style='filled', color=color)    # 左节点
                label_string = 'L' if label else ''    # 是否在连接线上写上标签，表明为左子树
                self.dot.edge(node_tag, left_tag,
                              label=label_string)   # 左节点与其父节点的连线
                print_node(node.left, left_tag)

            if node.right is not None:
                right_tag = str(uuid.uuid1())
                self.dot.node(right_tag, str(node.right.val),
                              style='filled', color=color)
                label_string = 'R' if label else ''  # 是否在连接线上写上标签，表明为右子树
                self.dot.edge(node_tag, right_tag, label=label_string)
                print_node(node.right, right_tag)

        # 如果树非空
        if self.val is not None:
            root_tag = str(uuid.uuid1())                # 根节点标签
            self.dot.node(root_tag, str(self.val), style='filled',
                          color=sample(colors, 1)[0])     # 创建根节点
            print_node(self, root_tag)

        self.dot.render(save_path)                              # 保存文件为指定文件


def create_BTree_By_List(array):
    # 将原数组拆成层次遍历的数组，每一项都储存这一层所有的节点的数据
    level_order = []
    i = sum = 1
    while sum < len(array):
        level_order.append(array[i-1:2*i-1])
        i *= 2
        sum += i
    level_order.append(array[i-1:])  # 将数据分组

    def Create_BTree_One_Step_Up(BTree_list, forword_level):
        '''
        function: 根据已经分好组的列表创建二叉树
        BTree_list: 这一层所有的节点组成的列表
        forword_level: 上一层节点的数据组成的列表
        '''
        new_BTree_list = []
        for i, elem in enumerate(forword_level):
            root = BTree(elem)
            if 2*i < len(BTree_list):
                root.left = BTree_list[2*i]
            if 2*i+1 < len(BTree_list):
                root.right = BTree_list[2*i+1]
            new_BTree_list.append(root)

        return new_BTree_list

    if len(level_order) == 1:
        return BTree(level_order[0][0])
    else:  # 二叉树的层数大于1
        # 创建最后一层的节点列表
        BTree_list = [BTree(elem) for elem in level_order[-1]]
        # 从下往上，逐层创建二叉树
        for i in range(len(level_order)-2, -1, -1):
            BTree_list = Create_BTree_One_Step_Up(
                BTree_list, level_order[i])
        return BTree_list[0]
