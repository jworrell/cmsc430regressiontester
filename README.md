cmsc430regressiontester
=======================

CMSC430 Regression Tester

Might not work in windows. 

Your main (c++) function must return the error count:
```C
int main() {
    // All your logic here
    
    // We return the error count to make automated regression testing easier.
    return Listing::getErrorCount();
}
```

Paths must be set in python file:
```Python
# Filename of the compile executable, must be in working directory
EXE_NAME = "compile"

# Subdirectory of working directory that contains test files
TEST_DIR = "tests"
```
