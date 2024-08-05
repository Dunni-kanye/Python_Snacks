      import java.util.Random;

public class ProtestDemandsApp{

	public static void main(String[]args){

		String[] demands = {
				     "Restoration of petrol subsidies and forex regime",
				     "Government should address food shortage",
					"Government should address unemployment",
					"Government should address wasteful spending by those in power",
					"We don't want protest",
					 "Government should enhance healthcare facilities",
  					  "We dey protest because say we dey hungry",
					   "we dey protest because the inflation rate don affect us to di point wey we no fit afford di simple tins of life"
						};
		String randomDemand = getRandomDemands(demands);
		
		System.out.println("You are welcome to the Protest Demands App");
		System.out.println("#EndBadGovernance");
		System.out.println("Protest demands 2024");
		System.out.println(randomDemand);

	}
	
		

	public static String getRandomDemands(String[] demands){
			Random rand = new Random();
			int randomIndex = rand.nextInt(demands.length);
			return demands[randomIndex];
	

    }
 }

