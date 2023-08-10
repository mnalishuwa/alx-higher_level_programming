#include "lists.h"

int check_cycle(listint_t *list)
{
	listint *current_node = list, *next_node = list;

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
