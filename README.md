# primecheck.py
A CLI tool to check if any ints in a list are prime and print their factors, or to print all primes up to *n*.

![out](https://user-images.githubusercontent.com/23170004/214976863-0e72e45f-12a9-41a6-8f00-57301cc13152.gif)

## Usage
Clone the repo, cd into the directory, and install with `pip install .`
The cli command for the program is `pprime` (mnemonic for 'py-prime').

### Prime-Check
Pass any number of ints as positional arguments and the program will print them back in color. All primes are green, all composites are red.

<img width="259" alt="Screen Shot 2023-01-26 at 18 04 09" src="https://user-images.githubusercontent.com/23170004/214977636-510cdb9c-4a57-428b-81a4-7c15afac2e86.png">

By default, the program sorts the list before it prints it back, but this can be overridden with the `-U` flag.

<img width="302" alt="Screen Shot 2023-01-26 at 18 00 52" src="https://user-images.githubusercontent.com/23170004/214977247-39d37008-e985-422c-82f7-484ea1eb1b92.png">

### Prime-List
Pass the `-N` flag followed by an int to print all primes up to that number.

<img width="510" alt="list" src="https://user-images.githubusercontent.com/23170004/214741795-1b2079ff-6091-45d1-8dd7-1fdfcf5ca501.png">

## Testing Implementation
The program's `Test` class is intended to be used for testing with `pytest`. The two functions are checked against a [list of the first ten-thousand primes](https://primes.utm.edu/lists/small/10000.txt) as well as each other. To run the tests, clone the repo, cd into the directory, and run `pytest` in the terminal.
