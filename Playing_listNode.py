class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
		
L = ListNode(1)
L2 = L.next = ListNode(3)
L3 = L2.next = ListNode(4)

sum = 0;
while L:
	sum += L.val
	print(L.val)
	L = L.next
print("sum",sum)
