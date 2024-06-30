# import libs
from random import choice
from colorama import Fore
import config

# print intro
symbols_pull_to_choise = ''.join([
    config.numbers if config.include_numbers else '',
    config.letters if config.include_letters else '',
    config.capital_letters if config.include_capital_letters else '',
    config.special_chars if config.include_special_chars else '',
    config.io_mode if config.include_io_mode else ''
])

symbols_pull = ''.join([choice(symbols_pull_to_choise) for symbol in range(10000)])
symbol_color = ''.join([choice(config.colors) for symbol_color in range(len(symbols_pull))])

for symbol in symbols_pull:
    print(choice(config.colors) + symbol, end='')

print()
