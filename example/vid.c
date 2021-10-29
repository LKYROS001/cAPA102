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
    myFile = fopen("vid.txt", "r");

    //read file into array
    
    //int i;

    if (myFile == NULL){
        printf("Error Reading File\n");
        exit (0);
    }
    int size = 0;
    fscanf(myFile, "%d,", &size);
    int numberArray[size];
  
    for (y = 0; y < size; y++){
        fscanf(myFile, "%d,", &numberArray[y] );
    }
    fclose(myFile);

    int x = 0;
    int i;
    while( time > -1 ){
        if (x > (size-1)){
            x = 0;
        }
        for ( i = 0; i < 72; i++){
            cAPA102_Set_Pixel_4byte(i, numberArray[x]);
            x++;
        }

        cAPA102_Refresh();
       // y++;
        //time++;
        usleep(0.01);
    }

    cAPA102_Clear_All();
    return 0;
}
