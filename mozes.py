from collections import deque
class Mozes:

    def __init__(self,cartantype):
        self.cartantype = cartantype
        self.n = len(self.cartantype.index_set())
        self.state = [1] * len(self.cartantype.index_set())
        self.identity = [1] * self.n

        # queue is the set of elements that need to be fired upon
        self.queue=deque([])
        self.queue.append([self.identity,0])

        # elements[i] is list of length i words
        # run compute_elements(L) to compute up to elements[L]
        # compute elements[0],elements[1]
        self.elements=[[self.identity],[]]
        element = self.queue.pop()
        for k in range(self.n):
            new = self.fire(element[0],k)
            self.elements[1].append(new)
            self.queue.appendleft([new,1]) 

    def fire(self,state,k):
        # tranpose to agree with Humphreys and the sagemath dynkin diagrams
        v = self.cartantype.cartan_matrix().transpose()[k]
        newstate = list(state)
        for i in range(self.n):
            if i == k:
                pass
            else:
                newstate[i] = state[i] + abs(v[i])*state[k]

        newstate[k] = -state[k]
        return newstate

    def compute_elements(self,L):
        while len(self.queue) > 0 and (self.queue[-1][1] <= L or L==-1):
            element = self.queue.pop()
            l = element[1]

            if l+2 > len(self.elements):
                self.elements.append([])

            for k in range(self.n):
                new = self.fire(element[0],k)
                if new not in self.elements[l-1] and new not in self.elements[l+1]:
                    # If w is length l then sw is length l\pm 1
                    self.elements[l+1].append(new)
                    self.queue.appendleft([new,l+1])
                else:
                    pass #repeated element

    def order(self):
        self.compute_elements(-1)
        return sum([len(x) for x in self.elements])
