## Learning Progress: GitHub Actions & CI/CD

### Phase 1: GitHub Actions Fundamentals and Python CI

**Objective:** Understand how GitHub Actions works, how workflows are defined using YAML, and how automated tests can validate code changes.

#### 1. First GitHub Actions Workflow

Created `.github/workflows/first-workflow.yml` to explore the fundamentals of GitHub Actions.

The workflow used an Ubuntu runner and executed basic Linux commands to understand how GitHub Actions runs jobs and steps.

**What I learned:**
- Workflow structure: `name`, `on`, `jobs`, `runs-on`, and `steps`.
- The difference between `uses` and `run`.
- How `actions/checkout@v4` makes repository files available to the runner.
- How to execute Linux commands such as `pwd`, `ls`, and `ls -la`.
- How GitHub Actions executes workflow steps and displays their output in logs.
- How to configure workflow triggers, beginning with `push`.

This first workflow provided a foundation for understanding the YAML structure and execution process before introducing application testing.

#### 2. Python Continuous Integration (CI)

Created `.github/workflows/python-ci.yml` to build a basic automated testing pipeline for a Python application.

**Project files:**
- `app.py` — contains the application logic.
- `test_app.py` — contains the automated test.
- `requirements.txt` — declares the Python testing dependency.
- `.github/workflows/python-ci.yml` — defines the CI pipeline.

**Application logic:**

```python
def add_numbers(a, b):
    return a + b
```

**Automated test:**

```python
from app import add_numbers

def test_add_numbers():
    assert add_numbers(10, 7) == 17
```

**CI pipeline stages:**

1. Check out the repository.
2. Set up Python 3.12.
3. Install dependencies from `requirements.txt`.
4. Execute automated tests using `python -m pytest -v`.

The workflow uses `actions/checkout@v4` and `actions/setup-python@v5`.

#### 3. Dependency Management

Started with an unpinned `pytest` dependency and later pinned its version in `requirements.txt`:

```text
pytest==9.1.1
```

**What I learned:**
- Why projects declare their dependencies.
- How `python -m pip install -r requirements.txt` installs declared dependencies.
- How version pinning helps make dependency installation more predictable.
- Why pinning a package version does not automatically pin the Python interpreter version.

#### 4. Workflow Triggers: Push and Pull Requests

Extended the Python CI workflow to run on both `push` and `pull_request` events.

```yaml
on:
  push:
  pull_request:
```

Practised the GitHub branching and pull-request workflow:

1. Create a feature branch from `main`.
2. Make a change on the feature branch.
3. Open a pull request targeting `main`.
4. Observe GitHub Actions checks.
5. Merge the change after the checks pass.

This introduced the role of CI in validating proposed changes before they are merged into the default branch.

#### 5. Deliberate Test Failures and Troubleshooting

Introduced deliberate failures to understand how automated tests detect problems.

**Experiments performed:**
- Changed the application logic from addition to subtraction.
- Observed the test fail because the actual result did not match the expected result.
- Changed the expected test value to an incorrect value and observed another failure.
- Restored the correct application logic and test expectation.
- Confirmed that the tests passed again and merged the corrected change.

**Key lessons:**
- Pytest reports assertion failures when actual results differ from expected results.
- Failed test commands return a non-zero exit code, causing the CI job to fail.
- Workflow logs help identify failing steps and diagnose problems.
- A passing test does not guarantee correct application behaviour if the tests themselves are incorrect.
- Automated tests complement code review; they do not replace it.
- A passing check does not automatically prevent or permit every merge unless the repository's rules enforce the required checks.

#### 6. GitHub Actions Concepts Covered

- Workflow files and YAML indentation.
- Workflow triggers: `push` and `pull_request`.
- Jobs, runners, and steps.
- Actions versus shell commands.
- Repository checkout.
- Python environment setup.
- Dependency installation and version pinning.
- Automated testing with pytest.
- Reading workflow logs and troubleshooting failures.
- Feature branches, pull requests, and merging into `main`.
- Understanding successful and failed CI runs.

### Current Status

**Completed:** Basic GitHub Actions workflow and Python CI pipeline, including pull-request validation, dependency management, failure diagnosis, and recovery.

**Not yet implemented:** Linting, caching, artifacts, environment variables and secrets, advanced workflow conditions, Docker image builds, continuous delivery, and continuous deployment.

### Next Steps

1. Add linting to the Python CI pipeline.
2. Continue learning essential GitHub Actions features.
3. Resume Linux administration, beginning with process management and service management.
4. Learn Docker fundamentals and containerise the Python application.
5. Extend the project into a build-and-deploy pipeline.
6. Apply the same CI/CD principles to JavaScript/Node.js, frontend applications, and Java.
