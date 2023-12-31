from datetime import datetime

def howMachTime(func):
    def wrapper():
        t=datetime.now()
        func()
        delta=datetime.now()-t
        print(f'runTime: {delta}')
    return wrapper

#@howMachTime
#def func():
#  print('in func')

#func()


dictionary={}
def catch(func):
    def inner(x):
        if x in dictionary:
            return dictionary.get(x)
        dictionary.update({x:func(x)})
        return dictionary.get(x)
    return inner

@catch
def fibunacci(x):
    if x==1:
        return 1
    elif x==2:
        return 2
    else:
        return fibunacci(x-1)+fibunacci(x-2)

@howMachTime
def run():
   print(fibunacci(10))
   print(fibunacci(20))

print('\n----------run1')
run()
print('\n----------run2')
run()