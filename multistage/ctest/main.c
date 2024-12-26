#include "stdio.h"
#include "stdlib.h"
#include "string.h"

char* ReadLine(void) {
	char* line = NULL;
	size_t buffsize = 0;
	getline(&line, &buffsize, stdin);	
	return line;
}

int main() {
	while(1) {
		char* line = ReadLine();
		printf("%s\n", line);
	}

	return 0;
}
