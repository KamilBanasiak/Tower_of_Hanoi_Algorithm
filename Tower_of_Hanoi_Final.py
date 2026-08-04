def hanoi_solver(n):
    if not isinstance(n, int):
        return 'n should be integer'
    if n <= 0:
        return 'n must be a positive number'
    rod1 = list(range(n, 0, -1))
    rod2 = []
    rod3 = []
    history = [f"{rod1} {rod2} {rod3}"]

    def move(disks, source, auxiliary, target):
        if disks == 1:
            target.append(source.pop())
            history.append(f"{rod1} {rod2} {rod3}")
            return
        move(disks - 1, source, target, auxiliary)
        target.append(source.pop())
        history.append(f"{rod1} {rod2} {rod3}")
        move(disks - 1, auxiliary, source, target)

    move(n, rod1, rod2, rod3)
    return "\n".join(history)