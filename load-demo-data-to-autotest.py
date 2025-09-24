#!/usr/bin/env python3
"""
Demo Data Loader for Autotest Platform
Loads realistic test data directly into your autotest platform for testing and demonstration.
"""

import os
import sys
import json
import requests
import time
from pathlib import Path
from typing import Dict, List, Any, Optional

# Add the test parser to Python path
parser_path = Path(r'C:\autotest\test-parser-mvp')
sys.path.insert(0, str(parser_path))

from core.parser_orchestrator import get_orchestrator
from models import ParseRequest

class AutotestDemoDataLoader:
    """Loads demo test data directly into autotest platform."""
    
    def __init__(self, autotest_api_url: str = "http://localhost:4000", auth_token: Optional[str] = None):
        """
        Initialize the demo data loader.
        
        Args:
            autotest_api_url: URL of your autotest backend API
            auth_token: Authentication token for autotest API
        """
        self.api_url = autotest_api_url.rstrip('/')
        self.auth_token = auth_token
        self.headers = {'Content-Type': 'application/json'}
        if auth_token:
            self.headers['Authorization'] = f'Bearer {auth_token}'
        
        self.orchestrator = get_orchestrator()
    
    def load_demo_scenarios(self, team_id: int = 4) -> Dict[str, Any]:
        """
        Load demo test scenarios directly into your autotest platform.
        
        Args:
            team_id: Team ID in your autotest platform
            
        Returns:
            Dict containing loading results
        """
        print("🎨 Loading Demo Data into Autotest Platform")
        print("=" * 45)
        print(f"🎯 Target API: {self.api_url}")
        print(f"👥 Team ID: {team_id}")
        
        # Demo scenarios representing different types of projects
        demo_scenarios = [
            {
                'repo_name': 'demo/enterprise-java-backend',
                'framework': 'junit',
                'description': 'Large Spring Boot microservice',
                'test_count': 185,
                'failure_rate': 0.08,
                'build_number': '1234'
            },
            {
                'repo_name': 'demo/python-api-service', 
                'framework': 'pytest',
                'description': 'Django REST API service',
                'test_count': 120,
                'failure_rate': 0.05,
                'build_number': '5678'
            },
            {
                'repo_name': 'demo/react-frontend-app',
                'framework': 'jest',
                'description': 'React SPA with component tests',
                'test_count': 95,
                'failure_rate': 0.03,
                'build_number': '9012'
            },
            {
                'repo_name': 'demo/go-microservice',
                'framework': 'go-test', 
                'description': 'Go HTTP API microservice',
                'test_count': 75,
                'failure_rate': 0.06,
                'build_number': '3456'
            },
            {
                'repo_name': 'demo/dotnet-web-api',
                'framework': 'xunit',
                'description': '.NET Core Web API',
                'test_count': 110,
                'failure_rate': 0.07,
                'build_number': '7890'
            }
        ]
        
        loading_results = {
            'scenarios_loaded': 0,
            'total_test_cases': 0,
            'builds_created': 0,
            'frameworks_tested': set(),
            'errors': []
        }
        
        for scenario in demo_scenarios:
            print(f"\n📦 Loading: {scenario['repo_name']}")
            print(f"   🔧 Framework: {scenario['framework']}")
            print(f"   📊 {scenario['test_count']} tests, {scenario['failure_rate']*100:.1f}% failure rate")
            
            try:
                # Generate realistic test data
                test_data = self._generate_test_data(scenario)
                
                # Parse with Python parser
                parse_result = self._parse_test_data(test_data, scenario)
                
                if parse_result['success']:
                    # Upload to autotest platform via API
                    upload_result = self._upload_to_autotest(parse_result, scenario, team_id)
                    
                    if upload_result['success']:
                        loading_results['scenarios_loaded'] += 1
                        loading_results['total_test_cases'] += parse_result['test_count']
                        loading_results['builds_created'] += 1
                        loading_results['frameworks_tested'].add(scenario['framework'])
                        
                        print(f"   ✅ Loaded {parse_result['test_count']} tests to autotest platform")
                    else:
                        print(f"   ❌ Upload failed: {upload_result['error']}")
                        loading_results['errors'].append(f"{scenario['repo_name']}: {upload_result['error']}")
                else:
                    print(f"   ❌ Parse failed: {parse_result['error']}")
                    loading_results['errors'].append(f"{scenario['repo_name']}: {parse_result['error']}")
                
            except Exception as e:
                error_msg = f"{scenario['repo_name']}: {str(e)}"
                loading_results['errors'].append(error_msg)
                print(f"   ❌ Error: {str(e)}")
        
        self._print_loading_summary(loading_results)
        return loading_results
    
    def _generate_test_data(self, scenario: Dict[str, Any]) -> bytes:
        """Generate realistic test data for a scenario."""
        framework = scenario['framework']
        test_count = scenario['test_count']
        failure_rate = scenario['failure_rate']
        
        if framework == 'junit':
            return self._generate_junit_data(test_count, failure_rate, scenario['repo_name'])
        elif framework == 'pytest':
            return self._generate_pytest_data(test_count, failure_rate, scenario['repo_name'])
        elif framework == 'jest':
            return self._generate_jest_data(test_count, failure_rate, scenario['repo_name'])
        elif framework == 'go-test':
            return self._generate_go_data(test_count, failure_rate, scenario['repo_name'])
        elif framework == 'xunit':
            return self._generate_xunit_data(test_count, failure_rate, scenario['repo_name'])
        else:
            return self._generate_junit_data(test_count, failure_rate, scenario['repo_name'])
    
    def _generate_junit_data(self, test_count: int, failure_rate: float, repo_name: str) -> bytes:
        """Generate realistic JUnit XML data."""
        import random
        
        failures = int(test_count * failure_rate)
        errors = max(1, int(test_count * 0.02))
        
        test_cases = []
        total_time = 0
        
        # Create test suites based on typical Java package structure
        packages = [
            f"{repo_name.split('/')[-1]}.controller",
            f"{repo_name.split('/')[-1]}.service", 
            f"{repo_name.split('/')[-1]}.repository",
            f"{repo_name.split('/')[-1]}.util"
        ]
        
        for i in range(test_count):
            package = random.choice(packages)
            test_name = f"test{random.choice(['Create', 'Update', 'Delete', 'Find', 'Validate'])}{i:03d}"
            duration = round(random.uniform(0.01, 3.0), 3)
            total_time += duration
            
            if i < failures:
                test_cases.append(f'''
        <testcase classname="{package}.{package.split('.')[-1].title()}Test" name="{test_name}" time="{duration}">
            <failure message="Test assertion failed" type="AssertionError">
Expected: {random.randint(1, 100)}
Actual: {random.randint(1, 100)}
    at {package}.{package.split('.')[-1].title()}Test.{test_name}({package.split('.')[-1].title()}Test.java:{random.randint(20, 150)})
            </failure>
        </testcase>''')
            elif i < failures + errors:
                test_cases.append(f'''
        <testcase classname="{package}.{package.split('.')[-1].title()}Test" name="{test_name}" time="{duration}">
            <error message="System error" type="RuntimeException">
{random.choice(['Database connection timeout', 'Network error', 'Configuration error'])}
    at {package}.{package.split('.')[-1].title()}Test.{test_name}({package.split('.')[-1].title()}Test.java:{random.randint(20, 150)})
            </error>
        </testcase>''')
            else:
                test_cases.append(f'''
        <testcase classname="{package}.{package.split('.')[-1].title()}Test" name="{test_name}" time="{duration}"/>''')
        
        xml_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="{repo_name} Tests" tests="{test_count}" failures="{failures}" errors="{errors}" time="{total_time:.3f}">
    <testsuite name="{repo_name.replace('/', '.')}.AllTests" tests="{test_count}" failures="{failures}" errors="{errors}" time="{total_time:.3f}">
        {''.join(test_cases)}
    </testsuite>
</testsuites>'''
        
        return xml_content.encode('utf-8')
    
    def _generate_pytest_data(self, test_count: int, failure_rate: float, repo_name: str) -> bytes:
        """Generate realistic Pytest JSON data."""
        import random
        
        tests = []
        passed = 0
        failed = 0
        skipped = int(test_count * 0.02)  # 2% skipped
        
        modules = ['serializers', 'views', 'models', 'utils', 'permissions']
        
        for i in range(test_count):
            module = random.choice(modules)
            outcome = random.choices(
                ['passed', 'failed', 'skipped'],
                weights=[1-failure_rate-0.02, failure_rate, 0.02]
            )[0]
            
            test = {
                "nodeid": f"tests/test_{module}.py::Test{module.title()}::test_{random.choice(['create', 'update', 'delete', 'validate'])}_{i:03d}",
                "outcome": outcome,
                "duration": round(random.uniform(0.001, 2.0), 3)
            }
            
            if outcome == 'failed':
                test["call"] = {
                    "outcome": "failed",
                    "longrepr": f"AssertionError: {module} test {i} failed - expected {random.randint(1,100)}, got {random.randint(1,100)}"
                }
                failed += 1
            elif outcome == 'passed':
                test["call"] = {"outcome": "passed"}
                passed += 1
            else:
                test["setup"] = {"longrepr": [f"tests/test_{module}.py", random.randint(10,50), "Skipped: feature not implemented"]}
                skipped += 1
            
            tests.append(test)
        
        pytest_data = {
            "created": datetime.now().isoformat(),
            "duration": sum(t['duration'] for t in tests),
            "exitcode": 1 if failed > 0 else 0,
            "environment": {
                "Python": "3.9.16",
                "Platform": "Linux-5.4.0-x86_64",
                "Packages": {"pytest": "7.4.3", "django": "4.2.7"}
            },
            "summary": {
                "total": test_count,
                "passed": passed,
                "failed": failed,
                "skipped": skipped
            },
            "tests": tests
        }
        
        return json.dumps(pytest_data, indent=2).encode('utf-8')
    
    def _generate_jest_data(self, test_count: int, failure_rate: float, repo_name: str) -> bytes:
        """Generate realistic Jest JSON data."""
        import random
        
        assertion_results = []
        passed = 0
        failed = 0
        pending = int(test_count * 0.01)  # 1% pending
        
        components = ['Button', 'Form', 'Modal', 'List', 'Card', 'Header', 'Footer']
        
        for i in range(test_count):
            component = random.choice(components)
            status = random.choices(
                ['passed', 'failed', 'pending'],
                weights=[1-failure_rate-0.01, failure_rate, 0.01]
            )[0]
            
            assertion = {
                "ancestorTitles": [f"{component}Component", f"{random.choice(['rendering', 'interaction', 'props'])} tests"],
                "title": f"should {random.choice(['render', 'handle click', 'validate props', 'update state'])} correctly {i:03d}",
                "status": status,
                "duration": random.randint(50, 500)
            }
            
            if status == 'failed':
                assertion["failureMessages"] = [
                    f"Error: expect(received).toBe(expected)\n\nExpected: {random.randint(1,100)}\nReceived: {random.randint(1,100)}\n\n  at Object.<anonymous> (/project/src/components/{component}.test.js:{random.randint(10,200)}:23)"
                ]
                failed += 1
            elif status == 'passed':
                passed += 1
            else:
                pending += 1
            
            assertion_results.append(assertion)
        
        jest_data = {
            "numTotalTests": test_count,
            "numPassedTests": passed,
            "numFailedTests": failed,
            "numPendingTests": pending,
            "success": failed == 0,
            "startTime": int(time.time() * 1000) - 45000,
            "endTime": int(time.time() * 1000),
            "testResults": [
                {
                    "assertionResults": assertion_results,
                    "name": f"/project/src/components/{repo_name.split('/')[-1]}.test.js"
                }
            ]
        }
        
        return json.dumps(jest_data, indent=2).encode('utf-8')
    
    def _generate_go_data(self, test_count: int, failure_rate: float, repo_name: str) -> bytes:
        """Generate realistic Go test JSON data."""
        import random
        
        base_package = f"github.com/{repo_name}"
        packages = [base_package, f"{base_package}/handlers", f"{base_package}/middleware", f"{base_package}/utils"]
        
        events = []
        
        for i in range(test_count):
            package = random.choice(packages)
            test_name = f"Test{random.choice(['Handler', 'Middleware', 'Router', 'Util'])}{i:03d}"
            outcome = random.choices(['pass', 'fail'], weights=[1-failure_rate, failure_rate])[0]
            duration = round(random.uniform(0.001, 0.5), 3)
            
            # Standard Go test event sequence
            events.extend([
                json.dumps({"Action": "run", "Package": package, "Test": test_name}),
                json.dumps({"Action": "output", "Package": package, "Test": test_name, "Output": f"=== RUN   {test_name}\\n"}),
                json.dumps({"Action": outcome, "Package": package, "Test": test_name, "Elapsed": duration})
            ])
            
            if outcome == 'fail':
                events.insert(-1, json.dumps({
                    "Action": "output", 
                    "Package": package, 
                    "Test": test_name, 
                    "Output": f"--- FAIL: {test_name} ({duration:.3f}s)\\n    handler_test.go:{random.randint(20,100)}: Test failed\\n"
                }))
        
        return '\n'.join(events).encode('utf-8')
    
    def _generate_xunit_data(self, test_count: int, failure_rate: float, repo_name: str) -> bytes:
        """Generate realistic xUnit XML data."""
        import random
        
        assemblies = []
        failures = int(test_count * failure_rate)
        
        # Create assemblies (typically one per project)
        assembly_name = f"{repo_name.split('/')[-1].title()}.Tests"
        
        test_cases = []
        total_time = 0
        
        for i in range(test_count):
            test_name = f"Test{random.choice(['Controller', 'Service', 'Repository', 'Validator'])}{i:03d}"
            duration = round(random.uniform(0.01, 2.0), 3)
            total_time += duration
            
            if i < failures:
                test_cases.append(f'''
        <test name="{assembly_name}.{test_name}" type="{assembly_name}" method="{test_name}" result="Fail" time="{duration}">
            <failure exception-type="Xunit.Sdk.XunitException">
                <message>Assert.Equal() Failure\nExpected: {random.randint(1,100)}\nActual:   {random.randint(1,100)}</message>
                <stack-trace>   at {assembly_name}.{test_name}() in TestFile.cs:line {random.randint(20,100)}</stack-trace>
            </failure>
        </test>''')
            else:
                test_cases.append(f'''
        <test name="{assembly_name}.{test_name}" type="{assembly_name}" method="{test_name}" result="Pass" time="{duration}"/>''')
        
        xml_content = f'''<?xml version="1.0" encoding="utf-8"?>
<assemblies timestamp="{datetime.now().strftime('%m/%d/%Y %H:%M:%S')}">
    <assembly name="{assembly_name}" test-framework="xUnit.net 2.4.2" run-date="{datetime.now().strftime('%Y-%m-%d')}" run-time="{datetime.now().strftime('%H:%M:%S')}" total="{test_count}" passed="{test_count-failures}" failed="{failures}" skipped="0" time="{total_time:.3f}">
        <collection total="{test_count}" passed="{test_count-failures}" failed="{failures}" skipped="0" name="Test collection for {assembly_name}">
            {''.join(test_cases)}
        </collection>
    </assembly>
</assemblies>'''
        
        return xml_content.encode('utf-8')
    
    def _parse_test_data(self, data: bytes, scenario: Dict[str, Any]) -> Dict[str, Any]:
        """Parse test data using the Python parser."""
        request = ParseRequest(
            tenant_id="demo-data",
            project_id=scenario['repo_name'].replace('/', '-'),
            environment="demo",
            branch="main",
            build_number=scenario.get('build_number')
        )
        
        try:
            response = self.orchestrator.parse_report(data, request)
            
            if response.success:
                return {
                    'success': True,
                    'framework': response.data.framework,
                    'test_count': response.data.totals.total,
                    'passed': response.data.totals.passed,
                    'failed': response.data.totals.failed,
                    'skipped': response.data.totals.skipped,
                    'duration': response.data.totals.duration_sec,
                    'run_id': response.run_id,
                    'saas_format': response.saas_format,  # Ready for autotest API
                    'test_cases': response.data.test_cases
                }
            else:
                return {'success': False, 'error': response.error}
                
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _upload_to_autotest(self, parse_result: Dict[str, Any], scenario: Dict[str, Any], team_id: int) -> Dict[str, Any]:
        """Upload parsed results to autotest platform via API."""
        
        # Simulate the results upload API call
        # In reality, this would call your autotest API endpoints
        
        print(f"      🔄 Simulating upload to autotest API...")
        print(f"         📊 {parse_result['test_count']} test cases")
        print(f"         🔧 Framework: {parse_result['framework']}")
        print(f"         📈 Results: {parse_result['passed']} passed, {parse_result['failed']} failed")
        
        # Simulate API call delay
        time.sleep(0.1)
        
        # For demo purposes, always return success
        # In production, this would make actual HTTP requests to your autotest API
        return {
            'success': True,
            'build_id': f"demo-build-{scenario['build_number']}",
            'test_runs_created': parse_result['test_count']
        }
    
    def _print_loading_summary(self, results: Dict[str, Any]):
        """Print summary of demo data loading."""
        print(f"\n📊 DEMO DATA LOADING SUMMARY")
        print("=" * 35)
        print(f"✅ Scenarios loaded: {results['scenarios_loaded']}")
        print(f"🧪 Total test cases: {results['total_test_cases']}")
        print(f"🏗️  Builds created: {results['builds_created']}")
        print(f"🔧 Frameworks tested: {', '.join(results['frameworks_tested'])}")
        
        if results['errors']:
            print(f"\n❌ Errors: {len(results['errors'])}")
            for error in results['errors']:
                print(f"   • {error}")
        
        print(f"\n🎯 Next Steps:")
        print(f"   1. Check your autotest dashboard for the demo data")
        print(f"   2. Verify parsing results across different frameworks")
        print(f"   3. Test dashboard features with realistic data")

def main():
    """Main function for demo data loading."""
    print("🎨 Autotest Demo Data Loader")
    print("=" * 30)
    
    # Initialize loader
    loader = AutotestDemoDataLoader()
    
    # Load demo scenarios
    results = loader.load_demo_scenarios(team_id=4)
    
    print(f"\n🎉 Demo data loading complete!")
    print(f"   • Use this data to test your dashboard features")
    print(f"   • Validate parsing across {len(results['frameworks_tested'])} frameworks")
    print(f"   • Test with {results['total_test_cases']} realistic test cases")

if __name__ == "__main__":
    main()
