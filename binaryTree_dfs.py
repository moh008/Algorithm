#binary Tree DFS 
def preorderTraversal(root):
  if root.left:                         #왼쪽 자식노드가 존재할때
    preorderTraversal(root.left)
  if root.right:                        #오른쪽 자식노드가 존재할때
    preorderTraversal(root.right)

#알고리즘은 같음
def preorderTraversalfor(root):         #위처럼 왼쪽 오른쪽 지정하지않고, for loop으로 돌리기
  for child in [root.left, root.right]:
    if child:
      preorderTraversalfor(child)