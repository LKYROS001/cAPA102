#include "cAPA102.h"
#include <stdio.h>
#include <stdlib.h>
#include<unistd.h>

int main(int argc, char *argv[]) {
   // int bri = 0;
   // int dir = 0;
    int time = 0;
    cAPA102_Init(72, 0, 0, 5);
    
    int y;
   
    FILE *myFile;
    myFile = fopen("readme.txt", "r");

    //read file into array
    int numberArray[12960];
    //int i;

    if (myFile == NULL){
        printf("Error Reading File\n");
        exit (0);
    }

    for (y = 0; y < 12960; y++){
        fscanf(myFile, "%d,", &numberArray[y] );
    }
    fclose(myFile);

    int track1 = 0;
    int track2 = 180;
    int left = 0;
    int right = 0;
    int i;
    while( time > -1 ){
        if (track1 == 360){
            track1 = 0;
        }
        if (track2 == 360){
            track2 = 0;
        }
        left = track1 * 36 + 36;
        right = track2 * 36 ;
        
        for ( i = 0; i < 36; i++){
            cAPA102_Set_Pixel_4byte(i, numberArray[right]);
            right++;
        }
        //cAPA102_Set_Pixel_RGB(i, 255, 0, 0);
        
        for ( i = 36; i < 72; i++){
            cAPA102_Set_Pixel_4byte(i, numberArray[left]);
            left--;
            
        }
        cAPA102_Refresh();
       // y++;
        //time++;
       track1++;
       track2++;
    }

    cAPA102_Clear_All();
    return 0;
}
