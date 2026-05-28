import java.util.*;

class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        int n = mat.length;
        int m = mat[0].length;

        int[] result = new int[n * m];
        int ndiagonals = n + m - 1;

        List<List<Integer>> diagonals = new ArrayList<>(ndiagonals);

        for (int i = 0; i < ndiagonals; i++) {
            diagonals.add(new ArrayList<>());
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                diagonals.get(i + j).add(mat[i][j]);
            }
        }

        int index = 0;
        for (int i = 0; i < ndiagonals; i++) {
            List<Integer> current = diagonals.get(i);
            if (i % 2 == 0) {
                for (int j = current.size() - 1; j >= 0; j--) {
                    result[index++] = current.get(j);
                }
            } else {
                for (int j = 0; j < current.size(); j++) {
                    result[index++] = current.get(j);
                }
            }
        }
        return result;
    }
}