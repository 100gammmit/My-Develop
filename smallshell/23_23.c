#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>
#define MAXARG 7

main()
{
    char buf[256];
    char *arg[MAXARG];
    char *s;
    char *save;
    int argi;
    
    static const char delim[] = " \t\n";
    int pid, status;

    
    while(1) {
       printf("myshell$ ");
       gets(buf);
       argi = 0;
       
       s = strtok_r(buf, delim, &save);
      
       while(s) {
          arg[argi++] = s;
          s = strtok_r(NULL, delim, &save);
          
       }
       
       arg[argi] = (char *)0;
       
       if (!strcmp(arg[0], "quit"))
           break;

       if ((pid=fork()) == -1)   
          perror("fork failed");
       
       else if (pid != 0) {
          pid = wait(&status);
       
       } else {
          execvp(arg[0], arg);
       }
    }
    exit(0);
}