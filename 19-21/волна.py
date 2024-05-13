def game(heap,heap2, moves, to):
    if heap + heap2 >= 123:
        return moves % 2 == to % 2
    if moves == to:
        return False
    h = [game(heap + 1,heap2, moves + 1, to),
         game(heap * 2,heap2, moves + 1, to),
         game(heap,heap2 + 1, moves + 1, to),
         game(heap,heap2 * 2, moves + 1, to),]
    return any(h)

print(f'19: {min(s for s in range(1, 109) if not game(13,s, 0, 1) and game(13,s, 0, 2))}')



def game2(heap,heap2, moves, to):
    if heap + heap2 >= 123:
        return moves % 2 == to % 2
    if moves == to:
        return False
    h = [game2(heap + 1,heap2, moves + 1, to),
         game2(heap * 2,heap2, moves + 1, to),
         game2(heap,heap2 + 1, moves + 1, to),
         game2(heap,heap2 * 2, moves + 1, to),]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)


print(f'20: {[s for s in range(1, 109) if not game2(13,s, 0, 1) and game2(13,s, 0, 3)]}')
print(f'21: {min(s for s in range(1, 109) if not game2(13,s, 0, 2) and game2(13,s, 0, 4))}')
