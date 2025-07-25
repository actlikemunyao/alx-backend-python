
---

## ✅ Tasks Implemented

### 0. Parameterize a unit test
- Added tests for `access_nested_map` with varying inputs using `parameterized`.

### 1. Parameterize a unit test (continued)
- Added test cases to check for `KeyError` exceptions in `access_nested_map`.

### 2. Mock HTTP calls
- Patched `get_json` to test behavior without making actual HTTP requests.

### 3. Parameterize and mock
- Combined parameterization with mocking `requests.get`.

### 4. Integration test: fixtures
- Setup a `fixtures.py` file containing fake payloads for GitHub org repos.

### 5. Integration test: setup
- Wrote setup logic for integration testing the GitHubOrgClient class.

### 6. Integration test
- Completed integration tests using actual calls to GitHub API (mocked with fixtures).

### 7. Mocking a property
- Mocked the `org` property of `GitHubOrgClient`.

### 8. Integration test: GithubOrgClient.public_repos
- Tested `public_repos()` with real-like payload and filters using `mock`.

---

## 💡 How to Run Tests

You can run all tests with:

```bash
python3 -m unittest discover
  
