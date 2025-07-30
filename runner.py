#!/usr/bin/env python3

import argparse
import importlib
import re
import sys
import time
from pathlib import Path
from typing import Optional


def find_solution_files(solutions_dir: Path) -> list[Path]:
    if not solutions_dir.exists():
        print(f"Solutions folder not found: {solutions_dir}")
        sys.exit(1)

    py_files = list(solutions_dir.glob("*.py"))
    solution_files = [
        f
        for f in py_files
        if f.name != "__init__.py" and re.match(r"^\d+\.py$", f.name)
    ]

    if not solution_files:
        print(f"No solution Python scripts found in {solutions_dir}")
        sys.exit(1)

    return solution_files


def get_numeric_value(filename: str) -> int:
    match = re.search(r"(\d+)", filename)
    return int(match.group(1)) if match else 0


def find_target_script(
    solution_files: list[Path], script_name: Optional[str] = None
) -> Path:
    if script_name:
        # Look for exact match or partial match
        target_script = None
        for file in solution_files:
            if file.name == script_name:
                target_script = file
                break
            elif file.stem == script_name:
                target_script = file
                break
            elif script_name.isdigit() and file.stem == script_name.zfill(3):
                target_script = file
                break

        if not target_script:
            print(f"Specified script not found: {script_name}")
            sys.exit(1)
        return target_script
    else:
        return max(solution_files, key=lambda f: get_numeric_value(f.name))


def format_execution_time(seconds: float) -> str:
    if seconds >= 1:
        return f"{seconds:.3f} seconds"
    elif seconds >= 0.001:
        return f"{seconds * 1000:.2f} ms"
    else:
        return f"{seconds * 1000000:.0f} μs"


def run_solution(script_path: Path) -> None:
    print(f"\033[96mRunning script: \033[93m{script_path.name}\033[0m")
    print("\033[90m" + "=" * 50 + "\033[0m")

    project_root = script_path.parent.parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    module_name = f"solutions.{script_path.stem}"
    try:
        module = importlib.import_module(module_name)

        if not hasattr(module, "solve"):
            print(f"Error: {script_path.name} does not have a 'solve' function")
            sys.exit(1)

        solve_function = module.solve

        start_time = time.perf_counter()
        result = solve_function()
        end_time = time.perf_counter()

        execution_time = end_time - start_time

        print(result)

        print("\033[90m" + "=" * 50 + "\033[0m")
        print(f"\033[92mExecution time: {format_execution_time(execution_time)}\033[0m")

    except ImportError as e:
        print(f"Error importing {module_name}: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error executing solve function: {e}")
        sys.exit(1)


def main():
    """Main function to parse arguments and run the solution."""
    parser = argparse.ArgumentParser(
        description="Execute solution files from the solutions directory",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python runner.py           # Run the highest numbered solution
  python runner.py 024       # Run solution 024.py
  python runner.py 024.py    # Run solution 024.py
  python runner.py 24        # Run solution 024.py (with zero-padding)
        """,
    )

    parser.add_argument(
        "script_name",
        nargs="?",
        help="Name or number of the script to run (optional, defaults to highest numbered solution)",
    )

    args = parser.parse_args()

    script_dir = Path(__file__).parent
    solutions_dir = script_dir / "solutions"

    solution_files = find_solution_files(solutions_dir)

    target_script = find_target_script(solution_files, args.script_name)

    run_solution(target_script)


if __name__ == "__main__":
    main()
