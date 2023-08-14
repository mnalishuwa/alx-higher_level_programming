#include "lists.h"

/**
 * is_palindrome - checks if a list is a palindrome
 * Description: checks if a singly linked list is
 * is a palindrome
 *
 * @head: first node in list
 *
 * Return: int, 0 if not palindrome 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	size_t size_l = list_len(*head), i, start = 0;
	int *list_data, result;
	listint_t *current_node = *head;

	if (head == NULL || size_l == 0)
		return (1);
	list_data = malloc(sizeof(int) * size_l);

	for (i = 0; i < size_l; i++)
	{
		*(list_data + i) = current_node->n;
		current_node = current_node->next;
	}

	size_l = size_l - 1;
	result = is_pal_helper(list_data, start, size_l);
	free(list_data);

	return (result);
}

/**
 * is_pal_helper - recursively check is an array is a palindrome
 * Description: takes an array of integers and checks if it is a
 * palindrome
 *
 * @a: int array
 * @st: start index, int
 * @end: end index of array containing data
 *
 * Return: int 1 if palindrome, 0 otherwise
 */
int is_pal_helper(int *a, size_t st, size_t end)
{
	if (st >= end)
		return (1);

	return ((*(a + st) == *(a + end)) && is_pal_helper(a, st + 1, end - 1));
}

/**
 * list_len - return number of elements in a list
 * Description: count the number of elements in a linked list
 *
 * @h: pointer to list head
 *
 * Return: size_t, number of elements
 */
size_t list_len(listint_t *h)
{
	size_t size_l = 0;
	listint_t *cur_node = h;

	while (cur_node)
	{
		size_l++;
		cur_node = cur_node->next;
	}
	return (size_l);
}
