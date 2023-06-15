#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char* argv[])
{
    clock_t start_time, end_time;
    double cpu_time_used;

    start_time = clock();

    int q = 0;
    int even = 0;
    float even_p = 0;
    int odd = 0;
    float odd_p = 0;

    printf("Give the number of iterations\n");
    scanf("%d", &q);

    srand(time(NULL));

    for(int i = q; i > 0; i--){
        int rand_num = rand() % 1000;
        if(rand_num %2 == 0){
            even += 1;
            printf("%d is an even number\n", rand_num);
        } else {
            odd += 1;
            printf("%d is an odd number\n", rand_num);
        }
    }
int total = even + odd;
even_p = (even * 100) / total;
odd_p = (odd * 100) / total;

printf("\n");
printf("Odd probability :: %.4f\n",odd_p);
printf("Even probability :: %.4f\n",even_p);
printf("\n");

end_time = clock();
cpu_time_used = ((double) (end_time - start_time)) / CLOCKS_PER_SEC;

printf("Execution time (C code) : %f seconds\n", cpu_time_used);
    return 0;
}