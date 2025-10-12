class Calculator:
    # Class attribute shared across all instances
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: performs addition without needing class or instance data."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: accesses class-level data via 'cls'."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
