public static void staircase(int n) {
        // Write your code here
        for (int i = n; i > 0; i--) {
            for (int y = 0; y < i - 1; y++) {
                System.out.print(" ");                    
            }
            for (int x = 0; x < n - i; x++) {
                System.out.print("#");            
            }   
            System.out.println("#");
        }
    }
}