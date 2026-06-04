class Solution {
    public boolean checkIfPangram(String sentence) {
        int n = sentence.length();
        if(n < 26){
            return false;
        }

        if(n >= 26){
            boolean[] alphabet = new boolean[26];
            int uniqueCount = 0;

            for (char c : sentence.toCharArray()) {
                int index = c - 'a'; 
                if (!alphabet[index]) {
                    alphabet[index] = true;
                    uniqueCount++;
                }
            }
            if(uniqueCount == 26)
                return true;
        }
        return false;
    }
}