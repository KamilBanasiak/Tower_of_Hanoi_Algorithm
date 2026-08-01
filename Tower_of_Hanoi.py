# works for n=1,2,3,4
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
        rod2.append(rod1[-1])
        rod1.pop()
    else:
        rod3.append(rod1[-1])
        rod1.pop()
    text += f'\n{rod1} {rod2} {rod3}'        
    if n == 1:
        return text
    while not n in rod3:
        if rod2 == [] and rod1[-1] > rod3[-1]:
            rod2.append(rod1[-1])
            rod1.pop()
        elif rod2 == [] and rod1[-1] < rod3[-1]:
            rod3.append(rod1[-1])
            rod1.pop()
        elif rod3 == [] and rod1[-1] > rod2[-1]:
            rod3.append(rod1[-1])
            rod1.pop()
        elif rod3 == [] and rod1[-1] < rod2[-1]: 
            rod2.append(rod1[-1])
            rod1.pop()
        elif rod3[-1] > rod2[-1] and len(rod2) == 1:
            rod3.append(rod2[-1])
            rod2.pop()
        elif rod3[-1] > rod2[-1]:
            rod1.append(rod2[-1])
            rod2.pop()
        elif rod3[-1] < rod2[-1] and len(rod3) == 1:
            rod2.append(rod3[-1])
            rod3.pop()
        else:
            rod1.append(rod3[-1])
            rod3.pop()
        text += f'\n{rod1} {rod2} {rod3}'        
    part_text = hanoi_solver(n-1)
    m = 8 + n + 2 * (n - 2)
    while m != len(part_text) - 1:
        o = part_text.find('[', m)
        a = part_text.find(']', m + 1)
        b = part_text.find(']', a + 1) 
        m = part_text.find(']', b + 1)
        if m - (b + 2) != 1:
            text += f'\n{part_text[a+2: b+1]} ' + part_text[o: a+2] + f'[{n}, ' + part_text[b+3: m+1] 
        else:
            text += f'\n{part_text[a+2: b+1]} ' + part_text[o: a+1] + part_text[b+1: m] + f'{n}]'
    return text