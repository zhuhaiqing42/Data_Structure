#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: zhuhaiqing
'''
def max_heapify(heap, heap_size, root):
    # 此函数为建立最大堆函数, 使得根节点比左右叶子节点大
    left = 2*root + 1
    right = left + 1
    larger = root
    if left < heap_size and heap[left] > heap[larger]:
        larger = left # larger只是记录比根节点大的值的位置,下面再做交换
    if right < heap_size and heap[right] > heap[larger]:
        larger = right
    if larger != root:
        heap[root], heap[larger] = heap[larger], heap[root] #将更大的那个节点与根节点交换
        max_heapify(heap, heap_size, larger) # 以lager为根节点,重新调整堆


def build_max_heap(heap):
    # 这是一个创建最大堆的函数, 通过循环每一个根节点(反复调用max_heapify函数), 来调整堆
    heap_size = len(heap)
    for i in range((heap_size-2)//2, -1, -1):
        max_heapify(heap, heap_size, i)


def heap_sort(heap):
    build_max_heap(heap) # 把无序二叉树转化成最大堆
    for i in range(len(heap)-1, -1, -1):
        heap[i], heap[0] = heap[0], heap[i] # 将二叉树末尾元素与根节点元素交换
        max_heapify(heap, i, 0) # 交换完后重新调整最大堆
    return heap


if __name__ == '__main__':
    a = [49,38,65,97,76,13,27,49]
    print(a)
    heap_sorted = heap_sort(a)
    print(heap_sorted)

