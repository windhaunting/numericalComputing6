import unittest
########################################
# Merge sort code
########################################

def merge_sort(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x)/2)
    y = merge_sort(x[:mid])
    z = merge_sort(x[mid:])
    while (len(y) > 0) or (len(z) > 0):
        if len(y) > 0 and len(z) > 0:
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(z) > 0:
            result += z
            z = []
        else:
            result += y
            y = []
    return result
    

########################################
# Testing code
########################################

## Add code here ##
class MergeSortTester(unittest.TestCase):
    def test1(self):
        '''
        test the merge_sort with an unsorted integer array
        input array  [3,5,8,1,4,100]
        '''
        x = [3,5,8,1,4,100]
        sortedX = [1,3,4,5,8,100]
        self.assertEqual(merge_sort(x), sortedX)

    def test2(self):
        '''
        test the merge_sort with an already sorted integer array
        input array  [1,2,3,4,5]
        '''
        x = [1,2,3,4,5]
        sortedX = [1,2,3,4,5]
        self.assertEqual(merge_sort(x), sortedX)


########################################
# Main
########################################
if __name__=="__main__":
    unittest.main()