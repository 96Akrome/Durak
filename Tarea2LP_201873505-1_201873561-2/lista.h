//structs mal escritos en pdf. preguntar o hacer typedef.
struct nodo{
  struct dato info;
  struct nodo* next;
}algo1;

struct lista{
  struct nodo* actual;
  struct nodo* head;
  struct nodo* tail;
  int length;
}algo2;

struct dato{
  void* contenido;
  char tipo;
}algo3;

void init(struct lista *a);
void clear(struct lista *a);
void insert(struct lista *a,int i,dato d);
void append(struct lista *a, dato d);
void remove(struct lista *a,int i);
int length(struct lista *a);
dato* at(struct lista *a,int i);
