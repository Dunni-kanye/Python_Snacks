package Loops;

import java.util.Scanner;

public class SalesCommisionCalculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double[] itemPrices = {239.99, 129.75,99.95,350.89};
        int[] itemsSold = new int[itemPrices.length];
        double commissionRate = 0.09;
        double salary = 200;
        double totalSales = 0;
        for (int count = 0; count < itemPrices.length; count++) {
            System.out.println("Enter the item price for " + itemPrices[count] + ":");
            itemsSold[count] = sc.nextInt();
             totalSales += itemsSold[count] * itemPrices[count];
        }

         double commission = commissionRate * totalSales;
        double totalCommission = salary + commissionRate;
        System.out.println("Commission: " + commission);



    }
}
