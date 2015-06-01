from mozes import Mozes

def main():
    tests = [['A',3],['B',4],['F',4]]

    for test in tests:
        A = Mozes(CartanType(test))
        m = A.order()
        w = WeylGroup(test)
        n = w.order()
        
        if m == n:
            print("Order of "+str(test)+" is: "+str(n))
        else:
            print("Disagreement on "+str(test))

if __name__ == '__main__':
    main()
