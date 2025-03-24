public class Week7 {
    private static int[] numbers = {0, 10, 15, 54, 14, 10, 24, 20};
    public static void main(String[] args){
        for(int i = 0; i < numbers.length; i++){
            if(numbers[i] == 10 || numbers[i] == 15){
            System.out.println("The value " + numbers[i] + " is at index " + i);
            }
            else if(numbers[i] != 15){System.out.println("Hindi siya 15. index" + i);}
            else{System.out.println("NOTHING!!!");}
        }
        int day = 3;
            switch (day){
                case 1: {System.out.println("Monday"); break;}
                case 2: {System.out.println("Tuesday"); break;}
                case 3: {System.out.println("Wednesday"); break;}
                case 4: {System.out.println("Thursday"); break;}
                case 5: {System.out.println("Friday"); break;}
            } 
    }
}