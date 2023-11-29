#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - insert node
 * @head: list
 * @number: new item
 * Return: result
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	while (tmp->next)
		tmp = tmp->next;

	tmp->next = new;

	return (new);
}
