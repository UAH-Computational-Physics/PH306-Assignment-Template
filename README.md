# PH306 Assignment Template (Notebook + Script Grading)

This template is designed for GitHub Classroom using GitHub Actions grading.

- Students use `assignment.ipynb` as a guided notebook for local checks.
- Students complete required functions in `assignment.py`.
- GitHub Classroom grading is run on `assignment.py` via Actions.

## Files

- `assignment.ipynb`: guided notebook with public checks
- `assignment.py`: student implementation file (graded)
- `tests/test_public.py`: visible tests used by Classroom autograder
- `.github/workflows/autograde.yml`: Actions workflow that runs Classroom autograding
- `.github/classroom/autograding.json`: points/commands for Classroom test items

## Student workflow

1. Open `assignment.ipynb`.
2. Implement functions in `assignment.py`.
3. Re-run notebook checks.
4. Commit and push.
5. Review autograding results in GitHub.

## Devcontainer environment

The provided `.devcontainer/devcontainer.json` uses a Miniconda image and updates the base environment with `mamba` from `environment.yml` (using `conda-forge`).
