#include "lists.h"

/**
 * check_cycle - checks if a fail link is circular or not
 * @list: linked list to check
 * Return: 1(circular) 0(no loop detected)
 */

int check_cycle(listint_t *list)
{
	listint_t *k1 = NULL, *k2 = NULL;

	k1 = k2 = list;
	while (list && k1 && k2 && k1->next && k2->next)
	{
		k1 = k1->next;
		k2 = k2->next->next;
		if (!k2 || !k1)
			return (0);
		if (k2->next == k2)
			return (1);
	}
	return (0);
}
