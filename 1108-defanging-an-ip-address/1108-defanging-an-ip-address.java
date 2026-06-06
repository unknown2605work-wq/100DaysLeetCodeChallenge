class Solution {
    public String defangIPaddr(String address) {
        String[] parts = address.split("\\.");
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < parts.length; i++) {
            sb.append(parts[i]);
            
            if (i < parts.length - 1) {
                sb.append("[.]");
            }
        }
        
        return sb.toString();
    }
}