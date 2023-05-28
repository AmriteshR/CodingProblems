# def new_div(func):

#     def inner(a,b):
#         if a < b:
#             a,b = b,a
#         return func(a,b)
#     return inner

# @new_div
# def div(a,b):
#     return a / b

# print(div(2,4))

class It:

    def __init__(self,n) -> None:
        self.value = n

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        self.current += 1
        if self.current >= self.value:
            raise StopIteration
        return self.current
        
it = It(5)
