## Project Euler Solutions

Solutions to selected [Project Euler](https://projecteuler.net/archives) problems, written in Python.

## Getting Started

### Prerequisites

- **Python 3.13+** (as specified in `Pipfile`)
- **pipenv** for dependency management
- **PowerShell** (for running utility scripts)

### Installation

1. **Fork and clone the repository:**

   ```bash
   git clone https://github.com/YOUR_USERNAME/code-challenges.git
   cd code-challenges
   ```

2. **Install dependencies using pipenv:**
   ```bash
   pipenv install --dev
   ```

### Project Structure

```
code-challenges/
├── solutions/          # Python solution files (001.py, 002.py, etc.)
├── data/              # Input data files for problems that require them
├── tests/             # Test files and benchmarks
├── utils/             # Utility modules (e.g., number theory functions)
├── execute.ps1        # PowerShell script to run solutions
├── new_problem.ps1    # PowerShell script to create new solution files
├── Pipfile           # Python dependencies and scripts
└── README.md         # This file
```

### Usage

#### Running Solutions

**Option 1: Run the latest solution**

```powershell
.\execute.ps1
```

**Option 2: Run a specific solution**

```powershell
.\execute.ps1 -ScriptName "022.py"
```

**Option 3: Using pipenv directly**

```bash
pipenv run python -m solutions.022
```

**Option 4: Using pipenv script**

```bash
pipenv run solution
```

#### Creating New Solutions

To create a new solution file with the next sequential number:

```powershell
.\new_problem.ps1
```

This will create a new file (e.g., `024.py`) in the `solutions/` directory with a basic template.

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
3. Test your solution by running it with `.\execute.ps1`
4. Add any required data files to the `data/` directory
5. Update this README table with your new problem

| Problem                                                                       | Solution                     |
| ----------------------------------------------------------------------------- | ---------------------------- |
| [1. Multiples of 3 and 5](https://projecteuler.net/problem=1)                 | [001.py](./solutions/001.py) |
| [2. Even Fibonacci Numbers](https://projecteuler.net/problem=2)               | [002.py](./solutions/002.py) |
| [3. Largest Prime Factor](https://projecteuler.net/problem=3)                 | [003.py](./solutions/003.py) |
| [4. Largest Palindrome Product](https://projecteuler.net/problem=4)           | [004.py](./solutions/004.py) |
| [5. Smallest Multiple](https://projecteuler.net/problem=5)                    | [005.py](./solutions/005.py) |
| [6. Sum Square Difference](https://projecteuler.net/problem=6)                | [006.py](./solutions/006.py) |
| [7. 10001st Prime](https://projecteuler.net/problem=7)                        | [007.py](./solutions/007.py) |
| [8. Largest Product in a Series](https://projecteuler.net/problem=8)          | [008.py](./solutions/008.py) |
| [9. Special Pythagorean Triplet](https://projecteuler.net/problem=9)          | [009.py](./solutions/009.py) |
| [10. Summation of Primes](https://projecteuler.net/problem=10)                | [010.py](./solutions/010.py) |
| [11. Largest Product in a Grid](https://projecteuler.net/problem=11)          | [011.py](./solutions/011.py) |
| [12. Highly Divisible Triangular Number](https://projecteuler.net/problem=12) | [012.py](./solutions/012.py) |
| [13. Large Sum](https://projecteuler.net/problem=13)                          | [013.py](./solutions/013.py) |
| [14. Longest Collatz Sequence](https://projecteuler.net/problem=14)           | [014.py](./solutions/014.py) |
| [15. Lattice Paths](https://projecteuler.net/problem=15)                      | [015.py](./solutions/015.py) |
| [16. Power Digit Sum](https://projecteuler.net/problem=16)                    | [016.py](./solutions/016.py) |
| [17. Number Letter Counts](https://projecteuler.net/problem=17)               | [017.py](./solutions/017.py) |
| [18. Maximum Path Sum I](https://projecteuler.net/problem=18)                 | [018.py](./solutions/018.py) |
| [19. Counting Sundays](https://projecteuler.net/problem=19)                   | [019.py](./solutions/019.py) |
| [20. Factorial Digit Sum](https://projecteuler.net/problem=20)                | [020.py](./solutions/020.py) |
| [21. Amicable Numbers](https://projecteuler.net/problem=21)                   | [021.py](./solutions/021.py) |
| [22. Names Scores](https://projecteuler.net/problem=22)                       | [022.py](./solutions/022.py) |
| [23. Non-abundant Sums](https://projecteuler.net/problem=23)                  | [023.py](./solutions/023.py) |
