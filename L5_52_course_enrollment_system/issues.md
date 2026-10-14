# Static Code Analysis – Issues Report

| Issue                            | Type              | Line(s) | Description                                                             | Fix Approach                                                             |
| -------------------------------- | ----------------- | ------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Unsafe `eval()` usage            | Security (Medium) | 47      | `eval(discount_expr)` may execute arbitrary code.                       | Replace with safe, validated discount calculation logic.                 |
| Weak MD5 hashing                 | Security (High)   | 52      | MD5 is unsuitable for security-sensitive hashing.                       | Use SHA-256 if a cryptographic hash is required.                         |
| Shell command execution          | Security (High)   | 63      | `os.system()` invokes a shell to display the export message.            | Replace with Python's `print()` function.                                |
| Hardcoded authentication token   | Security (Low)    | 75      | The registrar token is hardcoded in the source file.                    | Load the token from an environment variable.                             |
| Mutable default argument         | Bug               | 15      | `logs=[]` can share a list across function calls.                       | Use `None` as the default and initialize a new list inside the function. |
| Broad exception handling         | Code Quality      | 31      | A bare `except` with `pass` silently hides errors.                      | Catch and handle the specific expected exception.                        |
| Insecure OTP generation          | Security (Low)    | 56      | `random.randint()` is unsuitable for security-sensitive OTP generation. | Use Python's `secrets` module.                                           |
| Unused import                    | Code Quality      | 4       | The `math` module is imported but unused.                               | Remove the unused import.                                                |
| Incorrect comparison with `None` | Code Quality      | 37      | Uses `== None` instead of an identity check.                            | Change to `is None`.                                                     |
| Missing final newline            | Style             | 87      | The file does not end with a newline.                                   | Add a newline at the end of the file.                                    |
