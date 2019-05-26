class Letter:
    def __init__(self, pattern=[".",".","_"]):
        self.pattern = pattern

    def __str__(self):
        message = []
        for letter in self.pattern:
            if letter == ".":
                message.append("dot")
            if letter == "_":
                message.append("dash")
        return "-".join(message)
