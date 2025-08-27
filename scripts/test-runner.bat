@echo off
setlocal enabledelayedexpansion

REM Test Runner Script for CI/CD Pipeline Simulation (Windows)
REM This script allows you to test different modes locally

REM Default values
set FRAMEWORK=all
set TEST_MODE=normal
set INCLUDE_FAILING_TESTS=true

REM Parse command line arguments
:parse_args
if "%~1"=="" goto :main
if /i "%~1"=="-f" (
    set FRAMEWORK=%~2
    shift
    shift
    goto :parse_args
)
if /i "%~1"=="--framework" (
    set FRAMEWORK=%~2
    shift
    shift
    goto :parse_args
)
if /i "%~1"=="-m" (
    set TEST_MODE=%~2
    shift
    shift
    goto :parse_args
)
if /i "%~1"=="--mode" (
    set TEST_MODE=%~2
    shift
    shift
    goto :parse_args
)
if /i "%~1"=="-i" (
    set INCLUDE_FAILING_TESTS=%~2
    shift
    shift
    goto :parse_args
)
if /i "%~1"=="--include-failing" (
    set INCLUDE_FAILING_TESTS=%~2
    shift
    shift
    goto :parse_args
)
if /i "%~1"=="-h" (
    goto :usage
)
if /i "%~1"=="--help" (
    goto :usage
)
echo Unknown option: %~1
goto :usage

:usage
echo Usage: %0 [OPTIONS]
echo.
echo Options:
echo   -f, --framework FRAMEWORK    Test framework to run (all, junit, pytest, jest)
echo   -m, --mode MODE              Test execution mode (normal, force_pass, force_fail, mixed_results)
echo   -i, --include-failing BOOL   Include intentionally failing tests (true, false)
echo   -h, --help                   Show this help message
echo.
echo Examples:
echo   %0 -f pytest -m force_pass
echo   %0 -f all -m mixed_results -i false
echo   %0 -f jest -m force_fail
exit /b 1

:main
echo 🚀 Test Runner - CI/CD Pipeline Simulation
echo ================================================
echo Framework: %FRAMEWORK%
echo Test Mode: %TEST_MODE%
echo Include Failing Tests: %INCLUDE_FAILING_TESTS%
echo.

REM Configure and run tests based on framework
if "%FRAMEWORK%"=="all" (
    call :configure_python_tests
    call :configure_nodejs_tests
    call :run_python_tests
    call :run_nodejs_tests
) else if "%FRAMEWORK%"=="pytest" (
    call :configure_python_tests
    call :run_python_tests
) else if "%FRAMEWORK%"=="jest" (
    call :configure_nodejs_tests
    call :run_nodejs_tests
) else if "%FRAMEWORK%"=="junit" (
    echo JUnit tests not yet implemented in Windows script
    echo Please use the GitHub Actions workflow for JUnit tests
)

echo ✅ Test run completed!
exit /b 0

:configure_python_tests
echo Configuring Python tests...
cd python-service

if "%TEST_MODE%"=="force_pass" (
    echo 🟢 Force Pass Mode: Commenting out failing tests
    powershell -Command "(Get-Content tests/unit/test_calculator_service.py) -replace 'def test_.*_failing', '# def test_.*_failing' | Set-Content tests/unit/test_calculator_service.py"
    powershell -Command "(Get-Content tests/unit/test_string_service.py) -replace 'def test_.*_failing', '# def test_.*_failing' | Set-Content tests/unit/test_string_service.py"
) else if "%TEST_MODE%"=="force_fail" (
    echo 🔴 Force Fail Mode: Making all tests fail
    powershell -Command "(Get-Content tests/unit/test_calculator_service.py) -replace 'assert result == 8.0', 'assert result == 999.0' | Set-Content tests/unit/test_calculator_service.py"
    powershell -Command "(Get-Content tests/unit/test_string_service.py) -replace 'assert result == \"olleh\"', 'assert result == \"FAIL\"' | Set-Content tests/unit/test_string_service.py"
) else if "%TEST_MODE%"=="mixed_results" (
    echo 🟡 Mixed Results Mode: Some tests will pass, some will fail
    powershell -Command "(Get-Content tests/unit/test_calculator_service.py) -replace 'def test_add_positive_numbers_failing', '# def test_add_positive_numbers_failing' | Set-Content tests/unit/test_calculator_service.py"
)

if "%INCLUDE_FAILING_TESTS%"=="false" (
    echo 🚫 Excluding intentionally failing tests
    powershell -Command "(Get-Content tests/unit/test_calculator_service.py) -replace 'def test_.*_failing', '# def test_.*_failing' | Set-Content tests/unit/test_calculator_service.py"
    powershell -Command "(Get-Content tests/unit/test_string_service.py) -replace 'def test_.*_failing', '# def test_.*_failing' | Set-Content tests/unit/test_string_service.py"
)

cd ..
goto :eof

:configure_nodejs_tests
echo Configuring Node.js tests...
cd node-service

if "%TEST_MODE%"=="force_pass" (
    echo 🟢 Force Pass Mode: Commenting out failing tests
    powershell -Command "(Get-Content tests/unit/calculatorService.test.js) -replace 'test.*INTENTIONALLY FAILING', '# test.*INTENTIONALLY FAILING' | Set-Content tests/unit/calculatorService.test.js"
    powershell -Command "(Get-Content tests/unit/stringService.test.js) -replace 'test.*INTENTIONALLY FAILING', '# test.*INTENTIONALLY FAILING' | Set-Content tests/unit/stringService.test.js"
) else if "%TEST_MODE%"=="force_fail" (
    echo 🔴 Force Fail Mode: Making all tests fail
    powershell -Command "(Get-Content tests/unit/calculatorService.test.js) -replace 'expect(result).toBe(8)', 'expect(result).toBe(999)' | Set-Content tests/unit/calculatorService.test.js"
    powershell -Command "(Get-Content tests/unit/stringService.test.js) -replace 'expect(result).toBe(\"olleh\")', 'expect(result).toBe(\"FAIL\")' | Set-Content tests/unit/stringService.test.js"
) else if "%TEST_MODE%"=="mixed_results" (
    echo 🟡 Mixed Results Mode: Some tests will pass, some will fail
    powershell -Command "(Get-Content tests/unit/calculatorService.test.js) -replace 'test.*INTENTIONALLY FAILING.*calculator', '# test.*INTENTIONALLY FAILING.*calculator' | Set-Content tests/unit/calculatorService.test.js"
)

if "%INCLUDE_FAILING_TESTS%"=="false" (
    echo 🚫 Excluding intentionally failing tests
    powershell -Command "(Get-Content tests/unit/calculatorService.test.js) -replace 'test.*INTENTIONALLY FAILING', '# test.*INTENTIONALLY FAILING' | Set-Content tests/unit/calculatorService.test.js"
    powershell -Command "(Get-Content tests/unit/stringService.test.js) -replace 'test.*INTENTIONALLY FAILING', '# test.*INTENTIONALLY FAILING' | Set-Content tests/unit/stringService.test.js"
)

cd ..
goto :eof

:run_python_tests
echo Running Python tests...
cd python-service

python -m pip install -r requirements.txt
python -m pytest tests/unit/ -v

cd ..
goto :eof

:run_nodejs_tests
echo Running Node.js tests...
cd node-service

if not exist node_modules (
    echo Installing dependencies...
    npm install
)

npm test

cd ..
goto :eof
