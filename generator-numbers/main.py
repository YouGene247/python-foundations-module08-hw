import re
from decimal import Decimal
from typing import Callable, Iterable

def generator_numbers(text: str) -> Iterable[Decimal]:
    
    pattern = r'\b\d+\.\d+\b'

    for num in re.finditer(pattern, text):
        print(num)
        yield Decimal(num.group())


def sum_profit(text: str, func: Callable[[str], Iterable[Decimal]]) -> Decimal:

    numbers = func(text)

    total = Decimal('0')

    for number in numbers:
        total += number
    return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total = sum_profit(text, generator_numbers)

print(total)
