from ast import literal_eval

class PyUnitTest:
    def __init__(self, testFn=None, testFilePath=None):
        self.testFn = testFn
        self.testFilePath = testFilePath

    def loadTests(self, testSuiteNumber):
        try:
            with open(self.testFilePath, 'r', encoding='utf-8') as f:
                try:
                    self.tests = literal_eval(f.read())[testSuiteNumber]
                except (ValueError, SyntaxError):
                    print("ERROR: Failed to load tests due to invalid test suite format.")
                    print("ACTION: Ensure the test suite is a valid Python dictionary.")
                    exit(0)
        except FileNotFoundError:
            print("ERROR: Failed to load tests due to invalid test suite path: {0}".format(self.testFilePath))
            print("ACTION: Provide a valid file path and try again.")
            exit(0)
        finally:
            print()

    def runTests(self, testSuiteName=None, testSuiteNumber=None, descriptions=True):
        self.loadTests(testSuiteNumber)
        
        prettyPrintCharLen = 14
        passed = total = 0
        
        if testSuiteName:
            prettyPrintCharLen += len(testSuiteName)
        else:
            testSuiteName = '\b'
        print("-"*prettyPrintCharLen + "\nRUNNING {0} TESTS\n".format(testSuiteName) + "-"*prettyPrintCharLen)

        for i, test in enumerate(self.tests.values()):
            if type(test["input"]) == type(tuple()):
                actual = self.testFn(*test["input"])
            else:
                actual = self.testFn(test["input"])

            total += 1
            print("\n{0}) ".format(i+1), end='')

            if descriptions:
                print("{1}".format(i+1, test["description"]))
                print(" "*3 + "-"*(len(test["description"])))

            try:
                assert actual == test["expected"]
            except AssertionError:
                if descriptions:
                    print(" "*3, end='')
                print("Actual: {0}\n".format(actual) + " "*3 + "Expected: {0}\n".format(test["expected"]) + " "*3 + "Result: FAIL")
            else:
                passed += 1
                if descriptions:
                    print(" "*3, end='')
                print("Actual: {0}\n".format(actual) + " "*3 + "Expected: {0}\n".format(test["expected"]) + " "*3 + "Result: PASS")
                continue
            finally:
                print()
        print("Success Rate: {0}/{1}\n".format(passed, total))
