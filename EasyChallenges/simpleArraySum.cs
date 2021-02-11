/*
     * Complete the simpleArraySum function below.
     */
    static int simpleArraySum(int[] ar) {
        /*
         * Write your code here.
         */
        /*int sum = 0;
        for(int i; i <= ar.Length(); i++) {
            sum += ar[i];
        }
        return(sum);*/
        int sum = ar.Sum();
        return(sum);
    }
