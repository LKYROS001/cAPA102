#include "cAPA102.h"
#include <stdio.h>
#include <stdlib.h>
#include<unistd.h>
#include <time.h>
//By Ross Lakey
//Program used to test LED image assignment and timing

int main(int argc, char *argv[]) {

    cAPA102_Init(72, 0, 0, 15); //set number of LEDs and brightness
    
    int y;
   
    FILE *myFile;
    myFile = fopen("readme.txt", "r");//open file

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

    int x = 0; //array counter
    int i; //pixel counter
   
    time_t times = 0; //initial time 
    time_t diff = 0;//fnishing time
    
    while( 1 ){//loop through array
        if (x > 25840){//If array end has been reached, reset
            x = 0;
        }
        times = clock(); //get initial time
        for ( i = 0; i < 72; i++){  //assign each LED a colour
            cAPA102_Set_Pixel_4byte(i, numberArray[x]);
            x++;
        }
        cAPA102_Refresh(); //populate LEDs with assigned colour
        diff = clock(); //get finishing time
        printf("Timestamp: %f\n",difftime(diff, times)/CLOCKS_PER_SEC); //print time taken to display row of LEDs
       //No timing delay as max speed of LED changes are being tested
    }

    cAPA102_Clear_All();
    return 0;
}
