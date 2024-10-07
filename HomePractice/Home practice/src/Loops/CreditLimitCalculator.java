package Loops;

import java.util.Scanner;

public class CreditLimitCalculator {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter account number: ");
        int account = sc.nextInt();

        System.out.print("Enter balance at beginning:");
        double balance = sc.nextDouble();
        System.out.print("Enter total charges:");
        double totalCharges = sc.nextDouble();
        System.out.print("Enter total credits:");
        double totalCredits = sc.nextDouble();
        System.out.print("Enter credit limit:");
        double creditLimit = sc.nextDouble();

        double newBalance = balance + totalCharges - totalCredits;
        System.out.println("New balance for account:" + account + "New Balance"+ newBalance);
        if (newBalance > creditLimit){
            System.out.println("Credit limit exceeded");
        }
    }
}