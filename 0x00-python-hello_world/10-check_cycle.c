#include "lists.h"

/**
 * check_cycle - check if list has cycle
 * @list: the list
 * Return: 0 if ok 1 if not
*/

int check_cycle(listint_t *list)
{
	listint_t *node;
	listint_t *nextNode;

	if (list == NULL || list->next == NULL)
		return (0);

	node = nextNode = list;

	while (node != NULL && nextNode != NULL && nextNode != NULL)
	{
		if (node != nextNode)
		{
			nextNode = nextNode->next->next;
			node = node->next;
		}
		else
			return (1);
	}

	return (0);
}
