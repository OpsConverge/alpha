# Enhanced CI/CD Pipeline with Manual Test Triggers

This enhanced CI/CD pipeline allows you to manually trigger different test scenarios to simulate various real-world testing situations.

## 🎛️ Workflow Dispatch Options

When you manually trigger the pipeline from GitHub Actions, you'll see these options:

### 1. Framework Selection
- **all** - Run all frameworks (JUnit, pytest, Jest)
- **junit** - Run only Java/JUnit tests
- **pytest** - Run only Python/pytest tests
- **jest** - Run only Node.js/Jest tests

### 2. Test Execution Mode
- **normal** - Run tests as they are (default behavior)
- **force_pass** - Comment out failing tests to force all tests to pass
- **force_fail** - Modify test assertions to make all tests fail
- **mixed_results** - Some tests pass, some fail (simulates real-world scenarios)

### 3. Include Failing Tests
- **true** - Include intentionally failing tests (default)
- **false** - Exclude intentionally failing tests

## 🚀 How to Use

### From GitHub Actions UI

1. Go to your repository on GitHub
2. Navigate to **Actions** tab
3. Select **Unit Test Pipeline** workflow
4. Click **Run workflow** button
5. Configure your options:
   - **Framework**: Choose which test framework(s) to run
   - **Test execution mode**: Choose how tests should behave
   - **Include failing tests**: Whether to include intentionally failing tests
6. Click **Run workflow**

### Example Scenarios

#### Scenario 1: All Tests Pass
- **Framework**: all
- **Test execution mode**: force_pass
- **Include failing tests**: false
- **Result**: All tests will pass, pipeline succeeds

#### Scenario 2: All Tests Fail
- **Framework**: all
- **Test execution mode**: force_fail
- **Include failing tests**: true
- **Result**: All tests will fail, pipeline fails

#### Scenario 3: Mixed Results (Realistic)
- **Framework**: all
- **Test execution mode**: mixed_results
- **Include failing tests**: true
- **Result**: Some tests pass, some fail, pipeline fails

#### Scenario 4: Python Tests Only - Force Pass
- **Framework**: pytest
- **Test execution mode**: force_pass
- **Include failing tests**: false
- **Result**: Only Python tests run and all pass

## 🧪 Local Testing

Before pushing to GitHub, you can test different scenarios locally using the provided scripts.

### Windows Users
```bash
# Test all frameworks with force pass mode
scripts\test-runner.bat -f all -m force_pass

# Test only Python with mixed results
scripts\test-runner.bat -f pytest -m mixed_results

# Test only Node.js with force fail
scripts\test-runner.bat -f jest -m force_fail

# Exclude failing tests
scripts\test-runner.bat -f all -m normal -i false
```

### Linux/Mac Users
```bash
# Make script executable (first time only)
chmod +x scripts/test-runner.sh

# Test all frameworks with force pass mode
./scripts/test-runner.sh -f all -m force_pass

# Test only Python with mixed results
./scripts/test-runner.sh -f pytest -m mixed_results

# Test only Node.js with force fail
./scripts/test-runner.sh -f jest -m force_fail

# Exclude failing tests
./scripts/test-runner.sh -f all -m normal -i false
```

## 📊 Test Results and Artifacts

The pipeline generates comprehensive reports and artifacts:

### Test Results
- **JUnit**: Surefire reports in `java-service/target/surefire-reports/`
- **pytest**: JUnit XML reports and HTML coverage
- **Jest**: Coverage reports and test results

### Coverage Reports
- **JUnit**: JaCoCo coverage reports
- **pytest**: HTML and XML coverage reports
- **Jest**: Built-in coverage reports

### Quality Gates
The pipeline includes quality gates that:
- ✅ Pass when all tests succeed
- ❌ Fail when any tests fail
- 📊 Generate summary reports
- 🎯 Enforce test pass criteria

## 🔧 Pipeline Features

### Parallel Execution
- All test frameworks run in parallel
- Faster execution times
- Independent failure handling

### Caching
- Maven dependencies cached
- pip dependencies cached
- npm dependencies cached
- Faster subsequent runs

### Artifact Management
- Test results stored as artifacts
- Coverage reports preserved
- 30-day retention period
- Easy download and analysis

### Conditional Execution
- Tests only run for selected frameworks
- Configurable test modes
- Flexible test inclusion/exclusion

## 🎯 Use Cases

### 1. Development Testing
- **Mode**: normal
- **Purpose**: Verify current code state
- **Expected**: Some tests may fail (realistic)

### 2. Pre-deployment Validation
- **Mode**: force_pass
- **Purpose**: Ensure all tests pass before deployment
- **Expected**: All tests pass, pipeline succeeds

### 3. Failure Simulation
- **Mode**: force_fail
- **Purpose**: Test failure handling and notifications
- **Expected**: All tests fail, pipeline fails

### 4. Partial Testing
- **Mode**: mixed_results
- **Purpose**: Test specific frameworks or scenarios
- **Expected**: Mixed results, pipeline fails

### 5. Framework-Specific Testing
- **Mode**: normal
- **Purpose**: Test only specific frameworks
- **Expected**: Varies based on framework state

## 📈 Monitoring and Notifications

### GitHub Actions Summary
The pipeline provides detailed summaries including:
- Test configuration used
- Framework-specific results
- Coverage information
- Quality gate status

### Artifact Downloads
All test results and coverage reports are available as downloadable artifacts:
- Navigate to the workflow run
- Click on **Artifacts** section
- Download relevant reports

### Integration Possibilities
The pipeline can be extended to:
- Send notifications to Slack/Teams
- Update external monitoring systems
- Trigger downstream deployments
- Generate custom reports

## 🛠️ Customization

### Adding New Test Modes
1. Modify the workflow dispatch inputs
2. Add configuration logic in test jobs
3. Update test files accordingly

### Adding New Frameworks
1. Create new test job
2. Add framework selection logic
3. Include in parallel execution
4. Update summary generation

### Modifying Test Behavior
1. Edit the sed commands in configuration steps
2. Adjust test file modifications
3. Update local test scripts

## 🔍 Troubleshooting

### Common Issues

#### Tests Not Running
- Check framework selection
- Verify test file paths
- Ensure dependencies are installed

#### Unexpected Test Results
- Verify test mode configuration
- Check test file modifications
- Review test assertions

#### Pipeline Failures
- Check quality gate configuration
- Review test job dependencies
- Verify artifact uploads

### Debug Steps
1. Check workflow run logs
2. Review test configuration output
3. Download and examine artifacts
4. Test locally with scripts

## 📚 Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [JUnit 5 User Guide](https://junit.org/junit5/docs/current/user-guide/)
- [pytest Documentation](https://docs.pytest.org/)
- [Jest Documentation](https://jestjs.io/docs/getting-started)

---

**Happy Testing! 🎉**

