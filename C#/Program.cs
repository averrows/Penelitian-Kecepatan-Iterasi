using System;
using System.Diagnostics;


public class Example
{
    public static void Main()
    {
        Stopwatch stopwatch = new Stopwatch();

        stopwatch.Start();
        for (int i = 0; i < 1000000; i++)
        {
            
        }
        stopwatch.Stop();

        Console.WriteLine("Elapsed Time is {0} ms", stopwatch.ElapsedMilliseconds);
    }
}
