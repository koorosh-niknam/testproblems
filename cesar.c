
#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, string argv[])
{

//conditions to check the validity of key

if(argc == 2)
{
    
    // conditions to check whether the given input is digit or not
    
    for(int i = 1; i < argc; i++)
    {
        for(int j = 0, n = strlen(argv[1]); j < n; j++)
        {
            if (isalpha(argv[i][j]) || argv[1][0] == '-')
            {
                
                //condition for checking negative number and letters
                
                printf("Usage: %s key\n",argv[0]);
                return 1;
            }
        }
    }
}
else
{
    printf("Usage: %s key\n",argv[0]);
    return 1;
}
int k = atoi(argv[1]);

//prompt user for input

string p = get_string("plaintext: ");

int len = strlen(p);   //storing length of the input text

printf("ciphertext: ");


//loop to check each character of input text

for(int l = 0; l < len; l++)
{
    
    //checking uppercase letters
    
    if (isupper(p[l]))
    {
        
        //printing uppercase letters (ciphertext)
        
        printf("%c",(((p[l] - 'A') + k) % 26) + 'A');
    }
    
    //checking lowercase letters
    
    else if (islower(p[l]))
    {
        
        //printing lowercase letters (cyphertext)
        
        printf("%c",(((p[l] - 'a') + k) % 26) + 'a');
    }
    else
    {
        
        //printing charcters as it is if it is not alphabet
        
        printf("%c",p[l]);
    }
}
printf("\n");
return 0;

}
