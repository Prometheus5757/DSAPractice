#include <iostream>
#include <vector>

//typedef std::vector<std::pair<std::string, int>> pairlist_t;
//typedef std::string text_t;
//typedef int number_t;
using text_t = std::string;
using number_t = int;

int main(){

    //typedef = reserved keyword used to create an additional name (alias) for another data type kinda like a nickname
    // New identifier for an existing type
    // Helps with readability and reduces typos
    // Use when there is a clear benefit to doing so
    // Typedef has mostly been replaced nowadays with 'using' (because they work better with templates)

    text_t firstName = "Bro"; //Behaves exactly like a string
    number_t age = 21;

    std::cout << firstName << '\n';
    std::cout << age << '\n';

    return 0;
}