# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 20:45:57 2021
@author: DDH

有关图的建立(邻接矩阵和邻接表)、
最短路径算法(Dijkstra和Floyed)、
深度优先遍历(DFS)和广度优先遍历(BFS)等
"""

# Dijkstra算法: 找到某节点到所有节点之间的最短距离
# https://zhuanlan.zhihu.com/p/63395403
import sys
import xlrd
from pylab import *

def dijkstra(start: int, mgraph: list) -> list:
    passed = [start]
    nopass = [x for x in range(len(mgraph)) if x != start]
    dis = mgraph[start]
    while len(nopass):  # 每循环一次,更新一次dis
        idx = nopass[0]
        for i in nopass:
            if dis[i] < dis[idx]:
                idx = i  # 找到最小的那个节点
        nopass.remove(idx)
        passed.append(idx)
        for i in nopass:
            if dis[idx] + mgraph[idx][i] < dis[i]:
                dis[i] = dis[idx] + mgraph[idx][i]
    return dis


# Floyed算法
def matrix(address):  # 读取excel生成邻接矩阵
    wb = xlrd.open_workbook(address)
    sheet1 = wb.sheet_by_name('邻接矩阵_距离')
    L = []
    for i in range(1, 13):
        a = sheet1.row_values(i)
        a.remove(a[0])
        L.append([int(x) for x in a])
    return L
# chararray = ['A','B','C','D','E','F','G','H','I','J','K','L']
# L=[]
# for i in range(1,len(chararray)+1):
#     L.append('v%d'%i)
# Dict=dict(zip(L,chararray))
# print('各点对应关系：')
# print(Dict)
# address = r'D:\LeetCode\71.图\python\Floyed.xlsx'
# data=matrix(address)
# d=matrix.tran_m(data)
# floyd(d)

def floyed(d, isDirection=True):
    D = d  # 记录最短距离
    lengthD = len(D)  # 邻接矩阵大小
    p = list(range(lengthD))
    P = [p] * lengthD  # 记录路径前驱节点,初始化p[i,j]=i
    P = array(P)  # array --- 高效的数值数组
    '''<核心代码>'''
    for k in range(lengthD):
        for i in range(lengthD):
            for j in range(lengthD):
                if(D[i][j] > D[i][k]+D[k][j]):
                    P[i][j] = k  # 记录新路径的前驱
                    D[i][j] = D[i][k]+D[k][j]  # 更新最短路径
    '''<\核心代码>'''
    if isDirection:
        print('各个顶点的最短路径(有向图):')
        for i in range(lengthD):
            for j in range(lengthD):
                if i != j:
                    print(
                        f'v{i+1}--v{j+1}  dist_min: {D[i][j]}\tpath:v{i+1}', end='')
                    temp = P[i][j]
                    while (temp != j):
                        print('--'+'v%d' % (temp+1), end='')
                        temp = P[temp][j]
                    print('--'+'v%d' % (j+1))
    else:
        print('各个顶点的最短路径(无向图):')
        for i in range(lengthD):
            for j in range(i+1, lengthD):
                print(
                    f'v{i+1}--v{j+1}  dist_min: {D[i][j]}\tpath:v{i+1}', end='')
                temp = P[i][j]
                while (temp != j):
                    print('--'+'v%d' % (temp+1), end='')
                    temp = P[temp][j]
                print('--'+'v%d' % (j+1))

    print('前驱矩阵P:\n', P)
    return array(D)


## Dijkstra算法流程
'''
邻接矩阵如下：
[[0   1  12 999 999 999]
 [999   0   9   3 999 999]
 [999 999   0 999   5 999]
 [999 999   4   0  13  15]
 [999 999 999 999   0   4]
 [999 999 999 999 999   0]]
现从0出发
nopass = [1, 2, 3, 4, 5]
passed = [0]
从0到各点最短路径为dis = [0   1  12 999 999 999]

dis中未经过的点距离最短的为1, idx = 1
nopass = [2, 3, 4, 5]
passed = [0, 1]
base = dis[idx] = 1
line = mgraph[idx] = [999   0   9   3 999 999]
发现经过1点到2点的距离更短，更新dis[2] = 1 + 9
发现经过1点到3点的距离更短，更新dis[3] = 1 + 3
从0到各点最短路径为dis = [0   1  10   4 999 999]

dis中未经过的点距离最短的为4, idx = 3
nopass = [2, 4, 5]
passed = [0, 1, 3]
base = dis[idx] = 4
line = mgraph[idx] = [999 999   4   0  13  15]
发现经过3点到2点的距离更短，更新dis[2] = 4 + 4
发现经过3点到4点的距离更短，更新dis[4] = 4 + 13
发现经过3点到5点的距离更短，更新dis[5] = 4 + 15
从0到各点最短路径为dis = [0  1  8  4 17 19]

dis中未经过的点距离最短的为8, idx = 2
nopass = [4, 5]
passed = [0, 1, 3, 2]
base = dis[idx] = 8
line = mgraph[idx] = [999 999   0 999   5 999]
发现经过2点到4点的距离更短，更新dis[4] = 8 + 5
从0到各点最短路径为dis = [0  1  8  4 13 19]

dis中未经过的点距离最短的为13, idx = 4
nopass = [5]
passed = [0, 1, 3, 2, 4]
base = dis[idx] = 13
line = mgraph[idx] = [999 999 999 999   0   4]
发现经过4点到5点的距离更短，更新dis[5] = 13 + 4
从0到各点最短路径为dis = [0  1  8  4 13 17]

dis中未经过的点距离最短的为17, idx = 5
nopass = []
passed = [0, 1, 3, 2, 4, 5]
从0到各点最短路径为dis = [0  1  8  4 13 17]
'''
# https://blog.csdn.net/weixin_40274123/article/details/94578400
#1 利用栈实现
#2 从源节点开始把节点按照深度放入栈，然后弹出
#3 每弹出一个点，把该节点下一个没有进过栈的邻接点放入栈
#4 直到栈变空
def dfs(node):
    if node is None:
        return
    stack = []  # 建立空栈、建立空集合
    nodeSet = set()
    nodeSet.add(node)
    stack.append(node)
    while len(stack) > 0:
        cur = stack.pop()  # 弹出最近入栈的节点
        for n in cur.neighbors:  # 遍历该节点的邻接节点
            if n not in nodeSet:
                # 把节点压入 邻接节点压入 登记节点 打印节点值 退出当前循环
                stack.append(n)
                nodeSet.add(n)
                break
    return nodeSet


'''邻接矩阵'''
class DenseGraph:
    def __init__(self, n, directed=False):
        self.n = n  # number of vertex
        self.m = 0  # number of edge
        self.directed = directed
        self.matrix = [[0 for i in range(n)] for i in range(n)]

    def __str__(self):
        for line in self.matrix:
            print(str(line))
        return ''  # must return string

    def getNumberOfEdge(self):
        return self.m

    def getNumberOfVertex(self):
        return self.n

    def hasEdge(self, v, w):
        if 0 <= v <= self.n and 0 <= w <= self.n:
            return self.matrix[v][w]
        else:
            raise Exception("vertex not in the Graph")

    def addEdge(self, v, w):
        if 0 <= v <= self.n and 0 <= w <= self.n:
            if self.hasEdge(v, w):
                return
            self.matrix[v][w] = 1
            if self.directed is False:
                self.matrix[w][v] = 1
            self.m += 1
        else:
            raise Exception("vertex not in the Graph")


'''邻接表'''


class Vertex(object):
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}  # the key is vertex,value is weight

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getConnectionsId(self):
        idList = []
        for k in self.connectedTo.keys():
            idList.append(k.getId())
        return sorted(idList)

    def getConnectionsIdAndWeight(self):
        idList = []
        for k in self.connectedTo.keys():
            idList.append(k.getId())
        weightList = list(self.connectedTo.values())
        return {idList[i]: weightList[i] for i in range(len(idList))}

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def getId(self):
        return self.id


class SparseGraph(object):
    def __init__(self, directed=False, weighted=False):
        self.vertDict = {}  # key is the id of vertex，value is vertex
        self.numVertices = 0
        self.directed = directed
        self.weighted = weighted

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertDict[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertDict:
            return self.vertDict[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertDict

    def addEdge(self, f, t, weight=0):
        if f not in self.vertDict:
            self.addVertex(f)
        if t not in self.vertDict:
            self.addVertex(t)
        self.vertDict[f].addNeighbor(self.vertDict[t], weight)
        if self.directed is False:
            self.vertDict[t].addNeighbor(self.vertDict[f], weight)

    def getVertices(self):
        return list(self.vertDict.keys())

    def getVertNum(self):
        return self.numVertices

    def __iter__(self):
        return iter(self.vertDict.values())

    def getAllInfo(self):
        verticesList = [int(x) for x in list(self.getVertices())]
        verticesList.sort()
        if self.weighted:
            for i in range(len(verticesList)):
                print('vertex %s : %s' %
                      (i, self.getVertex(i).getConnectionsIdAndWeight()))
        else:
            for i in range(len(verticesList)):
                print('vertex %s : %s' %
                      (i, self.getVertex(i).getConnectionsId()))


def buildGraphFromFile(aGraph, filePath):
    graphList = []
    with open(filePath, 'r', encoding='utf-8') as f:
        for line in f:
            graphList.append([int(x) for x in re.split(r'\s+', line.strip())])
    for i in range(len(graphList)):
        aGraph.addEdge(graphList[i][0], graphList[i][1])


def main():
    g1 = DenseGraph(13)  # 必须填入正确的结点个数。。。我真的觉得邻接矩阵不好用
    buildGraphFromFile(g1, r'D:\LeetCode\71.图\python\data.txt')
    print(g1)
    g2 = SparseGraph()
    buildGraphFromFile(g2, r'D:\LeetCode\71.图\python\data.txt')
    print(g2.getAllInfo())








