#include <stdio.h>

int main() {

	int estrelas = 0;
	scanf("%d", &estrelas);
	int carneiros[estrelas];
	int i, total_carneiros = 0, roubados = 0, aux = 0, estrelas_roubadas = 0;

	for (i = 0; i < estrelas; i++) {
		scanf("%d", &carneiros[i]);

		total_carneiros += carneiros[i];
	}

	while (1) {
		if(carneiros[aux] == 0 || aux < 0 || aux >= estrelas)
			break;

		if(aux > estrelas_roubadas)
			estrelas_roubadas = aux;

		roubados += 1;
		if(carneiros[aux] % 2 == 0) {
			carneiros[aux] -= 1;
			aux -= 1;
		} else {
			carneiros[aux] -= 1;
			aux += 1;
		}
	}

	int nao_roubados = total_carneiros - roubados;

	printf("%d %d\n", estrelas_roubadas + 1, nao_roubados);

	return 0;
}