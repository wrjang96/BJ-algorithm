#include <stdio.h>
#include <math.h>
#pragma warning(disable:4996)

int main(void)
{
    int testcode, x1, y1, r1, x2, y2, r2, result;
    double distanse, subtract;    //거리, 뺄셈
    scanf("%d", &testcode);

    while (testcode--)
    {
        scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
        distanse = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));   
        subtract = r1 > r2 ? r1 - r2 : r2 - r1;

        if (distanse == 0 && r1 == r2) result = -1;   
        else if (distanse < r1 + r2 && (subtract < distanse)) result = 2;  
        else if (distanse == r1 + r2 || distanse == subtract) result = 1;    
        else result = 0;    

        printf("%d\n", result);
    }
}
