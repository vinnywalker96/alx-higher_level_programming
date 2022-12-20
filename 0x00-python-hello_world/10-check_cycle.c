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
	listint_t *slow;
	listint_t *fast;

	if (!list)
		return (0);
	slow = list;
	fast = list->next;

	while (fast && slow && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}



