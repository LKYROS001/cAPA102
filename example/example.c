#include "cAPA102.h"
#include <stdio.h>
#include<unistd.h>

int main(int argc, char *argv[]) {
    int bri = 0;
    int dir = 0;
    int time = 0;
    cAPA102_Init(72, 0, 0, 5);
    int i;
    int y;
    while( time < 1000000 ){
        if (y == 360){
            printf("YESSS \n");
        }
        for ( i = 0; i < 72; i++)
            cAPA102_Set_Pixel_4byte(i, 16711680);
        //cAPA102_Set_Pixel_RGB(i, 255, 0, 0);
        cAPA102_Refresh();
        
        for ( i = 0; i < 72; i++)
            cAPA102_Set_Pixel_4byte(i, 0);
        cAPA102_Refresh();
       
        y++;
        time++;
    }

    cAPA102_Clear_All();
    return 0;
}
