#include "cAPA102.h"
#include <stdio.h>
#include <stdlib.h>
#include<unistd.h>

int main(int argc, char *argv[]) {
   // int bri = 0;
   // int dir = 0;
    int time = 0;
    cAPA102_Init(72, 0, 0, 25);
    
    int y;
   
    FILE *myFile;
    myFile = fopen("readme.txt", "r");

    //read file into array
    int numberArray[25920];
    //int i;

    if (myFile == NULL){
        printf("Error Reading File\n");
        exit (0);
    }

    for (y = 0; y < 25920; y++){
        fscanf(myFile, "%d,", &numberArray[y] );
    }
    fclose(myFile);

    int x = 0;
    int i;
    int diff = 0;
    while( true ){
        if (x > 25840){
            x = 0;
        }
        time = (int)(time());
        for ( i = 0; i < 72; i++){
            cAPA102_Set_Pixel_4byte(i, numberArray[x]);
            x++;
        }
        diff = (int)(time()) - time;
        printf("Timestamp: %d\n",diff);
        cAPA102_Refresh();
       // y++;
        //time++;
        //usleep(10000);
        //usleep(0.01);
    }

    cAPA102_Clear_All();
    return 0;
}
