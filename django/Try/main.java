import java.util.Scanner;
public class main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        // String name = "Ameen Hamza";
        // String depart = "BS-AI";
        // String roll_id = "21f-bsai-57";
        // System.out.println("Name :"+name);
        // System.out.println("Department :"+depart);
        // System.out.println("Roll no :"+name);

        // System.out.println("Enter first number :");
        // int num1 = sc.nextInt();

        // System.out.println("Enter Second number :");
        // int num2 = sc.nextInt();
        
        // System.out.println("Multiplication of two number is :"+num1*num2);

        System.out.println("Enter first number :");
        int number = sc.nextInt();

        System.out.println("Enter Second number :");
        int number1 = sc.nextInt();

        System.out.println("Enter operator '+' '-' '*' '/'");
        char operator = sc.next().charAt(0);
        int answer=0;
        switch(operator){

            case '+': answer = number + number1;
            break;
            case '-': answer = number - number1;
            break;
            case '*': answer = number * number1;
            break;
            case '/': answer = number / number1;
            break; 
        }
        System.out.println(answer);
    }
}