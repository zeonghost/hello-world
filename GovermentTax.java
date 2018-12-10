package lesson2;
import java.util.Scanner;

public class GovermentTax {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int num1;
		int num2;
		double output = 0;
		
		Scanner inputDevice = new Scanner(System.in);
		
		System.out.print("What's the filter?\r");
		System.out.print("1.Single\r");
		System.out.print("2.Married filing jointly\r");
		System.out.print("3.Married filing separately\r");
		System.out.print("4.Head of household\r");
		System.out.print("Input the number before the choice>>");
		num1 = inputDevice.nextInt();
		switch(num1) {
		case 1: 
			System.out.print("What's the taxable income?>>");
			num2 = inputDevice.nextInt();
			if((num2>=0)&&(num2<=8350))
			{
				output= num2 * 0.1;
			}
			else if((num2>=8351)&&(num2<=33950))
			{
				output = num2 *1.15;
			}
			else if((num2>=33951)&&(num2<=82250))
			{
				output = num2 *0.25;
			}
			else if((num2>=82251)&&(num2<=171550))
			{
				output = num2 *0.28;
			}
			else if((num2>=171551)&&(num2<=372950))
			{
				output = num2 *0.33;
			}
			else
			{
				output = num2 *0.35;
			}
		break;
		case 2: 
			System.out.print("What's the taxable income?>>");
			num2 = inputDevice.nextInt();
			if((num2>=0)&&(num2<=16700))
			{
				output= num2 * 0.1;
			}
			else if((num2>=16700)&&(num2<=67900))
			{
				output = num2 *0.15;
			}
			else if((num2>=67901)&&(num2<=137050))
			{
				output = num2 *0.25;
			}
			else if((num2>=137051)&&(num2<=208850))
			{
				output = num2 *0.28;
			}
			else if((num2>=208851)&&(num2<=372950))
			{
				output = num2 *0.33;
			}
			else
			{
				output = num2 *0.35;
			}
		break;
		case 3: 
			System.out.print("What's the taxable income?>>");
			num2 = inputDevice.nextInt();
			if((num2>=0)&&(num2<=8350))
			{
				output= num2 * 0.1;
			}
			else if((num2>=8351)&&(num2<=33950))
			{
				output = num2 *0.15;
			}
			else if((num2>=33951)&&(num2<=68525))
			{
				output = num2 *0.25;
			}
			else if((num2>=68526)&&(num2<=104425))
			{
				output = num2 *0.28;
			}
			else if((num2>=104426)&&(num2<=186475))
			{
				output = num2 *0.33;
			}
			else
			{
				output = num2 *0.35;
			}
		break;
		case 4: 
			System.out.print("What's the taxable income?>>");
			num2 = inputDevice.nextInt();
			if((num2>=0)&&(num2<=11950))
			{
				output= num2 * 0.1;
			}
			else if((num2>=11951)&&(num2<=45500))
			{
				output = num2 *0.15;
			}
			else if((num2>=45501)&&(num2<=117450))
			{
				output = num2 *0.25;
			}
			else if((num2>=117451)&&(num2<=190200))
			{
				output = num2 *0.28;
			}
			else if((num2>=190201)&&(num2<=372950))
			{
				output = num2 *0.33;
			}
			else
			{
				output = num2 *0.35;
			}
		break;
		}
		System.out.println("The tax need to pay is "+output);
	}

}
