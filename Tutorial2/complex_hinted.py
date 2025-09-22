
def make_complex(re: int, im: int) -> list[int]:
    """Create a complex number represented as a list.

    Args:
        re (int): Real part of the complex number.
        im (int): Imaginary part of the complex number.

    Returns:
        list: A list where the first element is the real part and the second is the imaginary part.
    """
    return [re, im]

def re(complex_num: list) -> int:
    """Get the real part of a complex number.

    Args:
        complex_num (list): A list representing a complex number.

    Returns:
        float: The real part of the complex number.
    """
    return complex_num[0]

def im(complex_num: list) -> int:
    """Get the imaginary part of a complex number.

    Args:
        complex_num (list): A list representing a complex number.

    Returns:
        float: The imaginary part of the complex number.
    """
    return complex_num[1]

def add(c1: list, c2: list) -> list:
    return make_complex(re(c1) + re(c2), im(c1) + im(c2))

def print_complex(c: list) -> None:
    print(f"{re(c)} + {im(c)}i")

if __name__ == "__main__":

    integerNum:int = 1
    boolFlag:bool = True

    floatNum:float = 3.1415

    c1 = make_complex(2, 3)
    c2 = make_complex(4, 5)
    c3 = add(c1, c2)
    print_complex(c3)  # Output: 6 + 8i