#include <stdio.h>
#include "skiplist.h"

struct skiplist *skiplist_create(int max_level) 
{
    if (max_level <= 0)
    {
        max_level = 1;
    }
    struct skiplist_node *head = malloc(sizeof (struct skiplist_node));
    struct skiplist_node *tail = malloc(sizeof (struct skiplist_node));
    struct skiplist *list = malloc(sizeof(struct skiplist));
    list->head = head;
    list->tail = tail;
    list->max_level = max_level;

    head->next_nodes = malloc(max_level * sizeof(struct skiplist_node*));
    for (int i=0; i<max_level; i++)
    {
        head->next_nodes[i] = tail;
    }

    return list;
}

void skiplist_delete(struct skiplist* list)
{
    struct skiplist_node *head = list->head;
    struct skiplist_node *tail = list->tail;
    int max_level = list->max_level;

    struct skiplist_node *node = head->next_nodes[0];
    while (node != tail)
    {
        struct skiplist_node *temp = node->next_nodes[0];
        free(node->next_nodes);
        free(node);
        node = temp;
    }

    free(head);
    free(head->next_nodes);
    free(tail);
    free(tail->next_nodes);
    free(list);
}

void skiplist_insert(struct skiplist *list, int key, void *data)
{
    struct skiplist_node *head = list->head;
    struct skiplist_node *current = head;
}

void skiplist_remove(struct skiplist *list, int key)
{
    
}

struct skiplist_node *skiplist_get(struct skiplist *list, int key)
{

}
