import os
import re

# Filename of the compile executable, must be in working directory
EXE_NAME = "compile"

# Subdirectory of working directory that contains test files
TEST_DIR = "tests"

# Some simple "rules" for how many errors to expect
# More specific file patterns must go before less specific
VERIFY_COUNT = (("test\d.txt", 0),
                ("syntax6.txt", 5),
                ("syntax\d.txt", 1),
                ("semantic\d{1,2}.txt", 1))

working_directory = os.getcwd()
compile_path = os.path.join(working_directory, EXE_NAME)
test_path = os.path.join(working_directory, TEST_DIR)

fail_count = 0
test_files = os.listdir(test_path)

for filename in test_files:
    filepath = os.path.join(test_path, filename)

    compile_command = "%s < %s > %s" %(compile_path,
                                       filepath,
                                       os.devnull,)

    raw_return_code = os.system(compile_command)
    
    # This might not work right in windows!
    return_code = raw_return_code >> 8

    found = False
    for pattern, count in VERIFY_COUNT:
        if re.match(pattern, filename):
            if return_code != count:
                fail_count += 1
                print "Error: %s had %d errors, expecting %d" %(filename, return_code, count)

            found = True
            break
    
    if not found:
        fail_count += 1
        print "Error: no rule found for %s" %filename

print "Done %d running tests with %d failures" %(len(test_files), fail_count)