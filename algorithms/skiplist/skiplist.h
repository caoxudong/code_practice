struct skiplist_node
{
    int key;
    void *data;
    struct skiplist_node **next_nodes;
};

struct skiplist
{
    int max_level;
    struct skiplist_node *head;
};

struct skiplist *skiplist_create(int max_level);
void skiplist_delete(struct skiplist* list);
void skiplist_dump(struct skiplist *list);
void skiplist_insert_node(struct skiplist *list, int key, void *data);
void skiplist_remove_node(struct skiplist *list, int key);
struct skiplist_node *skiplist_find_node(struct skiplist *list, int key);
