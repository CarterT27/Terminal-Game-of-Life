from game_of_life import next_board_state

if __name__ == "__main__":
    # TEST 1: dead cells with no live neighbors
    # should stay dead.
    init_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected_next_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    actual_next_state1 = next_board_state(init_state1)

    if expected_next_state1 == actual_next_state1:
        print("PASSED 1")
    else:
        print("FAILED 1!")
        print("Expected:")
        print(expected_next_state1)
        print("Actual:")
        print(actual_next_state1)

    # TEST 2: dead cells with exactly 3 neighbors
    # should come alive.
    init_state2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    actual_next_state2 = next_board_state(init_state2)

    if expected_next_state2 == actual_next_state2:
        print("PASSED 2")
    else:
        print("FAILED 2!")
        print("Expected:")
        print(expected_next_state2)
        print("Actual:")
        print(actual_next_state2)

    # TEST 3: live cells with more than 3 live neighbors
    # should die
    init_state3 = [
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ]
    expected_next_state3 = [
        [1,0,1],
        [0,0,0],
        [1,0,1]
    ]
    actual_next_state3 = next_board_state(init_state3)

    if expected_next_state3 == actual_next_state3:
        print("PASSED 3")
    else:
        print("FAILED 3!")
        print("Expected:")
        print(expected_next_state3)
        print("Actual:")
        print(actual_next_state3)

    # TEST 4: live cells with 1 live neighbor
    # should die
    init_state4 = [
        [0,0,0],
        [0,1,0],
        [0,1,0]
    ]
    expected_next_state4 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    actual_next_state4 = next_board_state(init_state4)

    if expected_next_state4 == actual_next_state4:
        print("PASSED 4")
    else:
        print("FAILED 4!")
        print("Expected:")
        print(expected_next_state4)
        print("Actual:")
        print(actual_next_state4)