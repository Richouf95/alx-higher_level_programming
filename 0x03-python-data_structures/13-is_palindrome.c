#include "lists.h"

/**
 * check - check if list is palindrome
 * @head: list
 * @current: current node
 * Return: Result
*/

int check(listint_t *head, listint_t **current)
{
	int tail;

	if (head == NULL)
		return (1);

	tail = check(head->next, current);

	if (tail && (*current)->data == head->data)
	{
		*current = (*current)->next;
		return (1);
	}
	else
		return (0);
}

/**
 * is_palindrome - check if list is palindrome
 * @head: list
 * Return: 0 if ok 1 if not ok
*/

int is_palindrome(listint_t **head)
{
	if (*head == NULL || head == NULL)
		return (1);

	return (check(head, *head));
}
