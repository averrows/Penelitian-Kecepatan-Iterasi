#include <stdio.h> 
#include <time.h> 

int main() 
{ 
	clock_t t; 
	t = clock(); 
    int i;
    for (i = 1; i <= 100000; ++i)
    {
    }
	t = clock() - t; 
	double time_taken = ((double)t)/(CLOCKS_PER_SEC/1000);

	printf("Elapsed Time is %f ms \n", time_taken); 
	return 0; 
} 