#include "lists.h"

/**
 * check_cycle - checks whether a singly linked list has a cycle in it
 *
 * @list: linked list being checked
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr = list, *ptr2 = list;

	while (ptr && ptr2 && ptr->next)
	{
		ptr = ptr->next->next;
		ptr2 = ptr2->next;

		if (ptr == ptr2)
			return (1);
	}

	return (0);
}
