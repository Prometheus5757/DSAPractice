#include <iostream>

int main(){
    // Type conversion = conversion of one data type to another
    // Implicit conversion = automatic conversion
    // Explicit conversion = precede value with new data type i.e. (int)

    int x = 3.14;

    std::cout << x << '\n' ; //prints 3 by implicit conversion to int

    double y = 3.14;

    std::cout << y << '\n'; //retains 3.14

    double z = (int) 3.14;

    std::cout << z << '\n'; // prints 3 from explicit conversion aka type casting

    // More Examples

    char a = 100;
    std::cout << a << '\n'; //Implicit cast using ASCII type conversion. ASCII character 100 is 'd'

    std::cout << (char) 100 << '\n'; //Explicit casting using type casting to char

    /*
    Real Use Case;
    Suppose there is an online exam where we have to give the user a score.

    Score is how many questions they got right divided by the total number of questions.
    */

    int correct = 8;
    int questions = 10;

    /*
    double score = correct/questions * 100; 
    
    This is wrong. This non-casted division is integer division, meaning we truncate the decimal portion of 0.8, which is 0. We then multiply by 100, which is why we get 0% as the output instead of 80%. Fix this by type casting one of the terms to a double.
    */
    
    double score = (double)correct/questions * 100; 

    std::cout << score << "%";

    return 0;
}