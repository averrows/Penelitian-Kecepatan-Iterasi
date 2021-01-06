#include <algorithm> 
#include <chrono> 
#include <iostream> 
using namespace std; 
using namespace std::chrono; 

int main() 
{ 
    auto start = high_resolution_clock::now(); 

    int i = 1; 
    do {
        ++i;
    }
    while (i <= 100000);

	auto stop = high_resolution_clock::now(); 

	auto duration = duration_cast<microseconds>((stop - start)/1000); 

	cout << "Time taken by function: "
		<< duration.count() << " miliseconds" << endl; 

	return 0; 
}