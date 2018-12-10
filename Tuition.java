package lesson2;

public class Tuition {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		double fee=10000;
		int year = 1;
		
		do {
			fee=fee*1.07;
			year++;
		}while(fee<20000);
		System.out.println("The year the tuition be double is  "+year);
	}

}
