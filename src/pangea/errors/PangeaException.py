class PangeaException():
    def __init__(self, error_code, message=None, description=None, data=None):
        super().__init__(message)
        self.error_code = error_code
        self.message = message
        self.description = description
        self.data = data

  