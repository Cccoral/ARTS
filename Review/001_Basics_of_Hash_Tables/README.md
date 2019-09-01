[原文出处（Basics of Hash Tables)](https://www.hackerearth.com/zh/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/ "Basics of Hash Tables")
# Summary
- hash是一项被用来从一组相似对象中唯一识别某一特殊对象的技术。
- 为存储键值对，可以用一些简单的数组：一个数据结构（key作为一个索引存储数值）。若keys值较大并且无法直接作为一个索引值，需要用到hashing.
- **Hashing 优点**：节约空间，提高效率。结合了数组与链表优势
- **hashing 思路**：在一个数组中均匀地分布这些项（键值对）.每个项的key，利用算法（hash function）可以计算出一个index索引值，可以在O(1)时间内找到该元素。
- **Hashing 通常由两步组成：**<br>
1. 一个元素通过hash function 转换成一个整型数值。这个元素可以被用来作为存储该原始元素（存在hash table）的index索引值
2. 转换的这个元素通过hashed key也被存入hash table，便于快速取出。
-未完待续......

