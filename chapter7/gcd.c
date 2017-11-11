#include "stdio.h"
#include "stdlib.h"

/**
 * This function takes in two pointers,
 * then stores the result into the memory location of `b`.
 */
void gcd(int *a, int *b) {
        int r = *b;
        while (r != 0) {
                *b = r;
                r = *a % *b;
                *a = *b;
        }
}

int main(int argc, char *argv[]) {
        int *myA = malloc(sizeof(int));
        int *myB = malloc(sizeof(int));

        FILE *file;
        file = fopen("chap6_7File.txt", "r");
        if (file) {
                while(fscanf(file, "%d %d\n", myA, myB) != EOF) {
                        // comment out the following line to only return the answers
                        printf("gcd(%d,%d) = ", *myA, *myB);
                        gcd(myA, myB);
                        printf("%d\n", *myB);
                }
        }
}
