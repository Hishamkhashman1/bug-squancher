# static pattern definitions only

# add first batch of patterns
PYTHON_PATTERN_SEEDS = [
    {
        "name": "modulenotfounderror",
        "keywords": ["modulenotfounderror", "no module named"],
        "cause": "A required Python package or local module could not be found.",
        "possible_fix": "Install the missing package or check your import path/module name.",
        "recommended_command": "pip install <package_name>",
        "context": "Run in your active virtual environment or fix the import statement."
    },
    {
        "name": "importerror_cannot_import_name",
        "keywords": ["importerror", "cannot import name"],
        "cause": "The imported symbol does not exist or there is a circular import.",
        "possible_fix": "Check the object name and look for circular imports.",
        "recommended_command": "Review the import path and move shared code to a separate module.",
        "context": "Fix in Python source files."
    },
    {
        "name": "syntaxerror_invalid_syntax",
        "keywords": ["syntaxerror", "invalid syntax"],
        "cause": "Python found invalid code syntax.",
        "possible_fix": "Check the line shown in the traceback for missing punctuation or invalid structure.",
        "recommended_command": "python -m py_compile <file.py>",
        "context": "Run in terminal to validate the file."
    },
    {
        "name": "syntaxerror_eol_string",
        "keywords": ["syntaxerror", "unterminated string literal", "eol while scanning string literal"],
        "cause": "A string was opened but not closed.",
        "possible_fix": "Close the string quote properly.",
        "recommended_command": "Check the line highlighted in the traceback.",
        "context": "Fix in Python source file."
    },
    {
        "name": "indentationerror",
        "keywords": ["indentationerror", "unexpected indent", "unindent does not match"],
        "cause": "Indentation is inconsistent or invalid.",
        "possible_fix": "Use consistent indentation, preferably 4 spaces.",
        "recommended_command": "Format the file and replace tabs with spaces.",
        "context": "Fix in editor."
    },
    {
        "name": "taberror",
        "keywords": ["taberror", "inconsistent use of tabs and spaces"],
        "cause": "Tabs and spaces are mixed in indentation.",
        "possible_fix": "Convert tabs to spaces.",
        "recommended_command": "Set editor to insert spaces instead of tabs.",
        "context": "Fix in editor."
    },
    {
        "name": "nameerror",
        "keywords": ["nameerror", "is not defined"],
        "cause": "A variable or function name is being used before it exists.",
        "possible_fix": "Check spelling, scope, and definition order.",
        "recommended_command": "Search where the missing name should be defined.",
        "context": "Fix in Python source file."
    },
    {
        "name": "unboundlocalerror",
        "keywords": ["unboundlocalerror", "local variable referenced before assignment"],
        "cause": "A local variable is used before it gets a value.",
        "possible_fix": "Assign the variable before use or mark it global/nonlocal if intended.",
        "recommended_command": "Review function scope and assignment order.",
        "context": "Fix in Python source file."
    },
    {
        "name": "attributeerror",
        "keywords": ["attributeerror", "has no attribute"],
        "cause": "You are calling an attribute or method that does not exist on that object.",
        "possible_fix": "Check object type and attribute name.",
        "recommended_command": "Use print(type(obj)) or dir(obj) for inspection.",
        "context": "Run in terminal or debug in code."
    },
    {
        "name": "typeerror_wrong_arity",
        "keywords": ["typeerror", "missing 1 required positional argument", "takes", "positional arguments but"],
        "cause": "A function was called with the wrong number of arguments.",
        "possible_fix": "Match the call to the function signature.",
        "recommended_command": "Inspect the function definition or help(function_name).",
        "context": "Fix in Python source file or REPL."
    },
    {
        "name": "typeerror_none_not_callable",
        "keywords": ["typeerror", "'nonetype' object is not callable"],
        "cause": "A variable holding None is being called like a function.",
        "possible_fix": "Check whether a function name was overwritten or returned None.",
        "recommended_command": "Print the variable before calling it.",
        "context": "Fix in Python source file."
    },
    {
        "name": "typeerror_not_subscriptable",
        "keywords": ["typeerror", "object is not subscriptable"],
        "cause": "Indexing was used on a value that does not support it.",
        "possible_fix": "Check the type before using square brackets.",
        "recommended_command": "Use print(type(obj)) to inspect the object.",
        "context": "Run in terminal or debug in code."
    },
    {
        "name": "typeerror_unsupported_operand",
        "keywords": ["typeerror", "unsupported operand type"],
        "cause": "An operation is being applied to incompatible types.",
        "possible_fix": "Convert values to compatible types before the operation.",
        "recommended_command": "Inspect types with print(type(a), type(b)).",
        "context": "Run in terminal or debug in code."
    },
    {
        "name": "valueerror_invalid_literal",
        "keywords": ["valueerror", "invalid literal for int()", "invalid literal for float()"],
        "cause": "A string value cannot be converted to the requested numeric type.",
        "possible_fix": "Validate or clean the input before conversion.",
        "recommended_command": "Print the raw value before calling int() or float().",
        "context": "Run in terminal or fix input parsing in code."
    },
    {
        "name": "valueerror_unpacking",
        "keywords": ["valueerror", "too many values to unpack", "not enough values to unpack"],
        "cause": "The number of variables does not match the number of values returned.",
        "possible_fix": "Adjust the unpacking target count or inspect the returned data.",
        "recommended_command": "Print the returned object before unpacking.",
        "context": "Run in terminal or debug in code."
    },
    {
        "name": "valueerror_shape",
        "keywords": ["valueerror", "shape", "broadcast"],
        "cause": "Array or dataframe shapes do not align for the operation.",
        "possible_fix": "Check dimensions and reshape if needed.",
        "recommended_command": "Print array.shape or dataframe.shape before the operation.",
        "context": "Run in terminal or notebook."
    },
    {
        "name": "keyerror",
        "keywords": ["keyerror"],
        "cause": "A dictionary or mapping key does not exist.",
        "possible_fix": "Check key spelling or use dict.get() if the key may be missing.",
        "recommended_command": "Print the available keys with obj.keys().",
        "context": "Run in terminal or debug in code."
    },
    {
        "name": "indexerror",
        "keywords": ["indexerror", "list index out of range", "index out of bounds"],
        "cause": "An index is outside the valid range.",
        "possible_fix": "Check list length or loop bounds before indexing.",
        "recommended_command": "Print len(obj) before accessing by index.",
        "context": "Run in terminal or debug in code."
    },
    {
        "name": "zerodivisionerror",
        "keywords": ["zerodivisionerror", "division by zero"],
        "cause": "A calculation tried to divide by zero.",
        "possible_fix": "Guard against zero before dividing.",
        "recommended_command": "Add a condition before the division.",
        "context": "Fix in Python source file."
    },
    {
        "name": "filenotfounderror",
        "keywords": ["filenotfounderror", "no such file or directory"],
        "cause": "The file path is wrong or the file does not exist.",
        "possible_fix": "Check the path, working directory, and filename.",
        "recommended_command": "pwd && ls -la",
        "context": "Run in terminal."
    },
    {
        "name": "permissionerror",
        "keywords": ["permissionerror", "permission denied"],
        "cause": "The process does not have permission to access the file or directory.",
        "possible_fix": "Check file permissions, ownership, or run in an allowed location.",
        "recommended_command": "ls -l <path>",
        "context": "Run in terminal."
    },
    {
        "name": "isadirectoryerror",
        "keywords": ["isadirectoryerror", "is a directory"],
        "cause": "A directory path was used where a file path was expected.",
        "possible_fix": "Pass a file path instead of a directory path.",
        "recommended_command": "ls -la <path>",
        "context": "Run in terminal."
    },
    {
        "name": "notadirectoryerror",
        "keywords": ["notadirectoryerror", "not a directory"],
        "cause": "A file path was used where a directory path was expected.",
        "possible_fix": "Check the path and pass a real directory.",
        "recommended_command": "ls -la <path>",
        "context": "Run in terminal."
    },
    {
        "name": "unicodeencodeerror",
        "keywords": ["unicodeencodeerror"],
        "cause": "Text contains characters that cannot be encoded in the target encoding.",
        "possible_fix": "Use UTF-8 or specify error handling when encoding.",
        "recommended_command": "Open files with encoding='utf-8'.",
        "context": "Fix in Python source file."
    },
    {
        "name": "unicodedecodeerror",
        "keywords": ["unicodedecodeerror"],
        "cause": "The file or byte stream is being decoded with the wrong encoding.",
        "possible_fix": "Open the file with the correct encoding.",
        "recommended_command": "open(path, encoding='utf-8')",
        "context": "Fix in Python source file."
    },
    {
        "name": "recursionerror",
        "keywords": ["recursionerror", "maximum recursion depth exceeded"],
        "cause": "A recursive function does not reach a stopping condition soon enough.",
        "possible_fix": "Fix the base case or reduce recursion depth.",
        "recommended_command": "Review the recursive termination condition.",
        "context": "Fix in Python source file."
    },
    {
        "name": "memoryerror",
        "keywords": ["memoryerror"],
        "cause": "The process tried to allocate more memory than available.",
        "possible_fix": "Process data in chunks or reduce memory usage.",
        "recommended_command": "Load smaller batches or stream the input.",
        "context": "Refactor code or reduce dataset size."
    },
    {
        "name": "assertionerror",
        "keywords": ["assertionerror"],
        "cause": "An assertion failed because a required condition was false.",
        "possible_fix": "Inspect the values used in the assertion.",
        "recommended_command": "Print the compared values before the assert.",
        "context": "Run in terminal or tests."
    },
    {
        "name": "runtimeerror_event_loop",
        "keywords": ["runtimeerror", "event loop is already running"],
        "cause": "Async code tried to start an event loop while one is already active.",
        "possible_fix": "Avoid nested event loops or adapt code for notebook/async environment.",
        "recommended_command": "Use await directly in async-friendly environments.",
        "context": "Fix in Python source or notebook."
    },
    {
        "name": "runtimeerror_dictionary_changed",
        "keywords": ["runtimeerror", "dictionary changed size during iteration"],
        "cause": "A dictionary is being modified while iterating over it.",
        "possible_fix": "Iterate over a copy of keys/items instead.",
        "recommended_command": "Use list(my_dict.items()) in the loop.",
        "context": "Fix in Python source file."
    },
    {
        "name": "brokenpipeerror",
        "keywords": ["brokenpipeerror"],
        "cause": "The receiving end of a pipe or stream closed before writing finished.",
        "possible_fix": "Handle pipe closure or stop writing when the consumer exits.",
        "recommended_command": "Add proper pipe or subprocess error handling.",
        "context": "Fix in Python source file."
    },
    {
        "name": "oSError_address_in_use",
        "keywords": ["address already in use", "oserror", "errno 98", "errno 48"],
        "cause": "Another process is already using the requested port.",
        "possible_fix": "Stop the existing process or use a different port.",
        "recommended_command": "lsof -i :8000",
        "context": "Run in terminal."
    },
    {
        "name": "oserror_too_many_open_files",
        "keywords": ["too many open files"],
        "cause": "The process opened more files than the OS limit allows.",
        "possible_fix": "Close files properly or raise the file descriptor limit.",
        "recommended_command": "ulimit -n",
        "context": "Run in terminal."
    },
    {
        "name": "jsondecodeerror",
        "keywords": ["jsondecodeerror", "expecting value", "expecting property name enclosed in double quotes"],
        "cause": "Invalid JSON format was provided.",
        "possible_fix": "Validate the JSON and check commas, quotes, and brackets.",
        "recommended_command": "Print the raw JSON string before parsing.",
        "context": "Run in terminal or fix source data."
    },
    {
        "name": "pickle_error",
        "keywords": ["pickle", "can't pickle", "unpicklingerror"],
        "cause": "The object cannot be serialized/deserialized by pickle as used.",
        "possible_fix": "Avoid lambdas/local objects or check pickle compatibility.",
        "recommended_command": "Move the object definition to module scope.",
        "context": "Fix in Python source file."
    },
    {
        "name": "subprocess_calledprocesserror",
        "keywords": ["calledprocesserror"],
        "cause": "A subprocess returned a non-zero exit code.",
        "possible_fix": "Inspect the subprocess stderr/stdout for the real failure cause.",
        "recommended_command": "Print subprocess stderr and return code.",
        "context": "Fix in Python source file."
    },
    {
        "name": "subprocess_filenotfound",
        "keywords": ["filenotfounderror", "subprocess"],
        "cause": "The external command being called does not exist in PATH.",
        "possible_fix": "Install the command or provide the full executable path.",
        "recommended_command": "which <command>",
        "context": "Run in terminal."
    },
    {
        "name": "argparse_unrecognized_arguments",
        "keywords": ["unrecognized arguments"],
        "cause": "The script received CLI flags or values it does not accept.",
        "possible_fix": "Check the supported CLI arguments.",
        "recommended_command": "python <script.py> --help",
        "context": "Run in terminal."
    },
    {
        "name": "argparse_required_argument",
        "keywords": ["the following arguments are required"],
        "cause": "A required CLI argument is missing.",
        "possible_fix": "Pass all required arguments.",
        "recommended_command": "python <script.py> --help",
        "context": "Run in terminal."
    },
    {
        "name": "pytest_fixture_not_found",
        "keywords": ["fixture", "not found", "pytest"],
        "cause": "A pytest fixture name is missing or not discoverable.",
        "possible_fix": "Define the fixture or import it through conftest.py.",
        "recommended_command": "Check conftest.py and fixture naming.",
        "context": "Fix in test files."
    },
    {
        "name": "pytest_assertion_failure",
        "keywords": ["assert", "failed", "pytest"],
        "cause": "A test expectation did not match the actual result.",
        "possible_fix": "Inspect expected vs actual values.",
        "recommended_command": "Re-run the failing test with -vv.",
        "context": "Run in terminal."
    },
    {
        "name": "sqlite_operational_error",
        "keywords": ["sqlite3.operationalerror"],
        "cause": "SQLite operation failed due to path, lock, or SQL issue.",
        "possible_fix": "Check the DB path, locks, and query syntax.",
        "recommended_command": "Verify the SQLite file path and SQL statement.",
        "context": "Run in terminal or fix code."
    },
    {
        "name": "sqlite_readonly_database",
        "keywords": ["attempt to write a readonly database"],
        "cause": "The SQLite database file is not writable.",
        "possible_fix": "Check file permissions and directory ownership.",
        "recommended_command": "ls -l <database_file>",
        "context": "Run in terminal."
    },
    {
        "name": "sqlalchemy_operational_error",
        "keywords": ["sqlalchemy.exc.operationalerror"],
        "cause": "Database connection or SQL execution failed.",
        "possible_fix": "Check database URL, server availability, and query validity.",
        "recommended_command": "Print the DATABASE_URL (without secrets) and verify connectivity.",
        "context": "Run in terminal or inspect app config."
    },
    {
        "name": "sqlalchemy_integrity_error",
        "keywords": ["sqlalchemy.exc.integrityerror", "unique constraint", "foreign key constraint"],
        "cause": "The write operation violates a database constraint.",
        "possible_fix": "Check duplicate keys, missing references, or invalid values.",
        "recommended_command": "Inspect the failing row and DB constraints.",
        "context": "Fix in app logic or DB data."
    },
    {
        "name": "psycopg2_insufficient_privilege",
        "keywords": ["insufficientprivilege", "permission denied for schema public"],
        "cause": "The database user does not have the required permissions on the schema.",
        "possible_fix": "Grant the required permissions or use a user with proper privileges.",
        "recommended_command": "GRANT CREATE ON SCHEMA public TO your_user;",
        "context": "Run in psql or a PostgreSQL admin tool."
    },
    {
        "name": "psycopg2_duplicate_table",
        "keywords": ["duplicatetable", "relation", "already exists"],
        "cause": "The table or relation already exists.",
        "possible_fix": "Use IF NOT EXISTS, drop it first, or update the migration logic.",
        "recommended_command": "Check the DB schema before creating the table again.",
        "context": "Run in psql or fix migration/code logic."
    },
    {
        "name": "psycopg2_duplicate_key",
        "keywords": ["duplicate key value violates unique constraint"],
        "cause": "An insert or update violates a unique constraint.",
        "possible_fix": "Use a unique value or handle upserts properly.",
        "recommended_command": "Inspect the conflicting key values before insert.",
        "context": "Fix in app logic or SQL."
    },
    {
        "name": "psycopg2_connection_refused",
        "keywords": ["connection refused", "could not connect to server"],
        "cause": "The PostgreSQL server is not reachable or not running.",
        "possible_fix": "Start the server and verify host/port settings.",
        "recommended_command": "pg_isready",
        "context": "Run in terminal."
    },
    {
        "name": "psycopg2_auth_failed",
        "keywords": ["password authentication failed", "fe_sendauth"],
        "cause": "Database credentials are incorrect.",
        "possible_fix": "Check username, password, and connection string.",
        "recommended_command": "Verify DATABASE_URL and DB user credentials.",
        "context": "Inspect environment variables or config."
    },
    {
        "name": "django_improperly_configured",
        "keywords": ["django.core.exceptions.improperlyconfigured"],
        "cause": "Django settings or app configuration is invalid or incomplete.",
        "possible_fix": "Check DJANGO_SETTINGS_MODULE, INSTALLED_APPS, and environment variables.",
        "recommended_command": "python manage.py check",
        "context": "Run in terminal from project root."
    },
    {
        "name": "django_no_such_table",
        "keywords": ["django.db.utils.operationalerror", "no such table"],
        "cause": "The database schema is missing required tables.",
        "possible_fix": "Run migrations.",
        "recommended_command": "python manage.py migrate",
        "context": "Run in terminal from project root."
    },
    {
        "name": "django_app_registry_not_ready",
        "keywords": ["apps aren't loaded yet", "app registry isn't ready yet"],
        "cause": "Django code is being imported or executed before app initialization finishes.",
        "possible_fix": "Avoid importing models too early.",
        "recommended_command": "Move imports inside functions if needed.",
        "context": "Fix in Django source files."
    },
    {
        "name": "flask_working_outside_context",
        "keywords": ["working outside of application context", "working outside of request context"],
        "cause": "Flask context-dependent objects are being used outside the proper app/request context.",
        "possible_fix": "Use app.app_context() or move code into request handling.",
        "recommended_command": "Wrap the code with app.app_context() if appropriate.",
        "context": "Fix in Flask source file."
    },
    {
        "name": "jinja_template_not_found",
        "keywords": ["templatenotfound"],
        "cause": "The requested template file cannot be found.",
        "possible_fix": "Check the template path and template folder configuration.",
        "recommended_command": "Verify the template exists under the templates directory.",
        "context": "Fix in project structure or render call."
    },
    {
        "name": "fastapi_uvicorn_asgi_error",
        "keywords": ["error loading asgi app"],
        "cause": "The ASGI app path is wrong or the app object cannot be imported.",
        "possible_fix": "Check the module path and app variable name.",
        "recommended_command": "uvicorn app.main:app --reload",
        "context": "Run in terminal from project root."
    },
    {
        "name": "fastapi_pydantic_validation",
        "keywords": ["validationerror", "field required", "input should be"],
        "cause": "Request or model data does not match the expected schema.",
        "possible_fix": "Check the payload fields and types against the schema.",
        "recommended_command": "Compare request JSON to the Pydantic model.",
        "context": "Fix client payload or schema."
    },
    {
        "name": "fastapi_response_validation",
        "keywords": ["responsevalidationerror"],
        "cause": "The returned response does not match the declared response model.",
        "possible_fix": "Update the returned data or adjust the response model.",
        "recommended_command": "Compare returned dict keys/types to the response model.",
        "context": "Fix in FastAPI route code."
    },
    {
        "name": "pydantic_missing_field",
        "keywords": ["field required"],
        "cause": "A required field is missing from the input data.",
        "possible_fix": "Provide the required field or make it optional in the model.",
        "recommended_command": "Review the model definition and input payload.",
        "context": "Fix in payload or model."
    },
    {
        "name": "pydantic_extra_forbidden",
        "keywords": ["extra inputs are not permitted"],
        "cause": "The input includes fields not allowed by the model config.",
        "possible_fix": "Remove extra fields or allow them explicitly.",
        "recommended_command": "Review model config for extra handling.",
        "context": "Fix in payload or model."
    },
    {
        "name": "numpy_axis_error",
        "keywords": ["axiserror", "axis", "is out of bounds"],
        "cause": "The code references an axis that does not exist.",
        "possible_fix": "Check the array dimensions before using the axis.",
        "recommended_command": "Print arr.shape before the operation.",
        "context": "Run in terminal or notebook."
    },
    {
        "name": "numpy_broadcast_error",
        "keywords": ["operands could not be broadcast together"],
        "cause": "Array shapes are incompatible for broadcasting.",
        "possible_fix": "Reshape arrays or align dimensions.",
        "recommended_command": "Print shapes of both arrays before the operation.",
        "context": "Run in terminal or notebook."
    },
    {
        "name": "pandas_keyerror",
        "keywords": ["keyerror", "not in index"],
        "cause": "A dataframe column or index label does not exist.",
        "possible_fix": "Check column names and whitespace/casing.",
        "recommended_command": "print(df.columns.tolist())",
        "context": "Run in terminal or notebook."
    },
    {
        "name": "pandas_attribute_error",
        "keywords": ["dataframe object has no attribute"],
        "cause": "A dataframe method or attribute name is wrong.",
        "possible_fix": "Check pandas API usage and whether bracket notation is needed.",
        "recommended_command": "Use df['column'] instead of df.column where appropriate.",
        "context": "Fix in Python source or notebook."
    },
    {
        "name": "pandas_parser_error",
        "keywords": ["parsererror", "error tokenizing data"],
        "cause": "The input CSV or delimited file is malformed.",
        "possible_fix": "Check delimiter, quoting, and broken rows.",
        "recommended_command": "pd.read_csv(path, on_bad_lines='skip')",
        "context": "Run in code or inspect input file."
    },
    {
        "name": "pandas_merge_keyerror",
        "keywords": ["merge", "keyerror"],
        "cause": "A merge key is missing in one of the dataframes.",
        "possible_fix": "Check both dataframes for the merge column.",
        "recommended_command": "print(left.columns, right.columns)",
        "context": "Run in terminal or notebook."
    },
    {
        "name": "requests_connection_error",
        "keywords": ["requests.exceptions.connectionerror"],
        "cause": "The HTTP request could not connect to the server.",
        "possible_fix": "Check network access, DNS, and the target URL.",
        "recommended_command": "curl <url>",
        "context": "Run in terminal."
    },
    {
        "name": "requests_timeout",
        "keywords": ["requests.exceptions.timeout", "readtimeout", "connecttimeout"],
        "cause": "The HTTP request took too long.",
        "possible_fix": "Increase timeout or check server responsiveness.",
        "recommended_command": "Try a larger timeout value in code.",
        "context": "Fix in Python source file."
    },
    {
        "name": "requests_json_decode",
        "keywords": ["jsondecodeerror", "requests"],
        "cause": "The HTTP response is not valid JSON.",
        "possible_fix": "Inspect response.text before calling .json().",
        "recommended_command": "print(response.status_code, response.text)",
        "context": "Run in terminal or debug in code."
    },
    {
        "name": "aiohttp_client_error",
        "keywords": ["aiohttp.clienterror"],
        "cause": "The async HTTP request failed due to connection or protocol issues.",
        "possible_fix": "Check the URL, network, and exception details.",
        "recommended_command": "Log the full exception and response status.",
        "context": "Fix in Python source file."
    },
    {
        "name": "ssl_cert_verify_failed",
        "keywords": ["ssl: certificate_verify_failed", "certificate verify failed"],
        "cause": "TLS certificate verification failed.",
        "possible_fix": "Check system cert store, target cert validity, or custom CA setup.",
        "recommended_command": "Verify the endpoint certificate with curl or openssl.",
        "context": "Run in terminal."
    },
    {
        "name": "dotenv_missing_env",
        "keywords": ["keyerror", "environment variable", "none", "database_url"],
        "cause": "A required environment variable is missing or not loaded.",
        "possible_fix": "Set the variable or load the .env file correctly.",
        "recommended_command": "print(os.getenv('<VAR_NAME>'))",
        "context": "Run in Python or inspect shell env."
    },
    {
        "name": "venv_wrong_python",
        "keywords": ["no module named", "using system python", "venv"],
        "cause": "The wrong Python interpreter is being used.",
        "possible_fix": "Activate the virtual environment or run the correct interpreter.",
        "recommended_command": "which python && which pip",
        "context": "Run in terminal."
    },
    {
        "name": "pip_requirements_wrong_command",
        "keywords": ["could not find a version that satisfies the requirement", "requirements.txt"],
        "cause": "requirements.txt was treated as a package name instead of a requirements file.",
        "possible_fix": "Use the -r flag.",
        "recommended_command": "pip install -r requirements.txt",
        "context": "Run in terminal."
    },
    {
        "name": "pip_permission_denied",
        "keywords": ["permission denied", "site-packages", "pip"],
        "cause": "pip does not have permission to write to the target location.",
        "possible_fix": "Use a virtual environment instead of system install.",
        "recommended_command": "python -m venv .venv && source .venv/bin/activate",
        "context": "Run in terminal."
    },
    {
        "name": "pip_dependency_conflict",
        "keywords": ["resolutionimpossible", "dependency conflict"],
        "cause": "Installed package versions have incompatible dependency requirements.",
        "possible_fix": "Pin compatible versions or use a clean virtual environment.",
        "recommended_command": "pip freeze > requirements.lock",
        "context": "Run in terminal."
    },
    {
        "name": "setuptools_build_failed",
        "keywords": ["error: subprocess-exited-with-error", "failed building wheel"],
        "cause": "A package build failed, often due to missing system dependencies.",
        "possible_fix": "Install build tools or use a prebuilt wheel if available.",
        "recommended_command": "Check the package docs for OS-level dependencies.",
        "context": "Run in terminal."
    },
    {
        "name": "python_command_not_found",
        "keywords": ["python: command not found"],
        "cause": "Python is not installed or not available in PATH under that command name.",
        "possible_fix": "Use python3 or install/configure Python properly.",
        "recommended_command": "python3 --version",
        "context": "Run in terminal."
    },
    {
        "name": "pytest_command_not_found",
        "keywords": ["pytest: command not found"],
        "cause": "pytest is not installed in the active environment.",
        "possible_fix": "Install pytest in the current environment.",
        "recommended_command": "pip install pytest",
        "context": "Run in your active virtual environment."
    },
    {
        "name": "uvicorn_command_not_found",
        "keywords": ["uvicorn: command not found"],
        "cause": "uvicorn is not installed in the active environment.",
        "possible_fix": "Install uvicorn in the current environment.",
        "recommended_command": "pip install uvicorn",
        "context": "Run in your active virtual environment."
    },
    {
        "name": "django_manage_py_missing",
        "keywords": ["can't open file", "manage.py"],
        "cause": "The command is being run from the wrong directory or manage.py is missing.",
        "possible_fix": "Change to the Django project root.",
        "recommended_command": "pwd && ls -la",
        "context": "Run in terminal."
    },
    {
        "name": "fastapi_404_route",
        "keywords": ["404 not found", "fastapi"],
        "cause": "The requested route does not exist or method/path is wrong.",
        "possible_fix": "Check route path, prefix, and HTTP method.",
        "recommended_command": "Open /docs and verify registered endpoints.",
        "context": "Run app and inspect Swagger docs."
    },
    {
        "name": "sqlmodel_table_not_found",
        "keywords": ["no such table", "relation", "does not exist", "sqlmodel"],
        "cause": "Models exist but tables were not created or migrations not applied.",
        "possible_fix": "Create tables or apply migrations before querying.",
        "recommended_command": "Run metadata.create_all(engine) or migrate properly.",
        "context": "Fix in app startup or DB workflow."
    },
    {
        "name": "alembic_revision_not_found",
        "keywords": ["can't locate revision identified by"],
        "cause": "Alembic migration history is out of sync.",
        "possible_fix": "Check migrations folder and DB revision state.",
        "recommended_command": "alembic history",
        "context": "Run in terminal from project root."
    },
    {
        "name": "alembic_target_not_up_to_date",
        "keywords": ["target database is not up to date"],
        "cause": "Pending migrations have not been applied.",
        "possible_fix": "Upgrade the database to the latest revision.",
        "recommended_command": "alembic upgrade head",
        "context": "Run in terminal from project root."
    },
    {
        "name": "jinja_undefined_error",
        "keywords": ["undefinederror"],
        "cause": "A template references a variable that was not passed to it.",
        "possible_fix": "Pass the variable from the view/function or guard for missing values.",
        "recommended_command": "Check the render context and template variable names.",
        "context": "Fix in template/render code."
    },
    {
        "name": "celery_broker_connection",
        "keywords": ["kombu.exceptions.operationalerror", "connection refused", "celery"],
        "cause": "Celery cannot connect to the message broker.",
        "possible_fix": "Start Redis/RabbitMQ and verify broker URL.",
        "recommended_command": "Check the broker service and CELERY_BROKER_URL.",
        "context": "Run in terminal or inspect config."
    },
    {
        "name": "redis_connection_error",
        "keywords": ["redis.exceptions.connectionerror"],
        "cause": "Redis is unreachable or not running.",
        "possible_fix": "Start Redis and verify host/port.",
        "recommended_command": "redis-cli ping",
        "context": "Run in terminal."
    },
    {
        "name": "matplotlib_display_error",
        "keywords": ["cannot connect to x server", "matplotlib", "display"],
        "cause": "A GUI backend is being used in a headless environment.",
        "possible_fix": "Use a non-GUI backend like Agg.",
        "recommended_command": "import matplotlib; matplotlib.use('Agg')",
        "context": "Set in Python source before importing pyplot."
    },
    {
        "name": "seaborn_or_matplotlib_import_error",
        "keywords": ["importerror", "matplotlib", "seaborn"],
        "cause": "Plotting dependency versions may be incompatible or missing.",
        "possible_fix": "Install compatible versions in a clean environment.",
        "recommended_command": "pip install matplotlib seaborn",
        "context": "Run in active virtual environment."
    },
    {
        "name": "sklearn_not_fitted",
        "keywords": ["notfittederror", "is not fitted yet"],
        "cause": "A scikit-learn model is being used before fit() was called.",
        "possible_fix": "Train the model before predict/transform.",
        "recommended_command": "Call model.fit(X_train, y_train) first.",
        "context": "Fix in ML workflow code."
    },
    {
        "name": "sklearn_feature_mismatch",
        "keywords": ["x has", "features, but", "is expecting"],
        "cause": "Input feature count does not match the trained model.",
        "possible_fix": "Use the same feature columns/order as training.",
        "recommended_command": "Compare training features to prediction input.",
        "context": "Fix in ML pipeline code."
    },
    {
        "name": "torch_cuda_unavailable",
        "keywords": ["torch", "cuda", "not available"],
        "cause": "CUDA is not available to PyTorch in this environment.",
        "possible_fix": "Use CPU or install the correct CUDA-enabled build.",
        "recommended_command": "python -c \"import torch; print(torch.cuda.is_available())\"",
        "context": "Run in terminal."
    },
    {
        "name": "tensorflow_no_module",
        "keywords": ["no module named 'tensorflow'"],
        "cause": "TensorFlow is not installed in the active environment.",
        "possible_fix": "Install TensorFlow in the correct environment.",
        "recommended_command": "pip install tensorflow",
        "context": "Run in active virtual environment."
    },
    {
        "name": "tensorflow_shape_mismatch",
        "keywords": ["incompatible shapes", "shapes", "tensorflow"],
        "cause": "Tensor shapes are incompatible for the operation.",
        "possible_fix": "Inspect input tensor shapes and model expectations.",
        "recommended_command": "Print tensor shapes before the failing op.",
        "context": "Run in notebook or debug in code."
    },
    {
        "name": "openpyxl_invalid_file",
        "keywords": ["invalidfileexception", "openpyxl"],
        "cause": "The file is not a valid Excel workbook for openpyxl.",
        "possible_fix": "Verify file format and extension.",
        "recommended_command": "Check whether the file is truly .xlsx.",
        "context": "Inspect file before loading."
    },
    {
        "name": "yaml_scanner_error",
        "keywords": ["scannererror", "yaml"],
        "cause": "The YAML file has invalid indentation or syntax.",
        "possible_fix": "Check spacing, colons, and list indentation.",
        "recommended_command": "Validate the YAML structure in an online linter or parser.",
        "context": "Fix in YAML config file."
    },
    {
        "name": "toml_parse_error",
        "keywords": ["toml", "parse error", "invalid statement"],
        "cause": "The TOML config file contains invalid syntax.",
        "possible_fix": "Check quotes, brackets, and assignment structure.",
        "recommended_command": "Validate pyproject.toml syntax carefully.",
        "context": "Fix in TOML file."
    },
    {
        "name": "logging_basicconfig_ignored",
        "keywords": ["basicconfig", "not working", "logging"],
        "cause": "Logging was configured after handlers were already created.",
        "possible_fix": "Configure logging early before other imports initialize handlers.",
        "recommended_command": "Move logging.basicConfig() near the program entrypoint.",
        "context": "Fix in Python startup code."
    },
    {
        "name": "asyncio_coroutine_never_awaited",
        "keywords": ["coroutine", "was never awaited"],
        "cause": "An async function was called without await.",
        "possible_fix": "Await the coroutine or run it in the event loop.",
        "recommended_command": "Use await my_coroutine() inside async code.",
        "context": "Fix in Python source file."
    },
    {
        "name": "asyncio_task_destroyed",
        "keywords": ["task was destroyed but it is pending"],
        "cause": "An async task was left pending when the loop closed.",
        "possible_fix": "Await or cancel tasks properly before shutdown.",
        "recommended_command": "Track created tasks and await them before exit.",
        "context": "Fix in async workflow."
    },
    {
        "name": "dataclass_missing_default_order",
        "keywords": ["non-default argument follows default argument"],
        "cause": "In a function or dataclass, required fields appear after defaulted ones.",
        "possible_fix": "Place non-default parameters before default ones.",
        "recommended_command": "Reorder the parameters or fields.",
        "context": "Fix in Python source file."
    },
    {
        "name": "pathlib_type_mismatch",
        "keywords": ["expected str, bytes or os.PathLike object"],
        "cause": "A path argument received the wrong type.",
        "possible_fix": "Pass a string or Path object, not a different object type.",
        "recommended_command": "Wrap paths with Path(...) if needed.",
        "context": "Fix in Python source file."
    },
    {
        "name": "csv_field_larger_than_limit",
        "keywords": ["field larger than field limit"],
        "cause": "A CSV field exceeds the parser field size limit.",
        "possible_fix": "Increase the CSV field size limit before reading.",
        "recommended_command": "csv.field_size_limit(new_limit)",
        "context": "Set in Python code before reading CSV."
    },
    {
        "name": "httpx_connect_error",
        "keywords": ["httpx.connecterror"],
        "cause": "The HTTP request could not establish a connection.",
        "possible_fix": "Check URL, DNS, network, and target server availability.",
        "recommended_command": "curl <url>",
        "context": "Run in terminal."
    },
    {
        "name": "httpx_timeout",
        "keywords": ["httpx.readtimeout", "httpx.connecttimeout", "httpx.timeoutexception"],
        "cause": "The HTTP request timed out.",
        "possible_fix": "Increase the timeout or verify the remote service speed.",
        "recommended_command": "Set a higher timeout in the httpx client.",
        "context": "Fix in Python source file."
    },
    {
        "name": "click_no_such_option",
        "keywords": ["no such option"],
        "cause": "A Click CLI command received an unsupported option.",
        "possible_fix": "Use the defined CLI flags only.",
        "recommended_command": "<command> --help",
        "context": "Run in terminal."
    },
    {
        "name": "click_missing_argument",
        "keywords": ["missing argument"],
        "cause": "A required CLI argument was not provided.",
        "possible_fix": "Pass all required CLI arguments.",
        "recommended_command": "<command> --help",
        "context": "Run in terminal."
    },
    {
        "name": "datetime_parse_error",
        "keywords": ["does not match format", "unconverted data remains"],
        "cause": "A date string does not match the expected datetime format.",
        "possible_fix": "Adjust the format string or clean the input value.",
        "recommended_command": "Print the raw datetime string before parsing.",
        "context": "Run in terminal or fix parsing code."
    },
    {
        "name": "decimal_invalid_operation",
        "keywords": ["decimal.invalidoperation"],
        "cause": "A Decimal operation received invalid input or invalid arithmetic conditions.",
        "possible_fix": "Validate the input string/value before converting to Decimal.",
        "recommended_command": "Print the raw value before Decimal(value).",
        "context": "Run in terminal or debug in code."
    },
    {
        "name": "fraction_division_zero",
        "keywords": ["fractions", "zerodivisionerror"],
        "cause": "A Fraction denominator became zero.",
        "possible_fix": "Validate inputs before constructing the fraction.",
        "recommended_command": "Check denominator values before Fraction(a, b).",
        "context": "Fix in Python source file."
    }
]
