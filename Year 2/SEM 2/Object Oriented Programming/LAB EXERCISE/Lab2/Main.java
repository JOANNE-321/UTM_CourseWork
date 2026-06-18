public class Main {
    public static void main(String[] args) {

        System.out.println("Q1");
        Employee e1 = new Employee();
        e1.setEmpNum(101);
        e1.setEmpName("Ali");
        System.out.println("Employee Number: " + e1.getEmpNum());
        System.out.println("Employee Name: " + e1.getEmpName());
    
        System.out.println("\nQ2");
        Car c1 = new Car();
        c1.setBrand("Toyota");
        System.out.println("Car Brand: " + c1.getBrand());
        System.out.println("Car Year: " + c1.getYear());
    
        System.out.println("\nQ3");
        Book b1 = new Book("Java 101", "John Doe");
        b1.display();
    
        System.out.println("\nQ4");
        Student s1 = new Student();
        s1.setName("Joanne");
        System.out.println("Student Name: " + s1.getName());
        System.out.println("Student Age: " + s1.getAge());

        System.out.println("\nQ5");
        Message m1 = new Message();
        m1.display();
        m1.display("Nice to meet You ! ");

        System.out.println("\nQ6");
        new User();
        new User();
        System.out.println("Total Users: " + User.getUserCount());
        
        System.out.println("\nQ7");
        Employee e = new Employee();
        e.setSalary(5000);
        System.out.println("Salary: " + e.getSalary());
    
    
    }
}

// Q1: Class and Object Creation
// Q7: Access Modifiers
class Employee {
    
    // TODO: Add fields
    private int empNum;
    private String empName;
    
    // TODO: Make salary private
    private int salary;

    // TODO: Add setter and getter methods
    // setter
    public void setEmpNum(int num) {
        empNum = num;
    }

    public void setEmpName(String name) {
        empName = name;
    }

    // getter
    public int getEmpNum() {
        return empNum;
    }

    public String getEmpName() {
        return empName;
    }

    // TODO: Write setSalary() and getSalary() methods
    public void setSalary(int s) {
        salary = s;
    }
    public int getSalary() {
        return salary;
    }

}

//Q2: Instance Variables and Data Fields
class Car {
    // TODO: Declare two private instance variables (brand and year)
    private String brand;
    private int year = 2004;

    // TODO: Create setter for brand
    public void setBrand(String brand) {
        this.brand = brand;
    }
    // TODO: Create getter for year
    public int getYear() {
        return year;
    }

    public String getBrand() {
        return brand;
    }

}


// Q3: Constructor Usage
class Book {
    private String title;
    private String author;

    // TODO: Add a constructor
    public Book(String t, String a) {
        title = t;
        author = a;
    }

    public void display() {
        System.out.println("Title: " + title);
        System.out.println("Author: " + author);
    }
}

// Q4: Getters and Setters
class Student {
    private String name;
    private int age = 21;

    // TODO: Implement setter for name
    public void setName(String name) {
        this.name = name;
    }

    // TODO: Implement getter for age
    public int getAge() {
        return age;
    }

    public String getName() {
        return name;
    }
}

// Q5: Method Overloading
class Message {
    // TODO: Write a method display() that prints "Hello!"
    public void display() {
        System.out.println("Hello!");
    }
    // TODO: Overload display(String msg) to print "Message: msg"
    public void display(String msg) {
        System.out.println("Message: " + msg);
    }
}

//Q6: Static vs Non-Static
class User {
    // TODO: Declare a static counter variable
    private static int counter = 0;

    public User() {
        // TODO: Increment counter
        counter++;
    }

    public static int getUserCount() {
        // TODO: Return counter
        return counter;
    }
}

