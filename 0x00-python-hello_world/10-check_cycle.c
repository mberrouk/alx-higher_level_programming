#include "lists.h"

/**
 * check-cycle - check if a singly linked list
 * has a cycle in it
 * @list: head of list
 *
 * Return: 0 if there in no cycle, 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp;

	tmp = list;
	while (tmp)
	{
		tmp = tmp->next;
		if (list == tmp)
			return (1);
	}
	return (0);
}
