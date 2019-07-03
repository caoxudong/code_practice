#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>
#include "skiplist.h"

static int random_level(int max_level)
{
    while (rand() < RAND_MAX / 2 && max_level < max_level)
    {
        max_level++;
    }
    return max_level;
}

static void free_skiplist_node(struct skiplist_node *node)
{
    if (node)
    {
        free(node->next_nodes);
        free(node);
    }
}

struct skiplist *skiplist_create(int max_level)
{
    srand(time(NULL));
    if (max_level <= 0)
    {
        max_level = 1;
    }

    struct skiplist *list = (struct skiplist *)malloc(sizeof(struct skiplist));
    list->max_level = max_level;

    struct skiplist_node *head = (struct skiplist_node *)malloc(sizeof(struct skiplist_node));
    list->head = head;

    head->key = INT_MAX;
    head->next_nodes = (struct skiplist_node **)malloc(max_level * sizeof(struct skiplist_node *));
    for (int i = 0; i < max_level; i++)
    {
        head->next_nodes[i] = head;
    }

    return list;
}

void skiplist_delete(struct skiplist *list)
{
    struct skiplist_node *update[list->max_level - 1];
    struct skiplist_node *node = list->head;
    struct skiplist_node *head = list->head;
    int max_level = list->max_level;

    while (node->next_nodes[0] != head) {
        struct skiplist_node *temp = node->next_nodes[0];
        free_skiplist_node(node);
        node = temp;
    }

    free_skiplist_node(head);
    free(list);
}

void skiplist_insert_node(struct skiplist *list, int key, void *data)
{
    struct skiplist_node *update[list->max_level];
    struct skiplist_node *node = list->head;
    for (int i = list->max_level - 1; i >= 0; i--)
    {
        while (node->next_nodes[i]->key < key)
        {
            node = node->next_nodes[i];
        }
        update[i] = node;
    }
    node = node->next_nodes[0];

    if (node->key == key)
    {
        node->data = data;
        return;
    }

    int new_node_level = random_level(list->max_level);
    node = (struct skiplist_node *)malloc(sizeof(struct skiplist_node));
    node->key = key;
    node->data = data;
    node->next_nodes = (struct skiplist_node **)malloc(sizeof(struct skiplist_node *) * list->max_level);
    for (int i = 0; i < new_node_level; i++)
    {
        node->next_nodes[i] = update[i]->next_nodes[i];
        update[i]->next_nodes[i] = node;
    }
    return;
}

void skiplist_remove_node(struct skiplist *list, int key)
{
    struct skiplist_node *update[list->max_level];
    struct skiplist_node *node = list->head;
    for (int i = list->max_level - 1; i >= 0; i--)
    {
        while (node->next_nodes[i]->key < key)
        {
            node = node->next_nodes[i];
        }
        update[i] = node;
    }

    node = node->next_nodes[0];
    if (node->key == key)
    {
        for (int i = 0; i < list->max_level - 1; i++)
        {
            if (update[i]->next_nodes[i] != node)
            {
                break;
            }
            update[i]->next_nodes[i] = node->next_nodes[i];
        }
        free_skiplist_node(node);
        while ((list->max_level > 1) && (list->head->next_nodes[list->max_level - 1] == list->head))
        {
            list->max_level--;
        }
    }
}

struct skiplist_node *skiplist_find_node(struct skiplist *list, int key)
{
    struct skiplist_node *node = list->head;
    int max_level = list->max_level;

    for (int i = max_level - 1; i >= 0; i--)
    {
        while (node->next_nodes[i]->key < key)
        {
            node = *(node->next_nodes + i);
        }
    }

    if (node->next_nodes[0]->key == key)
    {
        return node->next_nodes[0];
    }
    else
    {
        return NULL;
    }
}

void skiplist_dump(struct skiplist *list)
{
    struct skiplist_node *node = list->head;
    for (int i=0; i<list->max_level; i++)
    {
        while (node && node->next_nodes[i] != list->head)
        {
            printf("%d[%d]->", node->next_nodes[i]->key, node->next_nodes[i]->data);
            node = node->next_nodes[i];
        }
        printf("NIL\n");
    }
}