def take_tour(current_square, seen_set):
    if len(seen_set) == (ROW_COUNT * COL_COUNT):
        print("We have a solution!")
        print(seen_set)

        raise SystemExit
    else:
        next_moves = get_smart_moves(current_square, seen_set)

        for move in next_moves:
            seen_set.append(move)
            take_tour(move, seen_set)

        seen_set.remove(current_square)


def get_possible_moves(current_square, seen_set):
    possible_moves = []

    for move in all_moves:
        new_square = tuple(map(lambda x, y: x + y, current_square, move))

        if is_valid_square(new_square) and new_square not in seen_set:
            possible_moves.append(new_square)

    return possible_moves


def get_smart_moves(current_square, seen_set):
    possible_moves = []

    for move in all_moves:
        new_square = tuple(map(lambda x, y: x + y, current_square, move))

        if is_valid_square(new_square) and new_square not in seen_set:
            possible_moves.append((new_square,
                                   get_second_order_move_count(current_square, new_square, seen_set)))

    possible_moves.sort(key=lambda tup: tup[1])
    possible_moves = [move[0] for move in possible_moves]

    return possible_moves


def get_second_order_move_count(current_square, next_square, seen_set):
    total_moves = 0

    for move in all_moves:
        new_square = tuple(map(lambda x, y: x + y, next_square, move))

        if is_valid_square(new_square) and new_square not in seen_set and new_square != current_square:
            total_moves = total_moves + 1

    return total_moves


def is_valid_square(square):
    if square[0] < 0 \
            or square[1] < 0 \
            or square[0] >= ROW_COUNT \
            or square[1] >= COL_COUNT:
        return False

    return True


if __name__ == '__main__':
    ROW_COUNT = 5
    COL_COUNT = 5
    all_moves = [(2, 1), (1, 2), (2, -1), (1, -2), (-2, 1), (-1, 2), (-2, -1), (-1, -2)]

    take_tour((0, 0), [(0, 0)])
