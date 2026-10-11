class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators=set({"+","*","-","/"})
        for ele in tokens:
            if ele in operators:
                one=stack.pop()
                two=stack.pop()
                result=None
                if ele=="+": result=one+two
                if ele=="*": result=one*two 
                if ele =="/": result=int(two/one)
                if ele=="-": result=two-one
                stack.append(result)
            else:stack.append(int(ele))
        return stack[-1]

        