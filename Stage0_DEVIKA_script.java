import java.util.*;
public class Stage0_DEVIKA_script
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
    String SU = "@Devika";
    String TH = "@Devpoo";
 
    
    System.out.println("HammingDist:"+ hammingDist (SU, TH));
    System.out.println("Name = Devika Kaliana");
    System.out.println("Email = devikakaliana94@gmail.com");
    System.out.println("slack username = @Devika");
    System.out.println("Biostack = Gemonics");
    System.out.println("Twitter Handel = @Devpoo");
}
}
           
        
