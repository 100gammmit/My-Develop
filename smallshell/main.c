#include "main.h"
#define MAXARG 7

main()
{
    char buf[256];
    char *arg[MAXARG], *args[MAXARG], *pipe_arg1[MAXARG], *pipe_arg2[MAXARG];
    char *s, *save;
    char input[20] = "", output[20] = "";
    int argi, i, j, num_args, m, pipe_bif;
    bool bgexc, ispipe;
    
    static const char delim[] = " \t\n";
    int pid, status;
    
    while(1){
        memset(buf, NULL, 256);
        printf("myshell$ ");
        gets(buf);

        if(buf[0] == NULL)
            break;

        if (strchr(buf, ';') != NULL) {
            num_args = Token_Split(buf, args, ";");
        } else {
            args[0] = buf;
            args[1] = (char *)0;
            num_args = 1;
        }
        
        for(i=0; i<num_args; i++){
            m=0;
            bgexc = false;
            ispipe = false;
            argi = 0;
            s = strtok_r(args[i], delim, &save);
            while(s) {
                if (strchr(s, '(') != NULL) s++;
                if (strchr(s, ')') != NULL) s--;

                if (strcmp(s, "|") == 0) {
                    ispipe = true;
                    for (j =0; j < argi; j++) {
                        pipe_arg1[j] =  arg[j];
                    }
                    pipe_arg1[argi] = (char *)0;
                    pipe_bif = argi;
                }
                else if (strcmp(s, "<") == 0) m = 1;
                else if (strcmp(s, ">") == 0) m = 2;
                else if (strcmp(s, "&") == 0) bgexc = true;
                else {
                    if (m == 1) strcpy(input, s);
                    else if (m == 2) strcpy(output, s);
                    else arg[argi++] = s;
                }

                s = strtok_r(NULL, delim, &save);
            }
            arg[argi] = (char *)0;
            if(ispipe) {
                for (j =0; j < argi-pipe_bif; j++) {
                    pipe_arg2[j] =  arg[j+pipe_bif];
                }
                pipe_arg2[argi-pipe_bif] = (char *)0;
                Pipe(pipe_arg1, pipe_arg2, m, arg, input, output);
            } else if(m == 1 || m == 2) {
                redirect(arg, input, output);  
            } else {
                excute(bgexc, arg);
            }            
        }
    }
    exit(0);
}