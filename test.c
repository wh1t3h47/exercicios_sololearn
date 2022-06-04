#include <stdio.h>
#include <errno.h>

char user_input[256];
int input_num;

int main(int argc, char * argv[]) {
	if (fgets(user_input, sizeof(user_input), stdin)) {
		if (1 == sscanf(user_input, "%d", &input_num)) {
			int *x = &input_num;

			if ((*x % 2) == 0) {
				printf("O número %d é par", *x);
				return 0;
			} // else
			printf("O número %d é impar", *x);
			return 0;
		}
	}

	// error
	errno = EINVAL;
	return 1;
}

