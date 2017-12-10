#include <stdio.h>
#include <string.h>
#include <sys/timeb.h>

int main(){
    FILE* file = fopen("input.txt", "r");
    int i = 0, len = 0;
    int list[2000];
    int listcopy[2000];

    fscanf(file, "%d", &i);
    while (!feof(file)) {
        list[len] = i;
        ++len;
        fscanf(file, "%d", &i);
    }
    fclose(file);

    memcpy(listcopy, list, 2000 * sizeof(int));

    struct timeb start, end;
    for (int i = 1; i < 3; i++) {
        memcpy(list, listcopy, 2000 * sizeof(int));
        ftime(&start);
        int place = 0;
        int steps = 0;
        while (place >= 0 && place < len) {
            int temp = place;
            place += list[place];
            list[temp] += 1 - 2 * (list[temp] > 2) * (i == 2);
            ++steps;
        }
        ftime(&end);
        float diff = (end.millitm - start.millitm);
        printf("Part %d: %d\tTime: %1.3f\n", i, steps, diff / 1000);
    }
    return 0;
}
