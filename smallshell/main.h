#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdbool.h>
#include <fcntl.h>
int Token_Split(char buff[], char* arg[] ,char delim[]);
void excute(bool isbg, char *argv[]);
void redirect(char *argv[], char* input, char * output);
void Pipe(char* command1[], char* command2[], int isredir, char *argv[], char* input, char* output);