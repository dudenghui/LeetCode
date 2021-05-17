# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 15:57:24 2021
@author: https://www.jianshu.com/p/b1817c75c268

python实现单链表参考
"""

#首先定义节点类Node
class LinkNode(object):
    #1. __init__初始化结点信息
    def __init__(self, data, pnext=None):
        '''
        data:节点保存的数据
        '''
        self.data = data
        self._next = pnext
    #2. 用于定义Node的字符输出
    def __repr__(self):
        '''
        用于定义Node的字符输出，
        print为输出data
        '''
        return str(self.data)

#初始化链表的类
class LinkList(object):
    #1. 初始化链表
    def __init__(self):
        #属性：链表头head,链表长度length
        self.head = None
        self.length = 0

    #2. 链表初始化函数，尾插法，插入data
    def initlist_tail(self, data):
        #创建头结点，其实是第一个有值节点
        self.head = LinkNode(data[0])
        pnext = self.head
        for i in data[1:]:
            node = LinkNode(i)
            pnext.next = node
            pnext = pnext.next

        self.length = len(data)

    #3. 判断链表是否为空
    def isEmpty(self):
        return (self.length == 0)

    #4. 增加一个节点（在链为添加）
    def append(self, dataOrNode):
        '''在链表尾添加'''
        item = None
        if isinstance(dataOrNode, LinkNode):
            item = dataOrNode
        else:
            item = LinkNode(dataOrNode)

        if not self.head:
            self.head = item
            self.length += 1
        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = item
            self.length += 1

    #5. 删除一个节点： delete()
    def delete(self, index):
        '''
        删除一个节点，需要把链表长度减一
        '''
        if self.isEmpty():
            print("this linked list is empty.")
            return

        if index < 0 or index >= self.length:
            print('error: out of index')
            return
        '''
        要注意删除第一个节点的情况
        '''
        if index == 0:
            self.head = self.head._next
            self.length -= 1
            return
        '''
        prev为保存前导节点
        node为保存当前节点
        '''
        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1
        if j == index:
            prev.next = node._next
            self.length -= 1

    #6. 修改一个节点： update()
    def update(self, index, data):
        '''修改一个节点'''
        if self.isEmpty() or index < 0 or index >= self.length:
            print("error: out of index")
            return

        j = 0
        node = self.head
        while node.next and j < index:
            node = node._next
            j += 1

        if j == index:
            node.data = data

    #7. 查找一个节点: getItem()
    def getItem(self, index):
        '''查找节点'''
        if self.isEmpty() or index < 0 or index >= self.length:
            print("error: out of index")
            return

        j = 0
        node = self.head

        while node._next and j < index:
            node = node._next
            j += 1

        return node.data

    #8. 查找一个节点的索引： getIndex()
    def getIndex(self, data):
        '''查找索引'''
        j = 0
        if self.isEmpty():
            print("this linked list is empty")
            return

        node = self.head
        while node:
            if node.data == data:
                return j
            node = node._next
            j += 1

        if j == self.length:
            print("%s not found" % str(data))
            return

    #9. 查找一个节点：insert()
    def insert(self, index, dataOrNode):
        if self.isEmpty():
            print("this linked list is empty")
            return

        if index < 0 or index >= self.length:
            print("error: out of index")
            return

        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if index == 0:
            item._next = self.head
            self.head = item
            self.length += 1
            return
        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1
        if j == index:
            item._next = node
            prev._next = item
            self.length += 1

    #10. 清空链表
    def clear(self):
        '''清空链表'''
        self.head = None
        self.length = 0

    #11. 取链表长度
    def getLength(self):
        return self.length

    #12. 在索引值为 index 的结点后插入结点key
    def insertElem(self, key, index):
        pnext = self.head
        j = 1
        while pnext and j < index:
            pnext = pnext.next
            j += 1
        if(pnext == 0 or j > index):  # 若出错则退出
            exit(0)
            print('insert error')
        node = LinkNode(key)
        node.next = pnext.next
        pnext.next = node
        print('inserted LinkList:')
        self.ReadList()

    #13. 删除第 index个 结点后的那一个节点
    def deleteElem(self, index):
        pnext = self.head
        j = 1
        while pnext and j < index:
            pnext = pnext.next
            j += 1
        if(pnext == 0 or j > index):  # 若出错则退出
            exit(0)
            print('insert error')
        q = pnext.next
        pnext.next = q.next
        print('deleted LinkList:')
        self.ReadList()

    #14. 链表逆序
    def reverseList(self):
        pnext = self.head

    def __repr__(self):
        if self.isEmpty():
            return "empty chain table"
        node = self.head
        nlist = ''
        while node:
            nlist += str(node.data) + ' '
            node = node._next
        return nlist

    def __getitem__(self, ind):
        if self.isEmpty() or ind < 0 or ind >= self.length:
            return "error: out of index"
        return self.getItem(ind)

    def __setitem__(self, ind, val):
        if self.isEmpty() or ind < 0 or ind >= self.length:
            return "error: out of index"
        self.update(ind, val)

    def __len__(self):
        return self.length
