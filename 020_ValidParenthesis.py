"""
여는 괄호를 스택에 append.
주어진 string을 iterate하며 닫는 괄호가 현재 스택의 마지막 원소와 매칭이 된다면 스택을 pop
마지막에 stack이 비어있다면(길이가 0이면) True 리턴 
"""
class Solution:
  def isValid(self, s: str) -> bool:
    if len(s) == 0:
      return False
    stack = []
    for i in range(len(s)):
      if s[i] in ("(", "{", "["):
        stack.append(s[i])
      elif stack[-1] == "(" and s[i] == ")" or stack[-1] == "[" and s[i] == "]" or stack[-1] == "{" and s[i] == "}":
        stack.pop()
      else:
        return False
    if len(stack) == 0: return True