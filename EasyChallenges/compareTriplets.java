// Complete the compareTriplets function below.
    static List<Integer> compareTriplets(List<Integer> a, List<Integer> b) {
        List<Integer> aliceList = a;
        List<Integer> bobList = b;
        
        //intial scores
        int aScore = 0;
        int bScore = 0;
		
		//initalize finalScore ArrayListist
        List<Integer> finalScore = new ArrayList<Integer>();      
        
		//for loop going through the size 
        for(int i = 0; i < aliceList.size(); i++ ) {
            //check for differences & and add accordingly
			if(aliceList.get(i) > bobList.get(i)) {
                aScore++;
            }
            else if(bobList.get(i) > aliceList.get(i)) {
                bScore++;
            } 
            else {
                continue;
            }
        }
        //add to finalScore
        finalScore.add(aScore);
        finalScore.add(bScore);
        System.out.println(finalScore);
                  
        return(finalScore);

    }