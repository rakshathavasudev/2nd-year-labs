// Java program to illustrate renaming and 
// moving a file permanently to a new loaction 
import java.io.*; 
import java.nio.file.Files; 
import java.nio.file.*; 

public class copy1 
{ 
	public static void main(String[] args) throws IOException 
	{ 
		Path temp = Files.move 
		(Paths.get("C:\\Users\\HP\\Desktop\\4th sem\\os\\lab0\\a.txt"), 
		Paths.get("C:\\Users\\HP\\Desktop\\4th sem\\os\\lab0\\b.txt")); 

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