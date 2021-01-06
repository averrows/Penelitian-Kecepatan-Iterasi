package Java;

public class Javawhiletest {
    public static void main(String[] args) {
        long startTime = System.nanoTime();
        int x = 0;
        while(x < 100000 ){
            x++;
        }
        long endTime = System.nanoTime();
        long totalTime = (endTime - startTime) / 1000000;
        System.out.format("Elapsed Time is %d ms", totalTime);
    }
}
