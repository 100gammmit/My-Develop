#include "main.h"
void excute(bool bgexc, char *argv[]){
    int status, pid;

    if ((pid=fork()) == -1)
        perror("fork failed");
    else if (pid != 0) {
        if(bgexc) {
            printf("[1] %d\n", getpid());
        }
        else {
            pid = wait(&status);   
        }
    } else {
        execvp(argv[0], argv);
    }
}