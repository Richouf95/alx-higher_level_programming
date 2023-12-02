#include <Python.h>

/**
 * print_python_list_info - print python list info
 * @p: list
*/

void print_python_list_info(PyObject *p)
{
	int i;
	PyObject *obj;
	int size = Py_SIZE(p);

	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		obj = Py_TYPE(PyList_GetItem(p, i))->tp_name;
		printf("Element %d: %s\n", i, obj);
	}
}
