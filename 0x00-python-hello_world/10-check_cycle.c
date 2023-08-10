#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * Description: traverses a singly linked list and checks
 * if the current node being visited has been visited before
 * update check cycle to use O(n) algorithm
 *
 * @list: pointer to the head of the list
 *
 * Return: 1 if cycle exists and 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *current_node = list, *next_node = list;

	while (next_node != NULL)
	{
		current_node = current_node->next;
		next_node = next_node->next;

		if (next_node == NULL)
			return (0);
		next_node = next_node->next;
		if (next_node == current_node)
			return (1);
	}
	return (0);
}
