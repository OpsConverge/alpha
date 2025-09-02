# Unit Testing CI/CD Pipeline

This repository contains a comprehensive CI/CD pipeline focused on unit testing with three popular testing frameworks:

- **JUnit** (Java) - For Java applications
- **pytest** (Python) - For Python applications  
- **Jest** (JavaScript/Node.js) - For JavaScript/Node.js applications

## 🏗️ Project Structure

```
alpha/
├── .github/
│   └── workflows/
│       └── unit-test-pipeline.yml    # Main CI/CD pipeline
├── java-service/                     # Java application with JUnit tests
│   ├── src/
│   │   └── main/java/com/example/
│   │       ├── CalculatorService.java
│   │       └── StringService.java
│   ├── src/test/java/com/example/unit/
│   │   ├── CalculatorServiceTest.java
│   │   └── StringServiceTest.java
│   └── pom.xml
├── python-service/                   # Python application with pytest tests
│   ├── src/
│   │   ├── calculator_service.py
│   │   └── string_service.py
│   ├── tests/unit/
│   │   ├── test_calculator_service.py
│   │   └── test_string_service.py
│   └── requirements.txt
├── node-service/                     # Node.js application with Jest tests
│   ├── src/
│   │   ├── calculatorService.js
│   │   └── stringService.js
│   ├── tests/unit/
│   │   ├── calculatorService.test.js
│   │   └── stringService.test.js
│   └── package.json
└── README.md
```

## 🚀 CI/CD Pipeline Features

### GitHub Actions Workflow

The pipeline (`unit-test-pipeline.yml`) includes:

- **Multi-framework Support**: Runs tests for JUnit, pytest, and Jest
- **Parallel Execution**: All test frameworks run simultaneously
- **Caching**: Maven, pip, and npm dependencies are cached for faster builds
- **Artifact Upload**: Test results and coverage reports are preserved
- **Quality Gates**: Ensures all tests pass before proceeding
- **Manual Triggering**: Can run specific framework tests or all tests
- **Comprehensive Reporting**: Detailed test summaries and coverage reports

### Pipeline Jobs

1. **JUnit Unit Tests** (Java)
   - Uses Java 17 with Maven
   - Runs unit tests with JUnit 5
   - Generates JaCoCo coverage reports
   - Uploads test results and coverage artifacts

2. **pytest Unit Tests** (Python)
   - Uses Python 3.11
   - Runs unit tests with pytest
   - Generates coverage reports with pytest-cov
   - Uploads test results and coverage artifacts

3. **Jest Unit Tests** (JavaScript/Node.js)
   - Uses Node.js 18
   - Runs unit tests with Jest
   - Generates coverage reports
   - Uploads test results and coverage artifacts

4. **Unit Test Summary**
   - Aggregates results from all test frameworks
   - Provides comprehensive test summary
   - Links to coverage reports

5. **Quality Gates**
   - Ensures all tests pass
   - Provides clear pass/fail status
   - Blocks deployment if tests fail

## 🧪 Sample Applications

### Java Service (JUnit)

**CalculatorService**: Mathematical operations including:
- Basic arithmetic (add, subtract, multiply, divide)
- Advanced math (power, square root, factorial)
- Array operations (average, max, min)
- Number theory (GCD, LCM, prime checking)

**StringService**: String manipulation operations including:
- Text reversal and palindrome detection
- Vowel counting and title case conversion
- Duplicate removal and longest word finding
- Anagram detection and word counting

### Python Service (pytest)

**CalculatorService**: Similar mathematical operations with Python implementation
**StringService**: String operations with additional features:
- Email validation
- Number extraction
- Special character removal

### Node.js Service (Jest)

**CalculatorService**: JavaScript implementation of mathematical operations
**StringService**: String operations with comprehensive error handling

## 🛠️ Running Tests Locally

### Java (JUnit)

```bash
cd java-service
mvn clean test
```

### Python (pytest)

```bash
cd python-service
pip install -r requirements.txt
pytest tests/unit/ -v --cov=src
```

### Node.js (Jest)

```bash
cd node-service
npm install
npm run test:unit
```

## 📊 Test Coverage

Each framework includes comprehensive test coverage:

- **Unit Tests**: Individual method testing
- **Parameterized Tests**: Multiple input combinations
- **Edge Cases**: Null/undefined handling, empty inputs
- **Error Conditions**: Exception testing
- **Boundary Testing**: Edge values and limits

### Test Statistics

- **JUnit**: 50+ test methods with parameterized testing
- **pytest**: 60+ test methods with fixtures and parametrization
- **Jest**: 70+ test cases with comprehensive assertions

## 🔧 Configuration

### Environment Variables

```yaml
NODE_VERSION: '18'
PYTHON_VERSION: '3.11'
JAVA_VERSION: '17'
```

### Dependencies

**Java (Maven)**:
- Spring Boot 3.3.2
- JUnit 5 with parameterized testing
- JaCoCo for coverage

**Python (pip)**:
- pytest 7.4.3
- pytest-cov for coverage
- pytest-html for reports

**Node.js (npm)**:
- Jest 29.7.0
- Coverage reporting enabled

## 🚦 Pipeline Triggers

The pipeline runs on:
- **Push** to main/develop branches
- **Pull Requests** to main/develop branches
- **Manual Dispatch** with framework selection

### Manual Trigger Options

- `all`: Run all test frameworks
- `junit`: Run only JUnit tests
- `pytest`: Run only pytest tests
- `jest`: Run only Jest tests

## 📈 Artifacts

The pipeline generates and preserves:

- **Test Results**: XML/JSON reports from each framework
- **Coverage Reports**: HTML coverage reports
- **Build Logs**: Detailed execution logs
- **Test Summaries**: Aggregated test statistics

## 🎯 Best Practices Implemented

1. **Test Organization**: Clear separation of test types
2. **Naming Conventions**: Descriptive test names and descriptions
3. **Parameterized Testing**: Efficient testing of multiple scenarios
4. **Error Handling**: Comprehensive exception testing
5. **Edge Case Coverage**: Null, empty, and boundary value testing
6. **Documentation**: Detailed test documentation and comments
7. **CI/CD Integration**: Automated testing with quality gates

## 🔍 Monitoring and Reporting

- **Real-time Status**: Live pipeline execution status
- **Test Results**: Detailed pass/fail information
- **Coverage Metrics**: Code coverage percentages
- **Performance Data**: Test execution times
- **Quality Metrics**: Overall test quality indicators

## 🚀 Getting Started

1. **Fork/Clone** this repository
2. **Push** to trigger the pipeline
3. **Review** test results and coverage reports
4. **Customize** for your specific needs

## 📝 Contributing

1. Add new test cases to existing services
2. Implement additional service classes
3. Enhance pipeline configuration
4. Improve documentation and examples

## 📄 License

MIT License - feel free to use this setup for your own projects!

---

**Happy Testing! 🧪✨**


