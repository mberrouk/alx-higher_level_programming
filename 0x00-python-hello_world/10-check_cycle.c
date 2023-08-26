#include "lists.h"

/**
 * check_cycle - check if a singly linked list
 * has a cycle in it
 * @list: head of list
 *
 * Return: 0 if there in no cycle, 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	slow = list;
	fast = list;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
