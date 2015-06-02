# Sagemath implementation of Mozes' Number Game

## Usage

### Compute Weyl Groups of finite type

````
sage: A = Mozes(CartanType(['B',4'])); A.order()
384
````

### Compute number of elements after k iterations on iterations

````
sage: A = Mozes(CartanType(['A',2,1])); A.compute_elements(5)
sage: sum(len(A.elements[i]) for i in range(6))
46
````

## References

[Mozes' Paper](http://www.sciencedirect.com/science/article/pii/009731659090024Q)

[Cartan Types in Sage](http://doc.sagemath.org/html/en/reference/combinat/sage/combinat/root_system/cartan_type.html)
