#运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。 
#
# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。 
#写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。 
#
# 进阶: 
#
# 你是否可以在 O(1) 时间复杂度内完成这两种操作？ 
#
# 示例: 
#
# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
#
#cache.put(1, 1);
#cache.put(2, 2);
#cache.get(1);       // 返回  1
#cache.put(3, 3);    // 该操作会使得密钥 2 作废
#cache.get(2);       // 返回 -1 (未找到)
#cache.put(4, 4);    // 该操作会使得密钥 1 作废
#cache.get(1);       // 返回 -1 (未找到)
#cache.get(3);       // 返回  3
#cache.get(4);       // 返回  4
# 
# Related Topics 设计



#leetcode submit region begin(Prohibit modification and deletion)
'''
doubly linked list
'''
class DLinkedNode:
    def __init__(self):
        self.key = 0
        self.val = 0
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._move_to_head(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.cache.get(key)
        if not node:
            new_node = DLinkedNode()
            new_node.key = key
            new_node.val = value

            self.cache[key] = new_node
            self._add_node(new_node)
            self.size += 1
            if self.size > self.capacity:
                # pop tail
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # update value
            node.val = value
            self._move_to_head(node)

    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        node = self.tail.prev
        self._remove_node(node)
        return node

''' OrderedDict == LinkedHashMap
    get/in/set/move_to_end/popitem == get/containsKey/put/remove in O(1)
'''
from collections import OrderedDict
class LRUCacheII(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
#leetcode submit region end(Prohibit modification and deletion)
