package lesson2;

import java.util.Scanner;

public class MultiplicationTable {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a;
		int b;
		int c;
		
		Scanner inputDevice = new Scanner(System.in);
		
		System.out.print("Input the size of the table>>");
		c = inputDevice.nextInt();
		for (a=1; a<=c; ++a)
		{
		    for (b=1; b<=c; ++b)
		    {
		    	System.out.print(String.format("%4d", a*b));  
		    }
		    System.out.println();
		}    
	}

}
