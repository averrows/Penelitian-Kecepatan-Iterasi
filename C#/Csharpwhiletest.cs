using System;
using System.Diagnostics;


public class Csharpwhiletest
{
    public static void Main()
    {
        Stopwatch stopwatch = new Stopwatch();

        stopwatch.Start();
        int x = 0;
        while(x<100000){
            x++;
        }
        stopwatch.Stop();

        Console.WriteLine("Elapsed Time is {0} ms", stopwatch.ElapsedMilliseconds);
    }
}
