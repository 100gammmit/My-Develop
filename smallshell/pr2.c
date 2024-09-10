#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/sem.h>

void repeat(int semid);
void p(int semid);
void v(int semid);

/* union semun {
   int val;
   struct semid_ds *buf;
   unsigned short int *array;
} arg; */

main()
{
    int semid, i;
    union semun {
       int val;
       struct semid_ds *buf;
       unsigned short int *array;
    } arg;

    /* ������ 1���� 1234 Ű�� ������� ���� �� */
    if((semid=semget((key_t)4045, 1, IPC_CREAT|0666)) == -1) {
       perror("semget failed");
       exit(1);
    }

    /* ������� ���� 1�� ����: 1 resources of the same type */
    arg.val = 1;
    if(semctl(semid, 0, SETVAL, arg) == -1) {
       perror("semctl failed");
       exit(1);
    }

    /* 3���� �ڽ� ���μ��� �� */
    for(i=0; i<3; i++) {
       if(!fork())
          repeat(semid);
    }

    /* parent process: 10�ʰ� ���� */
    sleep(10);
    printf("parent process %d\n", getpid());
    /* semid ������� ���� */
    if(semctl(semid, 0, IPC_RMID, arg) == -1) {
       perror("semctl failed");
       exit(1);
    }
    exit(0);
}

/* called by children process */
void repeat(int semid)
{
    /* ���� �ʱ�ȭ�ϱ� */
    srand((unsigned int)getpid());
    printf("process %d is trying to access critical section and acquire a resource\n", getpid());

    p(semid);
    /* critical section starts here */
    /* getpid()�� ���� ���μ����� ���μ��� ID�� ��ȯ */
    printf("process %d enters critical section and is using a resource,\n", getpid());
/*    printf("semval = %d\n", arg.buf->sem_base->semval); */

    /* ���� 5�� ���� ������ �� ���� ���� */
    sleep(rand()%5);

    /* critical section ends here */
    v(semid);
    printf("process %d exits critical section and returned a resource\n", getpid());
    exit(0);
}

/* request a resource */
void p(int semid)
{
    struct sembuf pbuf;
    pbuf.sem_num = 0;
    pbuf.sem_op = -1;
    /* ���μ��� �����ϸ� ������� ���� ��� ���� */
    pbuf.sem_flg = SEM_UNDO;
    /* ���� ������� ���� semval 1 �����ϱ� */
    if(semop(semid, &pbuf, 1) == -1) {
       perror("semop failed");
       exit(1);
    }
}

/* release a resource */
void v(int semid)
{
    struct sembuf vbuf;
    vbuf.sem_num = 0;
    vbuf.sem_op = 1;
    vbuf.sem_flg = SEM_UNDO;
    /* ���� ������� ���� semval 1 ���ϱ� */
    if(semop(semid, &vbuf, 1) == -1) {
       perror("semop failed");
       exit(1);
    }
}