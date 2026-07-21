# works for n=1,2,3,4,5
def hanoi_solver(n: int) -> str:
    if not isinstance(n, int):
        return 'n should be integer'
    if n <= 0:
        return 'n must be a positive number'
    rod1 = [n - i for i in range(n)]
    rod2 = []
    rod3 = []
    text = f'{rod1} {rod2} {rod3}'
    if n % 2 == 0:
        while len(rod1) != 0 or len(rod2) != 0:
            if rod2 == [] and rod3 == []:
                rod2.append(rod1[-1])
                rod1.pop()
                text += f'\n{rod1} {rod2} {rod3}'
            elif rod1 == [] and rod2[-1] < rod3[-1]:
                rod3.append(rod2[-1])
                rod2.pop()
                text += f'\n{rod1} {rod2} {rod3}'  
            elif rod1 == [] and rod2[-1] > rod3[-1]:
                rod1.append(rod2[-1])
                rod2.pop()
                text += f'\n{rod1} {rod2} {rod3}'                
            elif rod2 == [] and rod1[-1] > rod3[-1]:
                rod2.append(rod1[-1])
                rod1.pop()
                text += f'\n{rod1} {rod2} {rod3}'
            elif rod2 == [] and rod1[-1] < rod3[-1]:
                rod2.append(rod1[-1])
                rod1.pop()
                text += f'\n{rod1} {rod2} {rod3}'                
            elif rod3 == [] and rod1[-1] > rod2[-1]:
                rod3.append(rod1[-1])
                rod1.pop()
                text += f'\n{rod1} {rod2} {rod3}'
            elif rod3 == [] and rod1[-1] < rod2[-1]:
                rod2.append(rod1[-1])
                rod1.pop()
                text += f'\n{rod1} {rod2} {rod3}'                
            elif rod1[-1] > rod3[-1] and rod2[-1] < rod3[-1]:
                rod3.append(rod2[-1])
                rod2.pop()
                text += f'\n{rod1} {rod2} {rod3}'   
            elif rod1[-1] > rod2[-1] and rod2[-1] > rod3[-1]:
                rod1.append(rod3[-1])
                rod3.pop()
                text += f'\n{rod1} {rod2} {rod3}' 
            elif rod2[-1] > rod3[-1] and rod1[-1] < rod3[-1]:
                rod2.append(rod3[-1])
                rod3.pop()
                text += f'\n{rod1} {rod2} {rod3}'
            elif rod2[-1] > rod1[-1] and rod1[-1] > rod3[-1]:
                rod1.append(rod3[-1])
                rod3.pop()
                text += f'\n{rod1} {rod2} {rod3}'
            elif rod2[-1] < rod3[-1] and rod2[-1] > rod1[-1]:
                rod3.append(rod2[-1])
                rod2.pop()
                text += f'\n{rod1} {rod2} {rod3}' 
            elif rod2[-1] < rod1[-1] and rod2[-1] < rod3[-1]:
                rod3.append(rod1[-1])
                rod1.pop()
                text += f'\n{rod1} {rod2} {rod3}' 
    else:
        while len(rod1) != 0 or len(rod2) != 0:
            if rod2 == [] and rod3 == []:
                rod3.append(rod1[-1])
                rod1.pop()
                text += f'\n{rod1} {rod2} {rod3}'
            elif rod1 == [] and rod2[-1] < rod3[-1]:
                rod1.append(rod2[-1])
                rod2.pop()
                text += f'\n{rod1} {rod2} {rod3}'  
            elif rod1 == [] and rod2[-1] > rod3[-1]:
                rod1.append(rod2[-1])
                rod2.pop()
                text += f'\n{rod1} {rod2} {rod3}'                
            elif rod2 == [] and rod1[-1] > rod3[-1]:
                rod2.append(rod1[-1])
                rod1.pop()
                text += f'\n{rod1} {rod2} {rod3}'
            elif rod2 == [] and rod1[-1] < rod3[-1]:
                rod3.append(rod1[-1])
                rod1.pop()
                text += f'\n{rod1} {rod2} {rod3}'                
            elif rod3 == [] and rod1[-1] > rod2[-1]:
                rod3.append(rod1[-1])
                rod1.pop()
                text += f'\n{rod1} {rod2} {rod3}'
            elif rod3 == [] and rod1[-1] < rod2[-1]:
                rod3.append(rod1[-1])
                rod1.pop()
                text += f'\n{rod1} {rod2} {rod3}'                
            elif rod1[-1] > rod3[-1] and rod2[-1] < rod3[-1] and len(rod1) > len(rod3):
                rod1.append(rod2[-1])
                rod2.pop()
                text += f'\n{rod1} {rod2} {rod3}'  
            elif rod1[-1] > rod3[-1] and rod2[-1] < rod3[-1] and len(rod1) < len(rod3):
                rod1.append(rod3[-1])
                rod3.pop()
                text += f'\n{rod1} {rod2} {rod3}'                
            elif rod1[-1] > rod2[-1] and rod2[-1] > rod3[-1]:
                rod2.append(rod3[-1])
                rod3.pop()
                text += f'\n{rod1} {rod2} {rod3}' 
            elif rod2[-1] > rod3[-1] and rod1[-1] < rod3[-1] and len(rod1) > len(rod3):
                rod2.append(rod3[-1])
                rod3.pop()
                text += f'\n{rod1} {rod2} {rod3}'
            elif rod2[-1] > rod3[-1] and rod1[-1] < rod3[-1] and len(rod1) < len(rod3):
                rod3.append(rod1[-1])
                rod1.pop()
                text += f'\n{rod1} {rod2} {rod3}'                
            elif rod2[-1] > rod1[-1] and rod1[-1] > rod3[-1] and len(rod2) > len(rod3):
                rod2.append(rod1[-1])
                rod1.pop()
                text += f'\n{rod1} {rod2} {rod3}'
            elif rod2[-1] > rod1[-1] and rod1[-1] > rod3[-1] and len(rod2) < len(rod3):
                rod2.append(rod3[-1])
                rod3.pop()
                text += f'\n{rod1} {rod2} {rod3}'                
            elif rod2[-1] < rod3[-1] and rod2[-1] > rod1[-1]:
                rod3.append(rod2[-1])
                rod2.pop()
                text += f'\n{rod1} {rod2} {rod3}' 
            elif rod2[-1] < rod1[-1] and rod1[-1] < rod3[-1] and len(rod1) > len(rod3):
                rod1.append(rod2[-1])
                rod2.pop()
                text += f'\n{rod1} {rod2} {rod3}' 
            elif rod2[-1] < rod1[-1] and rod1[-1] < rod3[-1] and len(rod1) < len(rod3):
                rod3.append(rod1[-1])
                rod1.pop()
                text += f'\n{rod1} {rod2} {rod3}'                 
    return text

print(hanoi_solver(5))