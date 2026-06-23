class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        A = nums1
        B = nums2

        total = len(A) + len(B)
        half = total // 2

        left = 0
        right = len(A)

        while True:

            i = (left + right) // 2
            j = half - i

            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < len(A) else float("inf")

            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:

                if total % 2:
                    return min(Aright, Bright)

                return (
                    max(Aleft, Bleft) +
                    min(Aright, Bright)
                ) / 2

            elif Aleft > Bright:
                right = i - 1

            else:
                left = i + 1