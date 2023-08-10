#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * Description: traverses a singly linked list and checks
 * if the current not being visited has been visited before
 *
 * @list: pointer to the head of the list
 *
 * Return: 1 if cycle exists and 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *current_node = NULL, *temp = NULL;
	int index, j;

	current_node = list;
	index = 0;
	while (current_node)
	{
		current_node = current_node->next;
		index += 1;
		temp = list;
		while (temp && j < index)
		{
			if (temp == current_node)
			{
				return (1);
			}
			j++;
		}
	}
	return (0);
}
