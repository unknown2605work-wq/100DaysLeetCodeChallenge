class Solution {
    public boolean isPerfectSquare(int num) {
        if (num < 0) return false;
        double root = Math.sqrt(num);
        return root == (int) root;
    }
}