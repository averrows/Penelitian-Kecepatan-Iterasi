package Java;

public class Javafortest {


        public static void main(String[] args) {
            long startTime = System.nanoTime();
            for (int i = 1; i <= 100000; i = i + 1) {
                System.out.println(i);
              }
            long endTime = System.nanoTime();
        long totalTime = (endTime - startTime)/1000000;
        System.out.format("Elapsed Time is %d ms", totalTime);
        }
    }

