struct skiplist_node
{
    int key;
    void *data;
    struct node **next_nodes;
};

struct skiplist
{
    int max_level;
    struct skiplist_node *head;
    struct skiplist_node *tail;
};

struct skiplist *skiplist_create(int max_level);
void skiplist_delete(struct skiplist* list);
void skiplist_insert(struct skiplist *list, int key, void *data);
void skiplist_remove(struct skiplist *list, int key);
struct skiplist_node *skiplist_get(struct skiplist *list, int key);