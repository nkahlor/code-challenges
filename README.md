## Project Euler Solutions

Solutions to selected [Project Euler](https://projecteuler.net/archives) problems, written in Python.
| Problem | Solution |
| ----------------------------------------------------------------------------- | ---------------------------- |
| [1. Multiples of 3 and 5](https://projecteuler.net/problem=1) | [001.py](./solutions/001.py) |
| [2. Even Fibonacci Numbers](https://projecteuler.net/problem=2) | [002.py](./solutions/002.py) |
| [3. Largest Prime Factor](https://projecteuler.net/problem=3) | [003.py](./solutions/003.py) |
| [4. Largest Palindrome Product](https://projecteuler.net/problem=4) | [004.py](./solutions/004.py) |
| [5. Smallest Multiple](https://projecteuler.net/problem=5) | [005.py](./solutions/005.py) |
| [6. Sum Square Difference](https://projecteuler.net/problem=6) | [006.py](./solutions/006.py) |
| [7. 10001st Prime](https://projecteuler.net/problem=7) | [007.py](./solutions/007.py) |
| [8. Largest Product in a Series](https://projecteuler.net/problem=8) | [008.py](./solutions/008.py) |
| [9. Special Pythagorean Triplet](https://projecteuler.net/problem=9) | [009.py](./solutions/009.py) |
| [10. Summation of Primes](https://projecteuler.net/problem=10) | [010.py](./solutions/010.py) |
| [11. Largest Product in a Grid](https://projecteuler.net/problem=11) | [011.py](./solutions/011.py) |
| [12. Highly Divisible Triangular Number](https://projecteuler.net/problem=12) | [012.py](./solutions/012.py) |
| [13. Large Sum](https://projecteuler.net/problem=13) | [013.py](./solutions/013.py) |
| [14. Longest Collatz Sequence](https://projecteuler.net/problem=14) | [014.py](./solutions/014.py) |
| [15. Lattice Paths](https://projecteuler.net/problem=15) | [015.py](./solutions/015.py) |
| [16. Power Digit Sum](https://projecteuler.net/problem=16) | [016.py](./solutions/016.py) |
| [17. Number Letter Counts](https://projecteuler.net/problem=17) | [017.py](./solutions/017.py) |
| [18. Maximum Path Sum I](https://projecteuler.net/problem=18) | [018.py](./solutions/018.py) |
| [19. Counting Sundays](https://projecteuler.net/problem=19) | [019.py](./solutions/019.py) |
| [20. Factorial Digit Sum](https://projecteuler.net/problem=20) | [020.py](./solutions/020.py) |
| [21. Amicable Numbers](https://projecteuler.net/problem=21) | [021.py](./solutions/021.py) |
| [22. Names Scores](https://projecteuler.net/problem=22) | [022.py](./solutions/022.py) |
| [23. Non-abundant Sums](https://projecteuler.net/problem=23) | [023.py](./solutions/023.py) |
| [24. Lexicographic Permutations](https://projecteuler.net/problem=24) | [024.py](./solutions/024.py) |
| [25. 1000-digit Fibonacci Number](https://projecteuler.net/problem=25) | [025.py](./solutions/025.py) |
| [26. Reciprocal Cycles](https://projecteuler.net/problem=26) | [026.py](./solutions/026.py) |
| [27. Quadratic Primes](https://projecteuler.net/problem=27) | [027.py](./solutions/027.py) |
| [28. Number Spiral Diagonals](https://projecteuler.net/problem=28) | [028.py](./solutions/028.py) |
| [29. Distinct Powers](https://projecteuler.net/problem=29) | [029.py](./solutions/029.py) |
| [30. Digit Fifth Powers](https://projecteuler.net/problem=30) | [030.py](./solutions/030.py) |

## Getting Started

### Prerequisites

- **pyenv** not strictly needed, but highly recommended (if not using, check Pipfile for the python version you need)
- **pipenv** for dependency management
- **PowerShell** (for running utility scripts)

### Installation

**Install dependencies using pipenv:**

```bash
pipenv install --dev
```

### Usage

#### Running Solutions

**Option 1: Run the latest solution**

```powershell
pipenv run solution
```

**Option 2: Run a specific solution**

```powershell
pipenv run solution -- "022.py"
```

**Option 3: Using pipenv directly**

```bash
pipenv run python -m solutions.022
```

#### Creating New Solutions

To create a new solution file with the next sequential number in the solutions folder:

```powershell
.\new_problem.ps1
```

#### Development Commands

**Format code:**

```bash
pipenv run format
```

**Lint code:**

```bash
pipenv run lint
```

**Run tests:**

```bash
pipenv run test
```

### Adding Your Own Solutions

1. Use `.\new_problem.ps1` to create a new solution file
2. Implement your solution in the `solve()` function (putting it in the solve function makes benchmarking convenient)
3. Test your solution by running it with `pipenv run solution`
4. Add any required data files to the `data/` directory
5. Update this README table with your new problem
