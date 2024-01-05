#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the linked list
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;      /* Moves one step at a time */
		fast = fast->next->next; /* Moves two steps at a time */

        /* If the pointers meet, there is a cycle */
		if (slow == fast)
			return (1);
	}

	return (0); /* No cycle found */
}
