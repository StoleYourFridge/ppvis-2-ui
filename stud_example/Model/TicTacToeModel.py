class TicTackToeModel:
    coordinate = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # X
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Y
        (0, 4, 8), (2, 4, 6),  # D
    )

    def __init__(self):
        self.buttons = None
        self.switch = True

    def tic_tac_toe(self, arg):
        arg.disabled = True
        arg.text = 'X' if self.switch else 'O'
        self.switch = not self.switch

        vector = lambda item: [self.buttons[x].text for x in item]

        color = [0, 1, 0, 1]
        for item in self.coordinate:
            if vector(item).count('X') == 3 or vector(item).count('O') == 3:
                win = True
                for i in item:
                    self.buttons[i].color = color
                for button in self.buttons:
                    button.disabled = True
                break

    def restart(self):
        self.switch = True

        for button in self.buttons:
            button.color = [0, 0, 0, 1]
            button.text = ""
            button.disabled = False
