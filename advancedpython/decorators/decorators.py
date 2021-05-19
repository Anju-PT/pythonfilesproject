#decorator function
#adding extra feature with out changing already existing function definition
#increase code reliability

def avoid_zero(func):
    def wrapper(num1,num2):
        if(num1==0) or (num2==0):
            raise Exception("zero division not allowed")
        else:
            return func(num1,num2)
    return wrapper


def shuffle_values(func):
    def wrapper(num1,num2):
        if(num1<num2):
            (num1,num2)=(num2,num1)
        return func(num1,num2)
    return wrapper

@avoid_zero
@shuffle_values
def div(num1,num2):
    return num1/num2

print(div(4,10))