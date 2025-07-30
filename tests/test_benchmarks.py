import importlib
import pytest
from answers import expected_answers


@pytest.mark.parametrize("problem", ["021", "022", "023", "024"])
def test_solution_benchmark(benchmark, problem):  # type: ignore
    module = importlib.import_module(f"solutions.{problem}")
    assert hasattr(module, "solve"), f"{problem}.py has no solve() function"

    result = benchmark(module.solve)  # type: ignore

    assert result == expected_answers.get(problem)  # type: ignore
