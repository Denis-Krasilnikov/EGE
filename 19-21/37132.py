def game(heap, moves, to):
    """
    :param heap: Размер кучи
    :param moves: Номер текущего хода
    :param to: Ход, который проверяется
    :return: Возможная ли победа на ходу to
    """
    if heap >= 47:
        return moves % 2 == to % 2
    if moves == to:
        return False
    h = [game(heap + 1, moves + 1, to),
         game(heap * 2, moves + 1, to),
         game(heap + 4, moves + 1, to)]
    # any(массив_значений) - возвращает True, если хотя бы одно значение в массиве истинно
    return any(h)

print(f'19: {min(s for s in range(1, 47) if not game(s, 0, 1) and game(s, 0, 2))}')




def game2(heap, moves, to):
    if heap >= 47:
        return moves % 2 == to % 2
    if moves == to:
        return False
    h = [game2(heap + 1, moves + 1, to),
         game2(heap * 2, moves + 1, to),
         game2(heap + 4, moves + 1, to)]
    # all(массив_значений) - возвращает True, если все значения в массиве истинны
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)


print(f'20: {[s for s in range(1, 47) if not game2(s, 0, 1) and game2(s, 0, 3)]}')
print(f'21: {min(s for s in range(1, 47) if not game2(s, 0, 2) and game2(s, 0, 4))}')

