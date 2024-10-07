package Loops;

import java.util.Scanner;

public class GasMilage {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int gallonsUsed = 0;
        int milesDriven = 0;
        int totalGallons = 0;
        int totalMiles = 0;
        double tripMPG = 0;
        double totalMPG = 0;

        System.out.println("Enter number of trips:");
        int trips = sc.nextInt();
        for (int i = 0; i < trips; i++) {
            System.out.println("Enter miles driven or(-1 to quit):");
             milesDriven = sc.nextInt();
            if (milesDriven == -1) {
                break;
            }
            System.out.println("Enter gallons used");
            gallonsUsed = sc.nextInt();
            tripMPG = (double) milesDriven / gallonsUsed;
            System.out.printf("Miles per gallon for this trip is:%.2f\n", tripMPG);
            totalMiles += milesDriven;
            totalGallons += gallonsUsed;

            totalMPG = (double) totalMiles / totalGallons;
            System.out.printf("Total gallons for this trip is:%.2f\n", totalMPG);




        }

    }
}
