#include "lists.h"

/**
 * lst_size - count nodes in a linked list
 * @head: pointer to the head node
 *
 * Return: length of linked list
 */
int lst_size(listint_t *head)
{
	int len;

	len = 0;
	while (head)
	{
		len++;
		head = head->next;
	}
	return (len);
}

/**
 * revers_list - reverse a linked list
 * @head: pointer to head node
 *
 * Return: a pointer to a head
 */
listint_t *revers_list(listint_t **head)
{
	listint_t *tmp;
	listint_t *next;
	listint_t *prev;

	tmp = *head;
	prev = NULL;
	next = NULL;
	while (tmp)
	{
		next = tmp->next;
		tmp->next = prev;
		prev = tmp;
		tmp = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0 else 0.
 */
int is_palindrome(listint_t **head)
{
	int size;
	int i;
	listint_t *tmp;
	listint_t *mid;
	listint_t *h;


	if (!head || !*head || !(*head)->next)
		return (0);
	tmp = *head;
	size = lst_size(tmp);
	i = 0;
	while (i < (size / 2) - 1)
	{
		i++;
		tmp = tmp->next;
	}
	if (!(size % 2) && tmp->n != tmp->next->n)
		return (0);
	tmp = tmp->next;
	mid = revers_list(&tmp);
	tmp = *head;
	h = mid;
	while (h)
	{
		if (h->n != tmp->n)
			return (0);
		h = h->next;
		tmp = tmp->next;
	}
	revers_list(&mid);
	return (1);

}
