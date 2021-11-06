#include "cAPA102.h"
#include <stdio.h>
#include <stdlib.h>
#include<unistd.h>
//By Ross Lakey
//Program used to display video

int main(int argc, char *argv[]) {

    cAPA102_Init(72, 0, 0, 25); //set number of LEDs and brightness
    
    int y;
   
    FILE *myFile;
    myFile = fopen("vid.txt", "r");//open file

    if (myFile == NULL){
        printf("Error Reading File\n");
        exit (0);
    }
    int size = 0;
    fscanf(myFile, "%d,", &size);// get number of RGB values from first value in the text file
    int numberArray[size]; //give size of array
  
    for (y = 0; y < size; y++){
        fscanf(myFile, "%d,", &numberArray[y] );    //read file into array
    }
    fclose(myFile);

    int x = 0;
    int i;
    while( 1 ){   //loop through array
        if (x > (size-1)){ //If array end has been reached, reset
            x = 0;
        }
        for ( i = 0; i < 72; i++){ //assign each LED a colour
            cAPA102_Set_Pixel_4byte(i, numberArray[x]);
            x++;
        }

        cAPA102_Refresh();//populate LEDs with assigned colour
        usleep(1);// Timing delay
    }

    cAPA102_Clear_All();
    return 0;
}
