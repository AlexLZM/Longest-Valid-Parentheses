# Longest-Valid-Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 

### Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
### Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
### Example 3:

Input: s = ""
Output: 0
 

### Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.

### My strategy
Use a stack to store index information of last 'unmatched' positions
one pass solution
1. loop through s
2. push if '(', we have a unmatched '('
3. pop if ')'
4. if stack is empty, the poped is a '), push index of new ')'. What we did here is updating the last unmatched ')'position
5. otherwise, this is a neutrolization, compute current index - last stack element after pop, which is the last 'unmatched' index
note: As ')' always pop, the length of stack only go up by '('

### Time Complexity
O(n)
