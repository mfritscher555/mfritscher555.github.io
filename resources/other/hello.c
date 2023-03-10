#include <stdio.h>
#include <stdlib.h>

float addition(float num1, float num2){
    return num1 + num2;
}

float subtraction(float num1, float num2){
    return num1 - num2;
}

float multiplication(float num1, float num2){
  return num1 * num2;
}

float division(float num1, float num2){
  return num1 / num2;
}



int main() {
  // Create floateger variable that will store the number we get from the user

  float myNum1;
  int operator;
  float myNum2;
  int termInput;

//   char signs[] = {"+", "-", "/", ""};

  

  // Ask the user to type a number

do{

  printf("Type a number and press enter: \n"); 
  scanf("%f", &myNum1);

  printf("Do you want to add, subtract, multiply or divide? Type 0 for add, 1 for subtract, 2 for multiply, 3 for divide: \n");
  scanf("%d", &operator);

  printf("Type another number: \n");
  scanf("%f", &myNum2);

  if (operator == 0){
    printf("Your number is: %f \n", addition(myNum1, myNum2));
    }
  else if (operator==1) {
    printf("Your number is: %f \n", subtraction(myNum1, myNum2));
    }
  else if (operator==2) {
    printf("Your number is: %f \n", multiplication(myNum1, myNum2));
    }
  else if (operator==3){
    printf("Your number is: %f \n", division(myNum1, myNum2));
  }


  printf("Type 1 to end the program or 0 to continue: \n");
  scanf("%d", &termInput);

}

while (termInput !=1);

  // only terminates the program when the user says so (so the user can have a chance to the see output)
  return 0;

  // Return the output and terminate the program
}

