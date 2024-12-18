
# Advent of Code 2024
Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels. 
https://adventofcode.com/

About my Python level - haven't use python in two years (switched to Postman and JS instead), so this is again a great, but painful, experience :-).

# Cheatsheet
As every year, there are some small code snippets and python features that make the work easier. One of them is the script to prepare the file structure for the whole month :-)
Among others are (so that I don't forget to use these in the following challenging December days):
* reading the file: `input = [line.strip('\n') for line in f.readlines()]`, `input_num = [list(map(int, line.split())) for line in input]`
* use of list comprehension: 
  * `found_one = [m.start() for m in re.finditer(key, line)]`
   * list of strings to list of numbers: `line_int = list(map(int, line_str))`
* regex in string lines: `re.findall(r'\d+', line)`
* enumerate
* split: `_, game, move = line.split(":")`, `re.split(r'[:|]', line)`
* strip
* while, for-else, if-elif-else, match-case 
* print: `print('-'*20)`
* generators: cycle, next, zip
* data: list, tuple (namedtuple), set  dict (collections module - OrderedDict, defaultdict, Counter), string, int, deque
* range
* try-except-else-finally
* time: `import time`, `time.perf_counter()`
 

## unittests
``` 
import unittest
from day02a import set_direction

class TestSetDirection(unittest.TestCase):

    def test_increasing(self):
        self.assertEqual(set_direction(1, 10), 1)
```