# primecheck.py
A CLI tool to check if any ints in a list are prime and print their factors, or to print all primes up to *n*.

![out](https://user-images.githubusercontent.com/23170004/215036461-05f88176-7c6b-4471-b817-847657268c11.gif)

## Usage
Clone the repo, cd into the directory, and install with `pip install .`
The cli command for the program is `pprime` (mnemonic for 'py-prime').

### Prime-Check
Pass any number of ints as positional arguments and the program will print them back in color. All primes are green, all composites are red.

<img width="259" alt="Screen Shot 2023-01-26 at 18 04 09" src="https://user-images.githubusercontent.com/23170004/214977636-510cdb9c-4a57-428b-81a4-7c15afac2e86.png">

#### Unsorted
By default, the program sorts the list before it prints it back, but this can be overridden with the `-U` flag.

<img width="302" alt="Screen Shot 2023-01-26 at 18 00 52" src="https://user-images.githubusercontent.com/23170004/214977247-39d37008-e985-422c-82f7-484ea1eb1b92.png">

#### Grouped Factors

By default, the program will print out the sorted set of unique factors of any composite integer. When the `-G` flag is set, the factors will be grouped into their factor pairs.

<img width="266" alt="Screen Shot 2023-01-27 at 02 04 42" src="https://user-images.githubusercontent.com/23170004/215037469-8a58cc33-a0af-4ffa-87f8-f28dc5441fc1.png">

#### Prime Factors

Setting the `-P` flag prints the prime factors of the integer rather than the composite factors.

<img width="222" alt="Screen Shot 2023-01-27 at 02 08 37" src="https://user-images.githubusercontent.com/23170004/215038155-2ed7ba17-ce63-4f7f-acb5-2826c1301034.png">

### Prime-List
Pass the `-N` flag followed by an int to print all primes up to that number.

<img width="510" alt="list" src="https://user-images.githubusercontent.com/23170004/214741795-1b2079ff-6091-45d1-8dd7-1fdfcf5ca501.png">

### Radical Simplification

Simplify any nth-root radical with `-rs {nth} {base}` by factoring out all perfect squares. The radical terms are formatted `root{nth}{base}`. For example, `3(root(3)(6))` is equivalent to `3 * ∛6`

<img width="282" alt="Screen Shot 2023-01-29 at 22 22 56" src="https://user-images.githubusercontent.com/23170004/215387037-bdd11fe5-9c82-47bf-a79d-5afad5e1f9e4.png">

## Testing Implementation
The program's `Test` class is intended to be used for testing with `pytest`. The two functions are checked against a [list of the first ten-thousand primes](https://primes.utm.edu/lists/small/10000.txt) as well as each other. To run the tests, clone the repo, cd into the directory, and run `pytest` in the terminal.
