#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
  * check_cycle -checks if a singly linked list has a cycle in it.
  * @list: head node
  * Return: 0 or 1
  */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow != fast)
	{
		if (fast == NULL || fast->next == NULL)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
