#include "main.h"

void redirect(char *argv[], char* input, char* output) {
    int ipfd, opfd;
    int status, pid;
    
    if ((pid=fork()) == -1)
        perror("fork failed");
    else if (pid != 0) {
        pid = wait(&status);
    } else {
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
        execvp(argv[0], argv);
    }
}