#include <stdio.h>
#include "skiplist.h"

int main(int argc, char* args[])
{
    int numbers[] = {3,6,9,2,11,1,4};
    int max_level = 6;
    struct skiplist* list = skiplist_create(max_level);
    printf("insert====================\n");
    for (int i=0; i<sizeof(numbers)/sizeof(numbers[0]); i++)
    {
        skiplist_insert_node(list, numbers[i], numbers[i]);
    }
    skiplist_dump(list);

    printf("search======================\n");
    int keys[] = {3,4,7,10,111};
    for (int i=0; i<sizeof(keys)/sizeof(keys[0]); i++)
    {
        struct skiplist_node *node = skiplist_find_node(list, keys[i]);
        if (node){
            printf("key=%d, value=%d\n", keys[i], node->data);
        } else {
            printf("key=%d, not found\n", keys[i]);
        }
    }

    printf("remove=========================\n");
    skiplist_remove_node(list, 3);
    skiplist_remove_node(list, 9);
    skiplist_dump(list);

    return 0;
}