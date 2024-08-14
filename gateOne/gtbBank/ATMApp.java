import java.util.ArrayList; 
import java.util.Random;
import java.util.Scanner;

public class AtmApp {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        ArrayList<Integer> accountNumbers = new ArrayList<>();
        ArrayList<Double> balances = new ArrayList<>();
        ArrayList<String> pins = new ArrayList<>();

	System.out.println("Welcome");
	System.out.println("Kindly type 'Next' to select an option:");
	String next = scanner.next();
	if (!next.equals("Next")) {
	System .out.println("Please type 'Next' only");
	next = scanner.next();
					
	}
        boolean transactions = true;

        while (transactions) {
            System.out.println("\n--- ATM Machine ---");
            System.out.println("1. Create an account");
            System.out.println("2. Close account");
            System.out.println("3. Deposit money");
            System.out.println("4. Withdraw money");
            System.out.println("5. Check Account balance");
            System.out.println("6. Transfer from one account to another");
            System.out.println("7. Change Pin");
            System.out.println("8. Exit");

            System.out.print("Choose an option: ");
            int choice1 = scanner.nextInt();

            switch (choice1) {

                case 1:
                    System.out.println("Create account ");
                    System.out.println("Enter first name: ");
                    String firstName = scanner.next();

                    System.out.println("Enter last name: ");
                    String lastName = scanner.next();
                    System.out.print("Enter a 4-digit PIN: ");
                    String pin = scanner.next();

                    if (pin.length() != 4) {
                        System.out.println("Invalid PIN. Account creation failed.");
                        break;
                    }

                    int accountNumber = random.nextInt(900000);
                    accountNumbers.add(accountNumber);
                    balances.add(0.0);
                    pins.add(pin);
                    System.out.println("Account successfully created");
                    System.out.println("Your account number is: " + accountNumber);
                     break;

                case 2:
                    System.out.print("Enter your account number: ");
                    accountNumber = scanner.nextInt();
                    int index = accountNumbers.indexOf(accountNumber);
                    if (index != -1) {
                        System.out.printf("Account number %d closed successfully.\n", accountNumber);
                        accountNumbers.remove(index);
                        balances.remove(index);
                        pins.remove(index);
                    } else {
                         System.out.println("Account not found.");
                    }
                    break;

                case 3:
                     System.out.print("Enter your account number: ");
                    accountNumber = scanner.nextInt();
                    index = accountNumbers.indexOf(accountNumber);
                    if (index != -1) {
                        System.out.print("Enter deposit amount: ");
                        double amount = scanner.nextDouble();
                        if (amount > 0) {
                            balances.set(index, balances.get(index) + amount);
                            System.out.println("Deposit successful! New balance: $" + balances.get(index));
                        } else {
                            System.out.println("Invalid deposit amount.");
                        }
                    } else {
                        System.out.println("Account not found.");
                    }
                    break;

                case 4:
                    System.out.print("Enter your account number: ");
                    accountNumber = scanner.nextInt();
                    index = accountNumbers.indexOf(accountNumber);
                    if (index != -1) {
                        System.out.print("Enter withdrawal amount: ");
                        double amount = scanner.nextDouble();
                        if (amount > 0 && amount <= balances.get(index)) {
                            balances.set(index, balances.get(index) - amount);
                            System.out.println("Withdrawal successful! New balance: $" + balances.get(index));
                        } else {
                            System.out.println("Invalid withdrawal amount or insufficient funds.");
                        }
                    } else {
                        System.out.println("Account not found.");
                    }
                    break;

                case 5:
                    System.out.print("Enter your account number: ");
                    accountNumber = scanner.nextInt();
                    index = accountNumbers.indexOf(accountNumber);
                    if (index != -1) {
                        System.out.println("Your current balance is: $" + balances.get(index));
                    } else {
                        System.out.println("Account not found.");
                    }
                    break;

               case 6:
			
   			 System.out.print("Enter your account number: ");
   			 accountNumber = scanner.nextInt();
    			index = accountNumbers.indexOf(accountNumber);
    			System.out.println("Create recipient's account first if you have not:");
   			 if (index != -1) {
       				 System.out.println ("Enter the recipient's account number: ");
       				 int recipientAccount = scanner.nextInt();
       				 int recipientIndex = accountNumbers.indexOf(recipientAccount);

      			  if (recipientIndex != -1) {
            			System.out.print("Enter transfer amount: ");
           			 double transferAmount = scanner.nextDouble();

            		if (transferAmount > 0 && transferAmount <= balances.get(index)) {
                		balances.set(index, balances.get(index) - transferAmount);
                		balances.set(recipientIndex, balances.get(recipientIndex) + transferAmount);
                
               		 System.out.println("Transfer successful!");
               		 System.out.println("Your new balance: $" + balances.get(index));
                	System.out.println("Recipient's new balance: $" + balances.get(recipientIndex));

               		 System.out.print("Would you like to generate a receipt? (yes/no): ");
               		 String generateReceipt = scanner.next();
				
			if (generateReceipt.equalsIgnoreCase("yes")) {
                    	System.out.println("\n---------- Transfer Receipt --------------------------");
                    	System.out.println("Sender Account: " + accountNumbers.get(index));
                   	 System.out.println("Recipient Account: " + accountNumbers.get(recipientIndex));
                    	System.out.println("Transfer Amount: $" + transferAmount);
                   	 System.out.println("------------------------------------------------------------\n");
               			 }
           		 } else {
               		 System.out.println("Invalid transfer amount  or insufficient funds.");
           		 }
       			 } else {
           		 System.out.println("Recipient account not found.");
       		      		 }


               	 
   			 } else {
       			 System.out.println("Your account number not found.");
    				}
   			 break;

		case 7:
                    System.out.print("Enter your account number: ");
                    accountNumber = scanner.nextInt();
                    index = accountNumbers.indexOf(accountNumber);
                    if (index != -1) {
                        System.out.print("Enter your current PIN: ");
                        String currentPin = scanner.next();
                        if (pins.get(index).equals(currentPin)) {
                            System.out.print("Enter your new 4-digit PIN: ");
                            String newPin = scanner.next();
                            System.out.print("Confirm your new 4-digit PIN: ");
                            String confirmPin = scanner.next();
                            if (confirmPin.length() == 4 && newPin.equals(confirmPin)) {
                                pins.set(index, confirmPin);
                                System.out.println("PIN changed successfully.");
                            } else {
                                System.out.println("PINs do not match or invalid PIN. PIN change failed.");
                            }
                        } else {
                            System.out.println("Incorrect current PIN.");
                        }
                    } else {
                        System.out.println("Account not found.");
                    }
                    break;

                case 8:
                    transactions = false;
                    System.out.println("Thank you for using the ATM. Goodbye!");
                    break;

                default:
                    System.out.println("Invalid option. Please try again.");
                    break;
            }
        }
    }
}
