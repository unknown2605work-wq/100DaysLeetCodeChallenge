class Solution {
    public boolean canReach(int[] arr, int start) {
        return dfs(arr, start);
    }

    public boolean dfs(int[] arr, int index) {
        if(index < 0 || index >= arr.length)
            return false;

        if(arr[index] < 0)
            return false;

        if(arr[index] == 0)
            return true;

        int jump = arr[index];
        arr[index] = -arr[index];

        return dfs(arr, index + jump) ||
               dfs(arr, index - jump);
    }
}