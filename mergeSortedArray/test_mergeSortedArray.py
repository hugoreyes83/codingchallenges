import pytest
from mergeSortedArray import Solution

@pytest.mark.parametrize("nums1,m,nums2,n,expected",
                    (
                     ([1,2,3,0,0,0], 3, [2,5,6],3, [1,2,2,3,5,6]),
                     ([1],1,[],1,[1]),
                     ([0],0,[1],1,[1]),
                    ))
def test_Solution(nums1, m, nums2, n, expected):
    foo = Solution()
    assert foo.merge(nums1,m,nums2,n) == expected