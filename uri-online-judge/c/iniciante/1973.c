#include <stdio.h>

int main() {

	long long int estrelas = 0;
	scanf("%lld", &estrelas);
	long long int carneiros[estrelas];
	long long int i, total_carneiros = 0, roubados = 0, estrelas_roubadas = 0;

	for (i = 0; i < estrelas; i++) {
		scanf("%lld", &carneiros[i]);
		total_carneiros += carneiros[i];
	}

	i = 0;
	while (1) {
		if(i < 0 || i >= estrelas)
			break;

		if(i > estrelas_roubadas)
			estrelas_roubadas = i;

		if(carneiros[i] % 2 == 0) {
			if(carneiros[i] > 0) {
				roubados++;
				carneiros[i]--;
			}
			i--;
		} else {
			if(carneiros[i] > 0) {
				roubados++;
				carneiros[i]--;
			}
			i++;
		}
	}

	printf("%lld %lld\n", estrelas_roubadas + 1, total_carneiros - roubados);

	return 0;
}