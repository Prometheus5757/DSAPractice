#include <iostream>

int main(){

    // arithmetic operators = return the result of a specific arithmetic operation (+ - * /)

    int students = 20;

    //students = students + 1;
    //students += 1;
    //students++;

    //students = students - 1;
    //students -= 1;
    //students--;

    //students = students * 2;
    //students*=2;

    //students = students / 3;
    //students/=3;

    //Order of precedence:
    //parenthesis
    //multiplication and division
    //addition and subtraction

    int students2 = 6 - (5 + 4) * 3 / 2; //should be -7
    int remainder = students % 3;

    std::cout << students2;

    return 0;
}