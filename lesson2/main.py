
def find_prims(number):
    lista=[]
    for num in range(number):

        if num > 1:

            for i in range(2, num):

                if (num % i) == 0:
                    break

            else:

                lista.append(num)
    return lista

def sort_list(lista):
     lista.sort()
     return lista

def calculate_expretion(exp):
    return eval(exp)