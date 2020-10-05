class EnclosureException(Exception):
    """
    Exception raised for errors when enclosure does not match between begin and end.
    For ex: "(something]" "(" does not mach "]"
    """

    def __init__(self, message, match):
        self.match = match
        self.message = message
        super().__init__(self.message, match)
