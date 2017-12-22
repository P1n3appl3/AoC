#include <stdio.h>
#include <sys/timeb.h>
#include <limits.h>

int main(){
    long a = 512, b = 191;
    int afac = 16807, bfac = 48271;
    int total = 0;
    struct timeb start, end;
    ftime(&start);
    for (long i = 0; i < 40000000; i++) {
        a = (a * afac) % INT_MAX;
        b = (b * bfac) % INT_MAX;
        total += (a & 0xFFFF) == (b & 0xFFFF);
    }
    ftime(&end);
    float diff = (1000 * end.time + end.millitm - start.millitm - 1000 * start.time);
    printf("Part 1: %d\tTime: %1.3f\n", total, diff / 1000);

    a = 512, b = 191, total = 0;
    ftime(&start);
    for (long i = 0; i < 5000000; i++) {
        do {
            a = (a * afac) % INT_MAX;
        } while (a % 4 != 0);
        do {
            b = (b * bfac) % INT_MAX;
        } while (b % 8 != 0);
        total += (a & 0xFFFF) == (b & 0xFFFF);
    }
    ftime(&end);
    diff = (1000 * end.time + end.millitm - start.millitm - 1000 * start.time);
    printf("Part 2: %d\tTime: %1.3f\n", total, diff / 1000);
    return 0;
}
