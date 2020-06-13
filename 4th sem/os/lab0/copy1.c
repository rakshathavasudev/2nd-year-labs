// Java program to illustrate renaming and 
// moving a file permanently to a new loaction 
import java.io.*; 
import java.nio.file.Files; 
import java.nio.file.*; 

public class Test 
{ 
	public static void main(String[] args) throws IOException 
	{ 
		Path temp = Files.move 
		(Paths.get("C:\\Users\\Mayank\\Desktop\\44.txt"), 
		Paths.get("C:\\Users\\Mayank\\Desktop\\dest\\445.txt")); 

		if(temp != null) 
		{ 
			System.out.println("File renamed and moved successfully"); 
		} 
		else
		{ 
			System.out.println("Failed to move the file"); 
		} 
	} 
} 
