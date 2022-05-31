#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 *
 * @head: pointer to the pointer of the first node of listint_t list
 * @number: number to be inserted in the new node
 *
 * Return: pointer to the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *new_node;

	temp = *head;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;

		return (new_node);
	}

	while (temp->next != NULL)
	{
		if ((temp->next)->n >= number)
		{
			new_node->next = temp->next;
			temp->next = new_node;

			return (new_node);
		}

		temp = temp->next;
	}

	new_node->next = NULL;
	temp->next = new_node;

	return (new_node);
}
