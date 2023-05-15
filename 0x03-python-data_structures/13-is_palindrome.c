#include "lists.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - A function that checks if a list is a palindrome
 * @head: The pointer to the head of the list
 * Return: 0 if list not palindrome, 1 if it is
 */

int is_palindrome(listint_t **head)
{
	listint_t *condition = *head;
	int forks = 0, k = 0, *order = NULL;

	if (*head == NULL || head == NULL || (*head)->next == NULL)
		return (1);
	while (condition)
	{
		forks++;
		condition = condition->next;
	}
	order = malloc(sizeof(int) * forks);
	condition = *head;
	while (condition)
	{
		order[k++] = condition->n;
		condition = condition->next;
	}
	for (k = 0; k < forks / 2; k++)
	{
		if (order[k] != order[forks - 1 - k])
		{
			free(order);
			return (0);
		}
	}
	free(order);
	return (1);
}
