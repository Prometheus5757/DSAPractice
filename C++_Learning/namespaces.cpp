#include <iostream>

namespace first{
    int x = 1;
}
namespace second{
    int x = 2;
}

int main(){

    //Namespace = provides a solution for preventing name conflicts in large projects.
    // Each Entity needs a unique name.
    // A namespace allows for identically named entities as long as the namespaces are different.

    std::string name = "Bro";

    std::cout << "Hello " << name << " the number is " << second::x;
    return 0;
}