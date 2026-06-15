#include <iostream>
#include <vector>
#include <map>
#include <chrono>   // High-resolution clock library
#include <algorithm> // For std::binary_search

int main() {
    // 1. Setup a large dataset of 5 million "satellite IDs"
    const int DATA_SIZE = 5000000; // Boost this to 5 million
    const int TARGET_ID = 4500000; // Search for 4.5 million

    std::vector<int> vecData;
    std::map<int, int> mapData;

    // Reserve memory for the vector ahead of time to avoid mid-loop allocations
    vecData.reserve(DATA_SIZE);

    for (int i = 0; i < DATA_SIZE; ++i) {
        vecData.push_back(i);
        mapData[i] = i; // Map key: ID, Value: ID
    }

    // --- BENCHMARK 1: MAP LOOKUP ---
    // Start tracking time
    auto startMap = std::chrono::high_resolution_clock::now();
    
    // Perform the lookup in the tree structure
    auto mapResult = mapData.find(TARGET_ID);
    
    // Stop tracking time
    auto endMap = std::chrono::high_resolution_clock::now();
    auto durationMap = std::chrono::duration_cast<std::chrono::nanoseconds>(endMap - startMap).count();

    // --- BENCHMARK 2: SORTED VECTOR BINARY SEARCH ---
    auto startVec = std::chrono::high_resolution_clock::now();
    
    // Perform a binary search on the contiguous vector layout
    bool vecResult = std::binary_search(vecData.begin(), vecData.end(), TARGET_ID);
    
    auto endVec = std::chrono::high_resolution_clock::now();
    auto durationVec = std::chrono::duration_cast<std::chrono::nanoseconds>(endVec - startVec).count();

    // --- PRINT RESULTS ---
    std::cout << "--- Benchmark Results ---" << std::endl;
    std::cout << "std::map Lookup Time:       " << durationMap << " ns" << std::endl;
    std::cout << "std::vector Binary Search:  " << durationVec << " ns" << std::endl;

    return 0;
}