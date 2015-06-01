class mozes:

    def __init__(self,cartantype):
        self.cartantype = cartantype
        self.n = len(self.cartantype.index_set())
        self.state = [1] * len(self.cartantype.index_set())
        self.identity = [1] * self.n

        # R[i] is list of length i words
        self.R=[[self.identity],[]]
        # stack is the set of elements that need fired upon
        self.stack=[[self.identity,0]]

    def fire(self,state,k):
        # tranpose to agree with Humphreys
        v = self.cartantype.cartan_matrix().transpose()[k]
        newstate = list(state)
        for i in range(self.n):
            if i == k:
                pass
            else:
                newstate[i] = state[i] + abs(v[i])*state[k]

        newstate[k] = -state[k]
        return newstate

    def computeR(self,L):
        while len(self.stack) > 0 and (self.stack[-1][1] <= L or L==-1):
            element = self.stack.pop()
            l = element[1]

            if l+2 > len(self.R):
                self.R.append([])

            for k in range(self.n):
                new = self.fire(element[0],k)
                if element[1] == 0:
                    self.R[1].append(new)
                    self.stack.insert(0,[new,1])
                elif new not in self.R[l-1] and new not in self.R[l+1]:
                    self.R[l+1].append(new)
                    self.stack.insert(0,[new,l+1])
                else:
                    pass #repeated element

    def order(self):
        self.computeR(-1)
        S=[item for sublist in self.R for item in sublist]
        return len(S)
