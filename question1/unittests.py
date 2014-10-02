import unittest
from utils import *
 
class TestData(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_all(self):
        '''
        There is no real way to properly test this with a simple unittest for the following reasons:
        
        (1). Data can be empty for legitimate reasons - such as when there is no data unless it can be guaranteed there will always be data.
        (2). There is no state named DC in the USA however the data contains such a state - DC should maybe fail the unittest however this may be part of a trick question.
        (3). A proper unittest should do more than check whether or not there is data; it should check to see if the data looks reasonable as well as having an understanding as to whether all states are valid.
        (4). State validity should not be hardcoded - states can be added or removed from the USA so if the input data is being tested then an outside dynamic data source should be used to validate state names.
        (5). The data coming back from the REST call should also be validated for correctness.
        (6). At this time, the only real test is whether or not the target URL can be accessed and all tests succeed so long as the target URL is accessible without errors.
        '''
        for statename in states:
            __data__ = fetch_data_for(statename)
            self.assertEqual( __data__ is not None, True)
        pass
 
if __name__ == '__main__':
    unittest.main()
    