float sum(struct lista *a);

void print(struct lista *a);

float average(struct lista *a);

struct lista* map(struct lista *a, struct dato (*f)(struct dato));
