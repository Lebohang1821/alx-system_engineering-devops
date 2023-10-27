#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>

/**
 * infinite_while - It runs infinite while loop.
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - It creates five zombie processes
 *
 * Return: 0.
 */
int main(void)
{
	pid_t _pid;
	char x = 0;

	while (x < 5)
	{
		_pid = fork();
		if (_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", _pid);
			sleep(1);
			x++;
		}
		else
			exit(0);
	}

	infinite_while();

	return (EXIT_SUCCESS);
}
