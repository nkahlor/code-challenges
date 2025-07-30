import importlib
import pytest
import glob
import os
from typing import List
from answers import expected_answers


# TODO: go back and refactor previous problems so this can simply run on all python files in the solution directory
def get_problems_greater_than_021() -> List[str]:
    """Get all problem numbers greater than 021 from solutions directory."""
    solutions_dir = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "solutions"
    )
    solution_files = glob.glob(os.path.join(solutions_dir, "[0-9]*.py"))
    problems: List[str] = []
    for file in solution_files:
        filename = os.path.basename(file)
        if filename.replace(".py", "").isdigit():
            problem_num = int(filename.replace(".py", ""))
            if problem_num > 21:
                problems.append(f"{problem_num:03d}")
    return sorted(problems)


@pytest.mark.parametrize("problem", get_problems_greater_than_021())
def test_solution_benchmark(benchmark, problem):  # type: ignore
    module = importlib.import_module(f"solutions.{problem}")
    assert hasattr(module, "solve"), f"{problem}.py has no solve() function"

    result = benchmark(module.solve)  # type: ignore

    assert result == expected_answers.get(problem)  # type: ignore
