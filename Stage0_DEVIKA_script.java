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
 
    
    System.out.println("Devika Kaliana, devikakaliana94@gmail.com,@Devika, Gemonics, @Devpoo, "+ hammingDist (SU, TH));
    
}
}
              
