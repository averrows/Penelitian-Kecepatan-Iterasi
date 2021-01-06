using System;
using System.Diagnostics;


public class Csharpfortest
{
    public static void Main()
    {
        Stopwatch stopwatch = new Stopwatch();

        stopwatch.Start();
        for (int i = 0; i < 100000; i++)
        {
            
        }
        stopwatch.Stop();

        Console.WriteLine("Elapsed Time is {0} ms", stopwatch.ElapsedMilliseconds);
    }
}
