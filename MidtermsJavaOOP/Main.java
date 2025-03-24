import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        //1. Create Five instances of the "Person" class, set their attributes 
        // using the constructor, and print their name and age. 
        Person person1 = new Person("John Doe", 21, "Marikina City");
        Person person2 = new Person("Saige Fuentes", 61, "New York City"); 
        Person person3 = new Person("Bowen Higgins", 48, "All America City");
        Person person4 = new Person("Boomboom Markcross", 69, "Mandaluyong City");
        Person person5 = new Person("Franklin Sierra", 48, "Beijing City");

        person1.personInfo();
        person2.personInfo();
        person3.personInfo();
        person4.personInfo();
        person5.personInfo();

        System.out.println();

        // 2. Create two instances of the "Dog" class, set their attributes using 
        // the constructor and modify the attributes using the setter methods 
        // and print the updated values.
        Dog dog1 = new Dog("Doggy", "Golden Retriever");
        Dog dog2 = new Dog("Brownie", "Shiba Inu"); 

        dog1.displayDogInfo();
        dog2.displayDogInfo();

        System.out.println('\n');

        //3. Calculate the area and perimeter of the rectangle
        Scanner scan = new Scanner(System.in);
        char letter;

        do{
            System.out.println("Calculating Rectangle...");
            System.out.println("Length: ");
            int input1 = scan.nextInt();
            System.out.println("Width: ");
            int input2 = scan.nextInt();

            Rectangle calcu1 = new Rectangle();
            System.out.println("Rectangle Area: " + calcu1.calculateRectangle(input1, input2));

            
            System.out.println("Type Y if you want to Exit");
            letter = scan.next().charAt(0);
        }while(letter != 'y' && letter != 'Y');

        scan.close();
    }
}

//1. Create a class called "Person" with a name, age, and address attribute
class Person{
    String personName; 
    int age;
    String address;
    
    Person(){}
    Person(String personName, int age, String address){
        this.personName = personName;
        this.age = age;
        this.address = address;
    }

    void personInfo(){
        System.out.println("Your name is " + personName + ", " 
        + age + " years old, lived at " + address + ".");
    }
}

//2. Create a class called "Dog" with a name and breed attribute
class Dog{
    private String name;
    private String breed;

    public Dog(){}
    public Dog(String name, String breed){
        this.name = name;
        this.breed = breed;
    }
    //Getters
    public String getDogName(){return name;}
    public String getBreed(){return breed;}

    //Setters
    public void setDogName(String newDogName){ this.name = newDogName;}
    public void setBreed(String breed){ this.breed = breed;}

    public void displayDogInfo(){
        System.out.println("Dog name: " + name + "\nDog's breed: " + breed);
    }
}

//3. Create a class called "Rectangle" with width and height attributes
class Rectangle{
    public int length;
    public int width;

    public int calculateRectangle(int length, int width){
        return length * width;
    }
}