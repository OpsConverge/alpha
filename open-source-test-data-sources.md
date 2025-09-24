# Open Source Test Data Sources for Parser Testing

## Overview

This document lists open source repositories and datasets that provide excellent test result data for validating and demonstrating your parser system with real-world CI/CD pipeline outputs.

## 🎯 **Recommended Open Source Projects**

### **1. Large Java Projects (JUnit XML)**

#### **Spring Boot Projects**
- **Repository**: `spring-projects/spring-boot`
- **GitHub**: https://github.com/spring-projects/spring-boot
- **Test Data**: Comprehensive JUnit XML reports from Maven/Gradle
- **Why Good**: 
  - 10,000+ test cases across multiple modules
  - Complex test hierarchies and failure scenarios
  - Real-world enterprise test patterns
  - Multiple test types (unit, integration, web)

#### **Apache Projects**
- **Apache Commons**: https://github.com/apache/commons-lang
- **Apache Kafka**: https://github.com/apache/kafka  
- **Apache Maven**: https://github.com/apache/maven
- **Why Good**:
  - Mature, well-tested codebases
  - Comprehensive JUnit reports
  - Various failure patterns and edge cases

#### **Popular Java Libraries**
- **Jackson JSON**: https://github.com/FasterXML/jackson-core
- **Hibernate ORM**: https://github.com/hibernate/hibernate-orm
- **JUnit 5**: https://github.com/junit-team/junit5

### **2. Python Projects (Pytest JSON)**

#### **Major Python Frameworks**
- **Django**: https://github.com/django/django
- **Flask**: https://github.com/pallets/flask
- **FastAPI**: https://github.com/tiangolo/fastapi
- **Why Good**:
  - Extensive pytest test suites
  - Complex test scenarios
  - Real-world failure patterns

#### **Data Science Libraries**
- **Pandas**: https://github.com/pandas-dev/pandas
- **NumPy**: https://github.com/numpy/numpy
- **Scikit-learn**: https://github.com/scikit-learn/scikit-learn
- **Why Good**:
  - Large test suites (10,000+ tests)
  - Numerical testing edge cases
  - Performance and regression tests

### **3. JavaScript/TypeScript Projects (Jest/Mocha)**

#### **Popular Frontend Frameworks**
- **React**: https://github.com/facebook/react
- **Vue.js**: https://github.com/vuejs/vue
- **Angular**: https://github.com/angular/angular
- **Why Good**:
  - Comprehensive Jest test suites
  - Component testing patterns
  - Snapshot testing examples

#### **Node.js Libraries**
- **Express.js**: https://github.com/expressjs/express
- **Lodash**: https://github.com/lodash/lodash
- **Moment.js**: https://github.com/moment/moment
- **Why Good**:
  - Mocha/Jest test combinations
  - API testing patterns
  - Cross-platform testing

### **4. Go Projects (Go Test JSON)**

#### **Cloud Native Projects**
- **Kubernetes**: https://github.com/kubernetes/kubernetes
- **Docker**: https://github.com/moby/moby
- **Prometheus**: https://github.com/prometheus/prometheus
- **Why Good**:
  - Extensive Go test suites
  - Microservice testing patterns
  - Performance benchmarks

#### **Popular Go Libraries**
- **Gin Web Framework**: https://github.com/gin-gonic/gin
- **GORM**: https://github.com/go-gorm/gorm
- **Cobra CLI**: https://github.com/spf13/cobra

### **5. .NET Projects (xUnit XML)**

#### **Microsoft Open Source**
- **.NET Core**: https://github.com/dotnet/core
- **ASP.NET Core**: https://github.com/dotnet/aspnetcore
- **Entity Framework**: https://github.com/dotnet/efcore
- **Why Good**:
  - Comprehensive xUnit test suites
  - Enterprise-grade testing patterns
  - Complex integration tests

### **6. Ruby Projects (RSpec JSON)**

#### **Popular Ruby Frameworks**
- **Ruby on Rails**: https://github.com/rails/rails
- **Sinatra**: https://github.com/sinatra/sinatra
- **Jekyll**: https://github.com/jekyll/jekyll
- **Why Good**:
  - Extensive RSpec test suites
  - Behavior-driven development patterns
  - Real-world Ruby testing

## 🔄 **CI/CD Pipeline Examples**

### **GitHub Actions Workflows with Rich Test Data**

#### **Multi-Language Projects**
```yaml
# Example from large projects
name: CI
on: [push, pull_request]
jobs:
  test-java:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-java@v3
      - run: mvn test
      - uses: actions/upload-artifact@v3
        with:
          name: junit-results
          path: target/surefire-reports/*.xml

  test-python:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v3
      - run: pytest --json-report --json-report-file=pytest-results.json
      - uses: actions/upload-artifact@v3
        with:
          name: pytest-results
          path: pytest-results.json

  test-node:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
      - run: npm test -- --json --outputFile=jest-results.json
      - uses: actions/upload-artifact@v3
        with:
          name: jest-results
          path: jest-results.json
```

### **Jenkins Pipeline Examples**
- **Jenkins Pipeline Library**: https://github.com/jenkinsci/pipeline-examples
- **Jenkins Shared Libraries**: https://github.com/jenkinsci/workflow-cps-global-lib-plugin

## 📊 **Test Data Characteristics**

### **High-Quality Test Data Sources**

| Project Type | Test Count | Frameworks | Complexity | Failure Rate |
|--------------|------------|------------|------------|--------------|
| **Spring Boot** | 10,000+ | JUnit 5 | High | 5-10% |
| **Django** | 8,000+ | Pytest | High | 3-8% |
| **React** | 5,000+ | Jest | Medium | 2-5% |
| **Kubernetes** | 15,000+ | Go Test | Very High | 5-15% |
| **.NET Core** | 12,000+ | xUnit | High | 4-9% |
| **Ruby on Rails** | 6,000+ | RSpec | Medium | 3-7% |

### **Diverse Test Scenarios**

1. **Unit Tests** - Fast, isolated component tests
2. **Integration Tests** - Database, API, service integration
3. **E2E Tests** - Full application workflow testing
4. **Performance Tests** - Load, stress, benchmark testing
5. **Security Tests** - Vulnerability and penetration testing

## 🚀 **Implementation Strategy**

### **Phase 1: Connect to Popular Repositories**

1. **Add GitHub Integration**
   ```javascript
   // Connect to public repositories
   const testRepos = [
     'spring-projects/spring-boot',
     'django/django', 
     'facebook/react',
     'kubernetes/kubernetes'
   ];
   ```

2. **Fetch Recent Workflow Runs**
   ```javascript
   // Get latest workflow runs with test results
   const runs = await githubService.getWorkflowRuns(owner, repo, token, {
     status: 'completed',
     per_page: 50
   });
   ```

3. **Download and Parse Test Artifacts**
   ```javascript
   // Your existing sync logic will handle this
   await testSyncService.syncRepositoryTests(teamId, repoFullName);
   ```

### **Phase 2: Create Demo Dataset**

Create a curated demo dataset with representative test results:

```python
# Demo data generator
demo_repos = {
    'enterprise-java': {
        'framework': 'junit',
        'test_count': 2500,
        'failure_rate': 0.08,
        'complexity': 'high'
    },
    'python-microservice': {
        'framework': 'pytest', 
        'test_count': 1200,
        'failure_rate': 0.05,
        'complexity': 'medium'
    },
    'react-frontend': {
        'framework': 'jest',
        'test_count': 800,
        'failure_rate': 0.03,
        'complexity': 'medium'
    }
}
```

### **Phase 3: Dashboard Integration**

Display parsed results with rich analytics:

```javascript
// Dashboard components
const TestResultsDashboard = () => {
  const [testData, setTestData] = useState([]);
  
  // Fetch parsed test results
  useEffect(() => {
    fetchTestResults().then(data => {
      setTestData(data.nextjs_format); // Use Next.js optimized format
    });
  }, []);
  
  return (
    <div>
      <TestSummaryCards data={testData.summary} />
      <FrameworkBreakdown frameworks={testData.frameworks} />
      <TrendAnalysis trends={testData.trends} />
      <FailureAnalysis failures={testData.failures} />
    </div>
  );
};
```

## 📈 **Specific Repository Recommendations**

### **For Comprehensive Testing**

1. **Spring Pet Clinic** 
   - Repository: https://github.com/spring-projects/spring-petclinic
   - Why: Simple, well-documented, comprehensive test suite
   - Test Data: JUnit XML with integration tests

2. **Django REST Framework**
   - Repository: https://github.com/encode/django-rest-framework
   - Why: Excellent pytest coverage, API testing patterns
   - Test Data: Pytest JSON with detailed test metadata

3. **Create React App**
   - Repository: https://github.com/facebook/create-react-app
   - Why: Standard Jest setup, component testing
   - Test Data: Jest JSON with snapshot tests

4. **Gin Web Framework (Go)**
   - Repository: https://github.com/gin-gonic/gin
   - Why: Clean Go testing patterns, benchmarks
   - Test Data: Go test JSON with performance tests

### **For Edge Case Testing**

1. **Mockito** (Java)
   - Repository: https://github.com/mockito/mockito
   - Why: Complex mocking scenarios, edge cases
   - Test Data: JUnit XML with unusual test patterns

2. **Requests** (Python)
   - Repository: https://github.com/psf/requests
   - Why: HTTP testing, network failure scenarios
   - Test Data: Pytest JSON with timeout/network tests

3. **Lodash** (JavaScript)
   - Repository: https://github.com/lodash/lodash
   - Why: Utility function testing, edge cases
   - Test Data: Jest JSON with comprehensive coverage

## 🛠️ **Implementation Code**

Let me create a script to automatically fetch test data from these repositories:

```python
# Repository test data fetcher
class GitHubTestDataFetcher:
    def __init__(self, github_token):
        self.token = github_token
        self.repos = [
            'spring-projects/spring-petclinic',
            'encode/django-rest-framework', 
            'facebook/create-react-app',
            'gin-gonic/gin'
        ]
    
    async def fetch_test_data(self, repo_name):
        # Get recent workflow runs
        runs = await self.get_workflow_runs(repo_name)
        
        # Download test artifacts
        for run in runs[:5]:  # Last 5 runs
            artifacts = await self.get_artifacts(repo_name, run.id)
            for artifact in artifacts:
                if self.is_test_artifact(artifact.name):
                    data = await self.download_artifact(repo_name, artifact.id)
                    yield {
                        'repo': repo_name,
                        'run_id': run.id,
                        'artifact': artifact.name,
                        'data': data
                    }
```

## 🎯 **Recommended Approach**

1. **Start with Spring Pet Clinic** - Simple, reliable test data
2. **Add Django REST Framework** - Python/Pytest examples  
3. **Include Create React App** - JavaScript/Jest patterns
4. **Test with Kubernetes** - Large-scale, complex scenarios

These repositories will provide **real-world test data** that covers:
- ✅ **Multiple frameworks** (JUnit, Pytest, Jest, Go Test, etc.)
- ✅ **Various test types** (unit, integration, E2E)
- ✅ **Realistic failure patterns** 
- ✅ **Large-scale test suites** (1000+ tests)
- ✅ **Edge cases and complexities**

This will give you a robust dataset to demonstrate your parser's capabilities with real CI/CD pipeline data!
