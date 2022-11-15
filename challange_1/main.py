import os

from test_inputs import inputs_movement_test

os.system("clear")

outputs_received = list()
CARDINAL_POINTS = {
    "N": "Norte",
    "L": "Leste",
    "S": "Sul",
    "O": "Oeste",
}


def handle_movement_input(width_length, movement_input, cardinal_point=CARDINAL_POINTS["N"], x_coordinate=0, y_coordinate=0):
    """
    return nothing if widht_length is empty or return an string that contain cardinal_point, x_coordinate and y_coordinate

    :param width_length: string with 2 digits (Ex.: 0 0).
    :param movement_input: an sequence string that represent the movements.
    :param cardinal_point: receives an cardinal point. By default is N (North).
    :param x_coordinate: receives an x coordinate. By default is 0.
    :param y_coordinate: receives an y coordinate. By default is 0.
    """
    if width_length == "":
        return ""

    for char in movement_input:
        if char in 'F' and cardinal_point == CARDINAL_POINTS["N"] or char in 'T' and cardinal_point == CARDINAL_POINTS["S"]:
            y_coordinate += 1
        elif char in 'F' and cardinal_point == CARDINAL_POINTS["S"] and y_coordinate > 0 or char in 'T' and cardinal_point == CARDINAL_POINTS["N"] and y_coordinate > 0:
            y_coordinate -= 1
        elif char in 'F' and cardinal_point == CARDINAL_POINTS["L"] or char in 'T' and cardinal_point == CARDINAL_POINTS["O"]:
            x_coordinate += 1
        elif char in 'F' and cardinal_point == CARDINAL_POINTS["O"] and x_coordinate > 0 or char in 'T' and cardinal_point == CARDINAL_POINTS["L"] and x_coordinate > 0:
            x_coordinate -= 1
        elif char == "D":
            if cardinal_point == CARDINAL_POINTS["N"]:
                cardinal_point = CARDINAL_POINTS["L"]
            elif cardinal_point == CARDINAL_POINTS["L"]:
                cardinal_point = CARDINAL_POINTS["S"]
            elif cardinal_point == CARDINAL_POINTS["S"]:
                cardinal_point = CARDINAL_POINTS["O"]
            elif cardinal_point == CARDINAL_POINTS["O"]:
                cardinal_point = CARDINAL_POINTS["N"]
        elif char == "E":
            if cardinal_point == CARDINAL_POINTS["N"]:
                cardinal_point = CARDINAL_POINTS["O"]
            elif cardinal_point == CARDINAL_POINTS["O"]:
                cardinal_point = CARDINAL_POINTS["S"]
            elif cardinal_point == CARDINAL_POINTS["S"]:
                cardinal_point = CARDINAL_POINTS["L"]
            elif cardinal_point == CARDINAL_POINTS["L"]:
                cardinal_point = CARDINAL_POINTS["N"]

    return f"{cardinal_point[0]} {x_coordinate} {y_coordinate}"


if __name__ == "__main__":
    for i in range(len(inputs_movement_test)):
        movements = inputs_movement_test[f'input{i}']['second_line']
        wl = inputs_movement_test[f'input{i}']['first_line']
        outputs_received.append(
            handle_movement_input(wl, movement_input=movements))

    # Test the inputs that are to example
    for i in range(1, len(outputs_received)):
        print("received: ", outputs_received[i])
        print("expectd: ",
              inputs_movement_test[f'input{i}']['expected_output'])
        assert outputs_received[i] == inputs_movement_test[f'input{i}']['expected_output']
