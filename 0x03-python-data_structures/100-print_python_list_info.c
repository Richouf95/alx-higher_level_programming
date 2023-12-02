#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - print python list info
 * @p: list
*/

void print_python_list_info(PyObject *p)
{
	int i = 0;

	printf("
		[*] Size of the Python list = %lu\n
		[*] Allocated = %lu\n
		", Py_SIZE(p), ((PyListObject *)p)->allocated);

	while (i < Py_SIZE(p))
	{
		printf("Element %d : %s\n", i, Py_Type(PyList_GetItem(p, elem))->tp_name)
		i++
	}
}
