import random
import maths


def mutate(list_a):
    list_b=[]
    new_item=0
    for item in list_a:
        new_item=item*2
        new_item=new_item+ random.randint(1,3)
        new_item= maths.add(new_item, item)
    list_b.append(new_item)
    print(list_b)



mutate([1,2,3,4,5,])

