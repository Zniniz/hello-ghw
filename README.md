```
name: Test                     # The display name for this workflow in GitHub Actions UI.

on:                            # Triggers that start this workflow.
  push:                        # Run the workflow on pushes…
    branches:                  # …but only when pushing to these branches:
      - main                   # …the 'main' branch.

jobs:                          # A workflow is made of one or more jobs.
  test:                        # Job ID (internal key). You can name it anything.
    name: Run Tests with Python 3.13   # Human-friendly job name shown in the UI.
    runs-on: ubuntu-latest     # Runner image to execute on (GitHub-hosted Ubuntu).

    steps:                     # Ordered list of steps that run inside the job.
      - uses: actions/checkout@v4       # Step 1: check out your repository code.

      - uses: actions/setup-python@v5   # Step 2: install/configure a Python version.
        with:
          python-version: '3.13'        # Request Python 3.13.x (string is fine).
                                        # Note: many libs don’t have wheels for 3.13 yet.

      - run: python --version           # Step 3: print the actual Python version resolved.

      - run: python -m pip install -r requirements_dev.txt
                                        # Step 4: install dependencies from this file.
                                        # If it contains system-bound/native deps, this can fail.

      - run: pytest                     # Step 5: run your tests. Discovers tests automatically.
```
