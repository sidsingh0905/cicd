import datetime

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Run tests
results = []

if add(2, 3) == 5:
    results.append("PASS - add test passed")
else:
    results.append("FAIL - add test failed")

if subtract(5, 3) == 2:
    results.append("PASS - subtract test passed")
else:
    results.append("FAIL - subtract test failed")

# Generate report
with open("test-report.txt", "w") as f:
    f.write(f"Test Report - {datetime.datetime.now()}\n")
    f.write("="*40 + "\n")
    for r in results:
        f.write(r + "\n")

print("Tests completed! Report generated.")