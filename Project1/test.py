import json
import sys
import io
import importlib

program_module = importlib.import_module("project")

def run_test_case(json_file, program_function):
    with open(json_file, 'r') as f:
        test_groups = json.load(f)

    test_cases = [case for group in test_groups.values() for case in group]

    inputs = [case["input"] for case in test_cases]
    expected_outputs = [case["expected"] for case in test_cases]

    sys.stdin = io.StringIO("\n".join(inputs) + "\n")
    sys.stdout = io.StringIO()

    try:
        program_function() 
        full_output = sys.stdout.getvalue().strip().split("\n")
    finally:
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        
    for i, line in enumerate(full_output):
        if ">>>" in line: 
            actual_outputs = full_output[i:]
            break
    else:
        actual_outputs = full_output 

    all_pass = True
    for i, (expected, actual) in enumerate(zip(expected_outputs, actual_outputs)):
        actual = actual[4:]
        if expected != actual:
            print(f"Test {json_file} - Case {i+1}: FAILED")
            print(f"  Input:    {inputs[i]}")
            print(f"  Expected: {expected}")
            print(f"  Got:      {actual}")
            print()
            all_pass = False
    
    if all_pass:
        print(f"Test {json_file}: PASSED")

# Running tests
run_test_case("test_cases.json", program_module.main)
