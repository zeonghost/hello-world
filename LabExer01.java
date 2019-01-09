package strAndWrapClass;
import java.util.Scanner;

public class LabExer01 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String s;
		String n;
		
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("Number input >> ");
		
		s = scanner.nextLine();
		System.out.println("String Input: "+s);
		n = s.replaceAll("[^\\\\.0123456789]","");
		System.out.println("Number: "+n);
		if(n.contains("."))
		{
			float f = Float.parseFloat(n);
			Float floatobj = new Float(f);
			System.out.println("Number: "+f);
			System.out.println("Data type: " +floatobj.getClass().getSimpleName());
		}
		else 
		{
			int i = Integer.parseInt(n);
			if((i<=127)&&(i>=-128))
			{
				byte b =(byte)i;
				Byte byteobj = new Byte(b);
				System.out.println("Number: "+b);
				System.out.println("Data type: " +byteobj.getClass().getSimpleName());
			}
			else
			{
				Integer intobj = new Integer(i);
				System.out.println("Number: "+i);
				System.out.println("Data type: " +intobj.getClass().getSimpleName());
			}
		}
	}

}
