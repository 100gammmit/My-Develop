#include "main.h"

void Pipe(char* command1[], char* command2[], int isredir, char *argv[], char* input, char* output) {
    int ipfd, opfd;
    int status, pid;
    int fd[2];
    pipe(fd);

    if (isredir > 0) {
        if ((pid=fork()) == -1)
            perror("fork failed");
        else if(pid == 0){
            if (input != NULL) {
                ipfd = open(input, O_CREAT|O_RDONLY, 0600);
                dup2(ipfd, 0);
                close(ipfd);
            }
            if (output != NULL) {
                opfd = open(output, O_CREAT|O_TRUNC|O_WRONLY, 0600);
                dup2(opfd, 1);
                close(opfd);
            }
            if(fork() == 0) {
                close(fd[0]);
                dup2(fd[1], 1);
                close(fd[1]);
                execvp(command1[0], command1);
                perror("pipe");
                exit(1);
            }

            if(fork() == 0) {
                close(fd[1]);
                dup2(fd[0], 0);
                close(fd[0]);
                execvp(command2[0], command2);
                perror("pipe");
                exit(1);
            }
            close(fd[0]);
            close(fd[1]);
            wait(0);
            wait(0);
        }
    } else {
        if(fork() == 0) {
            close(fd[0]);
            dup2(fd[1], 1);
            close(fd[1]);
            execvp(command1[0], command1);
            perror("pipe");
            exit(1);
        }

        if(fork() == 0) {
            close(fd[1]);
            dup2(fd[0], 0);
            close(fd[0]);
            execvp(command2[0], command2);
            perror("pipe");
            exit(1);
        }
        close(fd[0]);
        close(fd[1]);
        wait(0);
        wait(0);
    }
}