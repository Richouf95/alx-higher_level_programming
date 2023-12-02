#include <Python.h>

/**
 * print_python_list_info - print python list info
 * @p: list
*/

void print_python_list_info(PyObject *p)
{
	int i;
	PyObject *obj;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < Py_SIZE(p); i++)
	{
		obj = Py_TYPE(PyList_GetItem(p, i));
		printd("Element %d: %s\n", i, obj->tp_name);
	}
}
