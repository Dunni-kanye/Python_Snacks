import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList; 
import java.util.Scanner;
public class CheckOutSystem {

	public static void main(String[] args) {
	Scanner input = new Scanner(System.in);

	System.out.print("What is the customer's name? ");
        String customerName = input.nextLine();

        ArrayList<String> productNames = new ArrayList<>();
        ArrayList<Double> productPrices = new ArrayList<>();
        ArrayList<Integer> productQuantities = new ArrayList<>();

	 LocalDateTime now = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");
        String formattedDateTime = now.format(formatter);
	String flag = "";

        while (!(flag.equalsIgnoreCase("no"))){

            System.out.print("What did the user buy? ");
            productNames.add(input.nextLine());

            System.out.print("How many pieces? ");
            productQuantities.add(input.nextInt());

            System.out.print("How much per unit? ");
            productPrices.add(input.nextDouble());

            System.out.print("Add more items? (yes/no)");
            flag = input.next();
        }
	
	System.out.println("What is the cashier's name? ");
        String cashierName = input.next();
	
	double vatRate = 0.175; 
    	double discountRate = 0.0;

        double subTotal = 0.0;

         for (int index = 0; index < productNames.size(); index++) {
            subTotal += productPrices.get(index) * productQuantities.get(index);
        }
	 System.out.printf("Subtotal calculated: %.2f\n", subTotal);

	System.out.print("How much discount do you want to give:");
            discountRate = input.nextDouble();
	double discount = (subTotal *( discountRate/100));
	
	double vat = subTotal * vatRate;
        double total = subTotal - discount + vat;

	System.out.print("Amount Paid: ");
        double amountPaid = input.nextDouble();
        double balance = amountPaid - total;

	System.out.printf("Discount calculated: %.2f\n", discount);
        System.out.printf("VAT calculated: %.2f\n", vat);
        System.out.printf("Total calculated: %.2f\n", total);

	System.out.printf("Cashier: %s\n", cashierName);
        System.out.printf("Customer: %s\n", customerName);

	System.out.println("\nSEMICOLON STORES");
        System.out.println("MAIN BRANCH");
        System.out.println("LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.");
        System.out.println("TEL: 0329382843");
        System.out.println("Date and Time" + formattedDateTime);
        System.out.println("Cashier: " + cashierName);
	input.nextLine();
        System.out.println("Customer Name: " + customerName);
        System.out.println("============================================================");
        System.out.printf("%22s%10s%10s%15s","ITEM","QTY","PRICE","TOTAL(NGN)");
	System.out.println("\n-----------------------------------------------------------");
	
	 for (int index = 0; index < productNames.size(); index++) {
		System.out.printf("%22s %10d %10.2f %10.2f %n",productNames.get(index), productQuantities.get(index), productPrices.get(index), total);

        }

	System.out.println("----------------------------------------------------------------");
        System.out.printf("Sub Total: %25.2f\n", subTotal);
        System.out.printf("Discount: %26.2f\n", discount);
        System.out.printf("VAT @ 17.5%%: %23.2f\n", vat);
	System.out.println("============================================================");

        System.out.printf("Bill Total: %24.2f\n", total);
	
	
        System.out.printf("Amount Paid: %23.2f\n", amountPaid);
        System.out.printf("Balance: %26.2f\n", balance);
        	System.out.println("============================================================");
	System.out.println("THANK YOU FOR YOUR PATRONAGE");
        System.out.println("-------------------------------------");

       
        
	

	
}



		
				
}