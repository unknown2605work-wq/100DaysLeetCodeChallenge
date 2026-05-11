class Solution {
    public int hammingWeight(int n) {
        int result = Integer.bitCount(n);
        return result;
    }
}