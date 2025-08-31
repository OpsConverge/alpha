#!/bin/bash

# Test Runner Script for CI/CD Pipeline Simulation
# This script allows you to test different modes locally

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default values
FRAMEWORK="all"
TEST_MODE="normal"
INCLUDE_FAILING_TESTS="true"

# Function to display usage
usage() {
    echo -e "${BLUE}Usage: $0 [OPTIONS]${NC}"
    echo ""
    echo "Options:"
    echo "  -f, --framework FRAMEWORK    Test framework to run (all, junit, pytest, jest)"
    echo "  -m, --mode MODE              Test execution mode (normal, force_pass, force_fail, mixed_results)"
    echo "  -i, --include-failing BOOL   Include intentionally failing tests (true, false)"
    echo "  -h, --help                   Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 -f pytest -m force_pass"
    echo "  $0 -f all -m mixed_results -i false"
    echo "  $0 -f jest -m force_fail"
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -f|--framework)
            FRAMEWORK="$2"
            shift 2
            ;;
        -m|--mode)
            TEST_MODE="$2"
            shift 2
            ;;
        -i|--include-failing)
            INCLUDE_FAILING_TESTS="$2"
            shift 2
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            usage
            exit 1
            ;;
    esac
done

echo -e "${BLUE}🚀 Test Runner - CI/CD Pipeline Simulation${NC}"
echo "================================================"
echo -e "Framework: ${YELLOW}$FRAMEWORK${NC}"
echo -e "Test Mode: ${YELLOW}$TEST_MODE${NC}"
echo -e "Include Failing Tests: ${YELLOW}$INCLUDE_FAILING_TESTS${NC}"
echo ""

# Function to configure Python tests
configure_python_tests() {
    echo -e "${BLUE}Configuring Python tests...${NC}"
    cd python-service
    
    if [ "$TEST_MODE" = "force_pass" ]; then
        echo -e "${GREEN}🟢 Force Pass Mode: Commenting out failing tests${NC}"
        sed -i.bak 's/def test_.*_failing/# def test_.*_failing/' tests/unit/test_calculator_service.py
        sed -i.bak 's/def test_.*_failing/# def test_.*_failing/' tests/unit/test_string_service.py
    elif [ "$TEST_MODE" = "force_fail" ]; then
        echo -e "${RED}🔴 Force Fail Mode: Making all tests fail${NC}"
        sed -i.bak 's/assert result == 8.0/assert result == 999.0/' tests/unit/test_calculator_service.py
        sed -i.bak 's/assert result == "olleh"/assert result == "FAIL"/' tests/unit/test_string_service.py
    elif [ "$TEST_MODE" = "mixed_results" ]; then
        echo -e "${YELLOW}🟡 Mixed Results Mode: Some tests will pass, some will fail${NC}"
        sed -i.bak 's/def test_add_positive_numbers_failing/# def test_add_positive_numbers_failing/' tests/unit/test_calculator_service.py
    fi
    
    if [ "$INCLUDE_FAILING_TESTS" = "false" ]; then
        echo -e "${YELLOW}🚫 Excluding intentionally failing tests${NC}"
        sed -i.bak 's/def test_.*_failing/# def test_.*_failing/' tests/unit/test_calculator_service.py
        sed -i.bak 's/def test_.*_failing/# def test_.*_failing/' tests/unit/test_string_service.py
    fi
    
    cd ..
}

# Function to configure Node.js tests
configure_nodejs_tests() {
    echo -e "${BLUE}Configuring Node.js tests...${NC}"
    cd node-service
    
    if [ "$TEST_MODE" = "force_pass" ]; then
        echo -e "${GREEN}🟢 Force Pass Mode: Commenting out failing tests${NC}"
        sed -i.bak 's/test.*INTENTIONALLY FAILING/# test.*INTENTIONALLY FAILING/' tests/unit/calculatorService.test.js
        sed -i.bak 's/test.*INTENTIONALLY FAILING/# test.*INTENTIONALLY FAILING/' tests/unit/stringService.test.js
    elif [ "$TEST_MODE" = "force_fail" ]; then
        echo -e "${RED}🔴 Force Fail Mode: Making all tests fail${NC}"
        sed -i.bak 's/expect(result).toBe(8)/expect(result).toBe(999)/' tests/unit/calculatorService.test.js
        sed -i.bak 's/expect(result).toBe("olleh")/expect(result).toBe("FAIL")/' tests/unit/stringService.test.js
    elif [ "$TEST_MODE" = "mixed_results" ]; then
        echo -e "${YELLOW}🟡 Mixed Results Mode: Some tests will pass, some will fail${NC}"
        sed -i.bak 's/test.*INTENTIONALLY FAILING.*calculator/# test.*INTENTIONALLY FAILING.*calculator/' tests/unit/calculatorService.test.js
    fi
    
    if [ "$INCLUDE_FAILING_TESTS" = "false" ]; then
        echo -e "${YELLOW}🚫 Excluding intentionally failing tests${NC}"
        sed -i.bak 's/test.*INTENTIONALLY FAILING/# test.*INTENTIONALLY FAILING/' tests/unit/calculatorService.test.js
        sed -i.bak 's/test.*INTENTIONALLY FAILING/# test.*INTENTIONALLY FAILING/' tests/unit/stringService.test.js
    fi
    
    cd ..
}

# Function to run Python tests
run_python_tests() {
    echo -e "${BLUE}Running Python tests...${NC}"
    cd python-service
    
    if ! command -v pytest &> /dev/null; then
        echo -e "${YELLOW}Installing pytest...${NC}"
        pip install -r requirements.txt
    fi
    
    pytest tests/unit/ -v --tb=short
    
    cd ..
}

# Function to run Node.js tests
run_nodejs_tests() {
    echo -e "${BLUE}Running Node.js tests...${NC}"
    cd node-service
    
    if [ ! -d "node_modules" ]; then
        echo -e "${YELLOW}Installing dependencies...${NC}"
        npm install
    fi
    
    npm test
    
    cd ..
}

# Function to restore original files
restore_files() {
    echo -e "${BLUE}Restoring original test files...${NC}"
    
    # Restore Python files
    if [ -f "python-service/tests/unit/test_calculator_service.py.bak" ]; then
        mv python-service/tests/unit/test_calculator_service.py.bak python-service/tests/unit/test_calculator_service.py
    fi
    if [ -f "python-service/tests/unit/test_string_service.py.bak" ]; then
        mv python-service/tests/unit/test_string_service.py.bak python-service/tests/unit/test_string_service.py
    fi
    
    # Restore Node.js files
    if [ -f "node-service/tests/unit/calculatorService.test.js.bak" ]; then
        mv node-service/tests/unit/calculatorService.test.js.bak node-service/tests/unit/calculatorService.test.js
    fi
    if [ -f "node-service/tests/unit/stringService.test.js.bak" ]; then
        mv node-service/tests/unit/stringService.test.js.bak node-service/tests/unit/stringService.test.js
    fi
}

# Main execution
main() {
    # Configure tests based on mode
    if [ "$FRAMEWORK" = "all" ] || [ "$FRAMEWORK" = "pytest" ]; then
        configure_python_tests
    fi
    
    if [ "$FRAMEWORK" = "all" ] || [ "$FRAMEWORK" = "jest" ]; then
        configure_nodejs_tests
    fi
    
    # Run tests
    if [ "$FRAMEWORK" = "all" ] || [ "$FRAMEWORK" = "pytest" ]; then
        run_python_tests
    fi
    
    if [ "$FRAMEWORK" = "all" ] || [ "$FRAMEWORK" = "jest" ]; then
        run_nodejs_tests
    fi
    
    # Restore files
    restore_files
    
    echo -e "${GREEN}✅ Test run completed!${NC}"
}

# Trap to restore files on exit
trap restore_files EXIT

# Run main function
main


