#include <Python.h>

/**
 * print_python_list_info - print python list info
 * @p: list
*/

void print_python_list_info(PyObject *p)
{
	int i = 0;
	PyObject *obj;

	printf("
		[*] Size of the Python list = %d\n
		[*] Allocated = %d\n
		", Py_SIZE(p), (PyListObject *)p)->allocated;

	while (i < Py_SIZE(p))
	{
		obj = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
		i++
	}
}
