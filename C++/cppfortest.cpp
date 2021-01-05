#include <algorithm> 
#include <chrono> 
#include <iostream> 
using namespace std; 
using namespace std::chrono; 

int main() 
{ 
    auto start = high_resolution_clock::now(); 

    for (int i = 1; i <= 100000; ++i) {
    cout << i << endl;
    }

	auto stop = high_resolution_clock::now(); 

	auto duration = duration_cast<microseconds>((stop - start)/1000); 

	cout << "Time taken by function: "
		<< duration.count() << " miliseconds" << endl; 

	return 0; 
} 