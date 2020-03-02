from django.test import TestCase
from regex_builder.regex_builder import createIntRegex
# Create your tests here.
import re

class RegexTestCase(TestCase):

    def test_integer_regex(self):
        
        p_low = 50667
        p_high = 54672

        regex_range = createIntRegex(str(p_low), str(p_high))
        print(regex_range)
        _range = re.compile(regex_range)

        for i in range(10000, 1000000):
            if i < p_low:
                self.assertFalse(_range.match(str(i)))
            if i >= p_low and i <= p_high:
                self.assertTrue(_range.match(str(i)))
            if i > p_high:
                self.assertFalse(_range.match(str(i)))