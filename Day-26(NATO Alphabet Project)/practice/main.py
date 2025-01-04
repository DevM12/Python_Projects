
def add_1(num):
    a=num+1
    a*=2
    return a

numbers=[1,2,3,4,5]
new_list=[add_1(n) for n in range(1,5)]
print(new_list)