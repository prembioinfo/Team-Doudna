import java.util.*;
public class Azeezat_stage0_script
{
         static int hammingDist(String SU, String TH)
{
    int i = 0, count = 0;
    while (i < SU.length())
    {
        if (SU.charAt(i) != TH.charAt(i))
            count++;
        i++;
    }
    return count;
}
 
public static void main (String[] args)
{
    String SU = "@azeezat";
    String TH = "@azeezat02";
 
    
    System.out.println("HammingDist:"+ hammingDist (SU, TH));
    System.out.println("Name = Osikoya Azeezat");
    System.out.println("Email = oluwatobiosikoya1gmail.com");
    System.out.println("slack username = @azeezat");
    System.out.println("Biostack = Drug Development");
    System.out.println("Twitter Handle = @azeezat");
}
}
           
        
