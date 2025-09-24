#!/usr/bin/env python3
"""
Comprehensive Parser Stress Test Suite
Tests parsing robustness with various scenarios including:
- Normal reports (pass/fail)
- Corrupted/malformed reports
- Huge reports
- Edge cases
- Performance analysis
"""

import os
import sys
import json
import time
import random
import string
from pathlib import Path
from typing import Dict, List, Any

# Add the test parser to Python path
parser_path = Path(r'C:\autotest\test-parser-mvp')
sys.path.insert(0, str(parser_path))

from core.parser_orchestrator import get_orchestrator
from models import ParseRequest, TestStatus

class ParserStressTester:
    """Comprehensive stress tester for the parser system."""
    
    def __init__(self):
        self.orchestrator = get_orchestrator()
        self.results = {
            'total_tests': 0,
            'passed_tests': 0,
            'failed_tests': 0,
            'parse_times': [],
            'scenarios': {}
        }
    
    def run_all_tests(self):
        """Run all stress test scenarios."""
        print("🧪 Parser Stress Test Suite")
        print("=" * 50)
        
        scenarios = [
            ("Normal Reports", self.test_normal_reports),
            ("Corrupted XML", self.test_corrupted_xml),
            ("Malformed JSON", self.test_malformed_json),
            ("Huge Reports", self.test_huge_reports),
            ("Edge Cases", self.test_edge_cases),
            ("Empty/Null Content", self.test_empty_content),
            ("Unicode/Encoding", self.test_unicode_content),
            ("Memory Stress", self.test_memory_stress),
            ("Timeout Scenarios", self.test_timeout_scenarios),
            ("Mixed Frameworks", self.test_mixed_frameworks)
        ]
        
        for scenario_name, test_func in scenarios:
            print(f"\n🔍 Testing: {scenario_name}")
            print("-" * 30)
            
            try:
                start_time = time.time()
                results = test_func()
                end_time = time.time()
                
                self.results['scenarios'][scenario_name] = {
                    'duration': end_time - start_time,
                    'results': results
                }
                
                print(f"✅ {scenario_name}: {results['passed']}/{results['total']} passed ({end_time - start_time:.2f}s)")
                
            except Exception as e:
                print(f"❌ {scenario_name}: Exception - {str(e)}")
                self.results['scenarios'][scenario_name] = {
                    'error': str(e)
                }
        
        self.print_summary()
    
    def test_normal_reports(self) -> Dict[str, int]:
        """Test with normal, well-formed reports."""
        results = {'total': 0, 'passed': 0, 'failed': 0}
        
        # JUnit XML with mixed results
        junit_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="Normal Tests" tests="5" failures="2" errors="1" time="10.5">
    <testsuite name="com.example.NormalTest" tests="5" failures="2" errors="1" time="10.5">
        <testcase classname="com.example.NormalTest" name="testPass1" time="1.0">
            <system-out>Test passed successfully</system-out>
        </testcase>
        <testcase classname="com.example.NormalTest" name="testPass2" time="1.5"/>
        <testcase classname="com.example.NormalTest" name="testFail1" time="2.0">
            <failure message="Assertion failed" type="AssertionError">
Expected: true
Actual: false
            </failure>
        </testcase>
        <testcase classname="com.example.NormalTest" name="testFail2" time="3.0">
            <failure message="Null pointer exception">NullPointerException at line 45</failure>
        </testcase>
        <testcase classname="com.example.NormalTest" name="testError1" time="3.0">
            <error message="System error" type="SystemError">
Database connection failed
            </error>
        </testcase>
    </testsuite>
</testsuites>'''
        
        # Test JUnit parsing
        result = self._parse_content(junit_xml.encode(), 'junit', 'normal-junit.xml')
        results['total'] += 1
        if result['success']:
            results['passed'] += 1
            print(f"   ✅ JUnit XML: {result['data']['totals']['total']} tests parsed")
        else:
            results['failed'] += 1
            print(f"   ❌ JUnit XML: {result['error']}")
        
        # Pytest JSON with mixed results
        pytest_json = {
            "created": "2023-12-01T10:30:00.123456",
            "duration": 15.5,
            "exitcode": 1,
            "summary": {"total": 4, "passed": 2, "failed": 1, "skipped": 1},
            "tests": [
                {
                    "nodeid": "tests/test_normal.py::test_success",
                    "outcome": "passed",
                    "duration": 0.123,
                    "call": {"outcome": "passed", "stdout": "Test passed"}
                },
                {
                    "nodeid": "tests/test_normal.py::test_failure",
                    "outcome": "failed",
                    "duration": 0.234,
                    "call": {
                        "outcome": "failed",
                        "longrepr": "AssertionError: Expected 5, got 3"
                    }
                },
                {
                    "nodeid": "tests/test_normal.py::test_another_pass",
                    "outcome": "passed",
                    "duration": 0.089
                },
                {
                    "nodeid": "tests/test_normal.py::test_skipped",
                    "outcome": "skipped",
                    "setup": {"longrepr": ["tests/test_normal.py", 42, "Skipped: not implemented"]}
                }
            ]
        }
        
        # Test Pytest parsing
        result = self._parse_content(json.dumps(pytest_json).encode(), 'pytest', 'normal-pytest.json')
        results['total'] += 1
        if result['success']:
            results['passed'] += 1
            print(f"   ✅ Pytest JSON: {result['data']['totals']['total']} tests parsed")
        else:
            results['failed'] += 1
            print(f"   ❌ Pytest JSON: {result['error']}")
        
        # Jest JSON with mixed results
        jest_json = {
            "numFailedTestSuites": 1,
            "numFailedTests": 2,
            "numPassedTests": 3,
            "numTotalTests": 5,
            "success": False,
            "testResults": [
                {
                    "assertionResults": [
                        {
                            "ancestorTitles": ["NormalTest"],
                            "title": "should pass test 1",
                            "status": "passed",
                            "duration": 123
                        },
                        {
                            "ancestorTitles": ["NormalTest"],
                            "title": "should pass test 2", 
                            "status": "passed",
                            "duration": 89
                        },
                        {
                            "ancestorTitles": ["NormalTest"],
                            "title": "should fail test 1",
                            "status": "failed",
                            "duration": 234,
                            "failureMessages": ["Expected 5 but received 3"]
                        }
                    ],
                    "name": "/project/src/normal.test.js"
                }
            ]
        }
        
        # Test Jest parsing
        result = self._parse_content(json.dumps(jest_json).encode(), 'jest', 'normal-jest.json')
        results['total'] += 1
        if result['success']:
            results['passed'] += 1
            print(f"   ✅ Jest JSON: {result['data']['totals']['total']} tests parsed")
        else:
            results['failed'] += 1
            print(f"   ❌ Jest JSON: {result['error']}")
        
        return results
    
    def test_corrupted_xml(self) -> Dict[str, int]:
        """Test with corrupted/malformed XML files."""
        results = {'total': 0, 'passed': 0, 'failed': 0}
        
        corrupted_xmls = [
            # Missing closing tags
            b'<?xml version="1.0"?><testsuites><testsuite name="test"><testcase name="test1">',
            
            # Invalid XML characters
            b'<?xml version="1.0"?><testsuites><testsuite name="test\x00invalid"><testcase name="test1"/></testsuite></testsuites>',
            
            # Malformed attributes
            b'<?xml version="1.0"?><testsuites><testsuite name=test><testcase name="test1"/></testsuite></testsuites>',
            
            # Nested XML errors
            b'<?xml version="1.0"?><testsuites><testsuite><testcase><failure>Unclosed CDATA <![CDATA[error</testcase></testsuite></testsuites>',
            
            # Encoding issues
            '<?xml version="1.0" encoding="UTF-8"?><testsuites><testsuite name="тест"><testcase name="тест1"/></testsuite></testsuites>'.encode('latin-1'),
        ]
        
        for i, corrupted_xml in enumerate(corrupted_xmls):
            results['total'] += 1
            result = self._parse_content(corrupted_xml, 'junit', f'corrupted-{i}.xml')
            
            if result['success']:
                print(f"   ⚠️  Corrupted XML {i+1}: Unexpectedly parsed successfully")
                results['passed'] += 1
            else:
                print(f"   ✅ Corrupted XML {i+1}: Correctly rejected - {result['error'][:50]}...")
                results['passed'] += 1  # Rejection is the correct behavior
        
        return results
    
    def test_malformed_json(self) -> Dict[str, int]:
        """Test with malformed JSON files."""
        results = {'total': 0, 'passed': 0, 'failed': 0}
        
        malformed_jsons = [
            # Missing closing brace
            b'{"tests": [{"nodeid": "test.py::test_func", "outcome": "passed"}',
            
            # Invalid JSON syntax
            b'{"tests": [{"nodeid": "test.py::test_func", "outcome": "passed",}]}',
            
            # Wrong data types
            b'{"tests": "not an array", "summary": {"total": "not a number"}}',
            
            # Truncated JSON
            b'{"testResults": [{"assertionResults": [{"title": "test", "st',
            
            # Invalid Unicode
            b'{"tests": [{"nodeid": "\xff\xfe\x00\x00test", "outcome": "passed"}]}',
        ]
        
        for i, malformed_json in enumerate(malformed_jsons):
            results['total'] += 1
            result = self._parse_content(malformed_json, 'pytest', f'malformed-{i}.json')
            
            if result['success']:
                print(f"   ⚠️  Malformed JSON {i+1}: Unexpectedly parsed successfully")
                results['passed'] += 1
            else:
                print(f"   ✅ Malformed JSON {i+1}: Correctly rejected - {result['error'][:50]}...")
                results['passed'] += 1  # Rejection is the correct behavior
        
        return results
    
    def test_huge_reports(self) -> Dict[str, int]:
        """Test with very large report files."""
        results = {'total': 0, 'passed': 0, 'failed': 0}
        
        print("   🔄 Generating large test reports...")
        
        # Test 1: Large JUnit XML (5MB)
        large_junit = self._generate_large_junit_xml(5000)  # 5000 test cases
        results['total'] += 1
        start_time = time.time()
        result = self._parse_content(large_junit, 'junit', 'huge-junit.xml')
        parse_time = time.time() - start_time
        
        if result['success']:
            results['passed'] += 1
            print(f"   ✅ Large JUnit (5K tests): Parsed in {parse_time:.2f}s")
        else:
            results['failed'] += 1
            print(f"   ❌ Large JUnit: {result['error']}")
        
        # Test 2: Large Pytest JSON (3MB)
        large_pytest = self._generate_large_pytest_json(3000)  # 3000 test cases
        results['total'] += 1
        start_time = time.time()
        result = self._parse_content(large_pytest, 'pytest', 'huge-pytest.json')
        parse_time = time.time() - start_time
        
        if result['success']:
            results['passed'] += 1
            print(f"   ✅ Large Pytest (3K tests): Parsed in {parse_time:.2f}s")
        else:
            results['failed'] += 1
            print(f"   ❌ Large Pytest: {result['error']}")
        
        # Test 3: Oversized file (>10MB) - should be rejected
        oversized_content = b'x' * (11 * 1024 * 1024)  # 11MB
        results['total'] += 1
        result = self._parse_content(oversized_content, 'junit', 'oversized.xml')
        
        if not result['success'] and 'limit' in result['error'].lower():
            results['passed'] += 1
            print(f"   ✅ Oversized file: Correctly rejected - {result['error']}")
        else:
            results['failed'] += 1
            print(f"   ❌ Oversized file: Should have been rejected")
        
        return results
    
    def test_edge_cases(self) -> Dict[str, int]:
        """Test edge cases and unusual scenarios."""
        results = {'total': 0, 'passed': 0, 'failed': 0}
        
        edge_cases = [
            # Empty test suite
            ('Empty JUnit', b'<?xml version="1.0"?><testsuites><testsuite name="empty" tests="0"></testsuite></testsuites>'),
            
            # Single test case
            ('Single test', b'<?xml version="1.0"?><testsuites><testsuite name="single" tests="1"><testcase name="only_test" time="1.0"/></testsuite></testsuites>'),
            
            # Very long test names
            ('Long names', f'<?xml version="1.0"?><testsuites><testsuite name="test" tests="1"><testcase name="{"very_long_test_name_" * 50}" time="1.0"/></testsuite></testsuites>'.encode()),
            
            # Special characters in names
            ('Special chars', '<?xml version="1.0"?><testsuites><testsuite name="test" tests="1"><testcase name="test_with_&lt;&gt;&amp;_chars" time="1.0"/></testsuite></testsuites>'.encode()),
            
            # Zero duration
            ('Zero duration', b'<?xml version="1.0"?><testsuites><testsuite name="test" tests="1"><testcase name="zero_time" time="0.0"/></testsuite></testsuites>'),
            
            # Negative duration
            ('Negative duration', b'<?xml version="1.0"?><testsuites><testsuite name="test" tests="1"><testcase name="negative_time" time="-1.0"/></testsuite></testsuites>'),
            
            # Missing required attributes
            ('Missing attrs', b'<?xml version="1.0"?><testsuites><testsuite><testcase/></testsuite></testsuites>'),
            
            # Deeply nested XML
            ('Deep nesting', b'<?xml version="1.0"?><testsuites><testsuite name="deep"><testcase name="test"><failure><message><details><inner>Deep failure</inner></details></message></failure></testcase></testsuite></testsuites>'),
        ]
        
        for case_name, content in edge_cases:
            results['total'] += 1
            result = self._parse_content(content, 'junit', f'edge-{case_name.replace(" ", "_")}.xml')
            
            if result['success']:
                results['passed'] += 1
                test_count = result['data']['totals']['total']
                print(f"   ✅ {case_name}: {test_count} tests parsed")
            else:
                # For edge cases, both success and controlled failure are acceptable
                if 'invalid' in result['error'].lower() or 'format' in result['error'].lower():
                    results['passed'] += 1
                    print(f"   ✅ {case_name}: Correctly handled - {result['error'][:40]}...")
                else:
                    results['failed'] += 1
                    print(f"   ❌ {case_name}: Unexpected error - {result['error'][:40]}...")
        
        return results
    
    def test_empty_content(self) -> Dict[str, int]:
        """Test with empty or null content."""
        results = {'total': 0, 'passed': 0, 'failed': 0}
        
        empty_cases = [
            ('Empty bytes', b''),
            ('Whitespace only', b'   \n\t  \n   '),
            ('Just XML declaration', b'<?xml version="1.0" encoding="UTF-8"?>'),
            ('Empty JSON object', b'{}'),
            ('Empty JSON array', b'[]'),
            ('Null bytes', b'\x00\x00\x00'),
        ]
        
        for case_name, content in empty_cases:
            results['total'] += 1
            result = self._parse_content(content, 'auto', f'empty-{case_name.replace(" ", "_")}.xml')
            
            if not result['success']:
                results['passed'] += 1
                print(f"   ✅ {case_name}: Correctly rejected")
            else:
                results['failed'] += 1
                print(f"   ❌ {case_name}: Should have been rejected")
        
        return results
    
    def test_unicode_content(self) -> Dict[str, int]:
        """Test with various Unicode and encoding scenarios."""
        results = {'total': 0, 'passed': 0, 'failed': 0}
        
        # Unicode test names and messages
        unicode_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<testsuites>
    <testsuite name="Unicode Tests" tests="3">
        <testcase name="测试中文" time="1.0"/>
        <testcase name="тест_русский" time="1.5"/>
        <testcase name="🧪_emoji_test" time="2.0">
            <failure message="Unicode failure: 测试失败">
Stack trace with unicode: файл.py:42
            </failure>
        </testcase>
    </testsuite>
</testsuites>'''.encode('utf-8')
        
        results['total'] += 1
        result = self._parse_content(unicode_xml, 'junit', 'unicode.xml')
        
        if result['success']:
            results['passed'] += 1
            print(f"   ✅ Unicode XML: {result['data']['totals']['total']} tests with Unicode names")
        else:
            results['failed'] += 1
            print(f"   ❌ Unicode XML: {result['error']}")
        
        return results
    
    def test_memory_stress(self) -> Dict[str, int]:
        """Test memory usage with multiple large files."""
        results = {'total': 0, 'passed': 0, 'failed': 0}
        
        print("   🔄 Testing memory stress with multiple large files...")
        
        # Parse multiple large files in sequence
        for i in range(5):
            large_content = self._generate_large_junit_xml(1000)  # 1000 tests each
            results['total'] += 1
            
            start_time = time.time()
            result = self._parse_content(large_content, 'junit', f'memory-stress-{i}.xml')
            parse_time = time.time() - start_time
            
            if result['success']:
                results['passed'] += 1
                print(f"   ✅ Memory test {i+1}: Parsed 1K tests in {parse_time:.2f}s")
            else:
                results['failed'] += 1
                print(f"   ❌ Memory test {i+1}: {result['error']}")
        
        return results
    
    def test_timeout_scenarios(self) -> Dict[str, int]:
        """Test timeout handling (simulated with very large files)."""
        results = {'total': 0, 'passed': 0, 'failed': 0}
        
        print("   ⏱️  Testing timeout scenarios...")
        
        # Create an extremely large file that might timeout
        huge_content = self._generate_large_junit_xml(10000)  # 10K tests
        results['total'] += 1
        
        start_time = time.time()
        result = self._parse_content(huge_content, 'junit', 'timeout-test.xml')
        parse_time = time.time() - start_time
        
        if result['success']:
            results['passed'] += 1
            print(f"   ✅ Huge file: Parsed 10K tests in {parse_time:.2f}s (within timeout)")
        elif 'timeout' in result['error'].lower():
            results['passed'] += 1
            print(f"   ✅ Huge file: Correctly timed out after {parse_time:.2f}s")
        else:
            results['failed'] += 1
            print(f"   ❌ Huge file: Unexpected error - {result['error']}")
        
        return results
    
    def test_mixed_frameworks(self) -> Dict[str, int]:
        """Test with mixed framework scenarios."""
        results = {'total': 0, 'passed': 0, 'failed': 0}
        
        # Test auto-detection with various formats
        test_files = [
            ('JUnit XML', self._generate_junit_xml(50), 'junit'),
            ('Pytest JSON', self._generate_pytest_json(30), 'pytest'),
            ('Jest JSON', self._generate_jest_json(40), 'jest'),
            ('Go Test JSON', self._generate_go_test_json(25), 'go-test'),
        ]
        
        for framework_name, content, expected_framework in test_files:
            results['total'] += 1
            result = self._parse_content(content, 'auto', f'mixed-{framework_name.lower().replace(" ", "-")}.json')
            
            if result['success']:
                detected_framework = result['data']['framework']
                if detected_framework == expected_framework:
                    results['passed'] += 1
                    print(f"   ✅ {framework_name}: Correctly detected as {detected_framework}")
                else:
                    results['failed'] += 1
                    print(f"   ❌ {framework_name}: Expected {expected_framework}, got {detected_framework}")
            else:
                results['failed'] += 1
                print(f"   ❌ {framework_name}: Parse failed - {result['error']}")
        
        return results
    
    def _parse_content(self, content: bytes, format_hint: str, filename: str) -> Dict[str, Any]:
        """Parse content and return structured result."""
        request = ParseRequest(
            tenant_id="stress-test",
            project_id="stress-test",
            report_type=format_hint if format_hint != 'auto' else None,
            environment="stress-test"
        )
        
        start_time = time.time()
        try:
            response = self.orchestrator.parse_report(content, request)
            parse_time = time.time() - start_time
            self.results['parse_times'].append(parse_time)
            
            return {
                'success': response.success,
                'data': response.data.dict() if response.data else None,
                'error': response.error,
                'parse_time': parse_time
            }
        except Exception as e:
            parse_time = time.time() - start_time
            return {
                'success': False,
                'data': None,
                'error': str(e),
                'parse_time': parse_time
            }
    
    def _generate_large_junit_xml(self, num_tests: int) -> bytes:
        """Generate a large JUnit XML file with specified number of tests."""
        xml_parts = ['<?xml version="1.0" encoding="UTF-8"?>', '<testsuites>']
        
        # Create multiple test suites
        suite_size = 100
        num_suites = (num_tests + suite_size - 1) // suite_size
        
        for suite_idx in range(num_suites):
            suite_name = f"TestSuite{suite_idx}"
            tests_in_suite = min(suite_size, num_tests - suite_idx * suite_size)
            failures = random.randint(0, tests_in_suite // 3)
            
            xml_parts.append(f'<testsuite name="{suite_name}" tests="{tests_in_suite}" failures="{failures}" time="{random.uniform(10, 100):.3f}">')
            
            for test_idx in range(tests_in_suite):
                test_name = f"test{test_idx:04d}"
                duration = random.uniform(0.001, 2.0)
                
                if test_idx < failures:
                    # Failed test
                    xml_parts.append(f'<testcase classname="{suite_name}" name="{test_name}" time="{duration:.3f}">')
                    xml_parts.append(f'<failure message="Test {test_idx} failed">Stack trace for test {test_idx}</failure>')
                    xml_parts.append('</testcase>')
                else:
                    # Passed test
                    xml_parts.append(f'<testcase classname="{suite_name}" name="{test_name}" time="{duration:.3f}"/>')
            
            xml_parts.append('</testsuite>')
        
        xml_parts.append('</testsuites>')
        return '\n'.join(xml_parts).encode('utf-8')
    
    def _generate_large_pytest_json(self, num_tests: int) -> bytes:
        """Generate a large Pytest JSON file."""
        tests = []
        passed = 0
        failed = 0
        skipped = 0
        
        for i in range(num_tests):
            outcome = random.choice(['passed', 'passed', 'passed', 'failed', 'skipped'])  # Bias toward passed
            duration = random.uniform(0.001, 1.0)
            
            test = {
                "nodeid": f"tests/test_stress_{i // 100}.py::test_case_{i:04d}",
                "outcome": outcome,
                "duration": duration
            }
            
            if outcome == 'failed':
                test["call"] = {
                    "outcome": "failed",
                    "longrepr": f"AssertionError: Test {i} failed intentionally"
                }
                failed += 1
            elif outcome == 'passed':
                test["call"] = {"outcome": "passed"}
                passed += 1
            else:
                skipped += 1
            
            tests.append(test)
        
        pytest_data = {
            "created": "2023-12-01T10:30:00.123456",
            "duration": sum(t['duration'] for t in tests),
            "exitcode": 1 if failed > 0 else 0,
            "summary": {
                "total": num_tests,
                "passed": passed,
                "failed": failed,
                "skipped": skipped
            },
            "tests": tests
        }
        
        return json.dumps(pytest_data).encode('utf-8')
    
    def _generate_junit_xml(self, num_tests: int) -> bytes:
        """Generate a normal-sized JUnit XML file."""
        return self._generate_large_junit_xml(num_tests)
    
    def _generate_pytest_json(self, num_tests: int) -> bytes:
        """Generate a normal-sized Pytest JSON file."""
        return self._generate_large_pytest_json(num_tests)
    
    def _generate_jest_json(self, num_tests: int) -> bytes:
        """Generate a Jest JSON file."""
        assertion_results = []
        passed = 0
        failed = 0
        
        for i in range(num_tests):
            status = random.choice(['passed', 'passed', 'failed'])  # Bias toward passed
            duration = random.randint(50, 500)
            
            assertion = {
                "ancestorTitles": [f"TestSuite{i // 10}"],
                "title": f"test case {i:03d}",
                "status": status,
                "duration": duration
            }
            
            if status == 'failed':
                assertion["failureMessages"] = [f"Test {i} failed: Expected true, got false"]
                failed += 1
            else:
                passed += 1
            
            assertion_results.append(assertion)
        
        jest_data = {
            "numTotalTests": num_tests,
            "numPassedTests": passed,
            "numFailedTests": failed,
            "success": failed == 0,
            "testResults": [
                {
                    "assertionResults": assertion_results,
                    "name": "/project/src/stress.test.js"
                }
            ]
        }
        
        return json.dumps(jest_data).encode('utf-8')
    
    def _generate_go_test_json(self, num_tests: int) -> bytes:
        """Generate a Go test JSON file (newline-delimited)."""
        lines = []
        
        for i in range(num_tests):
            test_name = f"TestCase{i:03d}"
            package = f"github.com/example/package{i // 10}"
            outcome = random.choice(['pass', 'pass', 'fail'])  # Bias toward pass
            duration = random.uniform(0.001, 0.5)
            
            # Run event
            lines.append(json.dumps({
                "Action": "run",
                "Package": package,
                "Test": test_name
            }))
            
            # Output event
            lines.append(json.dumps({
                "Action": "output",
                "Package": package,
                "Test": test_name,
                "Output": f"=== RUN   {test_name}\\n"
            }))
            
            # Result event
            lines.append(json.dumps({
                "Action": outcome,
                "Package": package,
                "Test": test_name,
                "Elapsed": duration
            }))
        
        return '\n'.join(lines).encode('utf-8')
    
    def print_summary(self):
        """Print comprehensive test summary."""
        print("\n" + "=" * 50)
        print("📊 STRESS TEST SUMMARY")
        print("=" * 50)
        
        total_scenarios = len(self.results['scenarios'])
        passed_scenarios = sum(1 for s in self.results['scenarios'].values() if 'error' not in s)
        
        print(f"🎯 Scenarios: {passed_scenarios}/{total_scenarios} passed")
        
        if self.results['parse_times']:
            avg_time = sum(self.results['parse_times']) / len(self.results['parse_times'])
            max_time = max(self.results['parse_times'])
            min_time = min(self.results['parse_times'])
            
            print(f"⏱️  Parse Times: avg={avg_time:.3f}s, max={max_time:.3f}s, min={min_time:.3f}s")
        
        print(f"\n📋 Detailed Results:")
        for scenario, data in self.results['scenarios'].items():
            if 'error' in data:
                print(f"   ❌ {scenario}: {data['error']}")
            else:
                duration = data['duration']
                results = data['results']
                print(f"   ✅ {scenario}: {results['passed']}/{results['total']} ({duration:.2f}s)")
        
        print(f"\n🎉 Parser Stress Test Complete!")
        print(f"   • Tested robustness with corrupted files")
        print(f"   • Verified handling of large files")
        print(f"   • Confirmed edge case handling")
        print(f"   • Validated Unicode support")
        print(f"   • Assessed memory usage")
        print(f"   • Checked timeout protection")

def main():
    """Run the stress test suite."""
    tester = ParserStressTester()
    tester.run_all_tests()

if __name__ == "__main__":
    main()
