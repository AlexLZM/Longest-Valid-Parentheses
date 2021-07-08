def longestValidParentheses(s):
    
    stack = [-1] # dummy index -1 indicating a dummy unmatched ')'
    res = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if stack == []: # update unmatched ')' position
                stack.append(i)
            else: # we just neutrolized a ')', update max length
                res = max(res, i - stack[-1])
    return res
