#include "Python.h"
#include <stdlib.h>

/**
 * print_python_list_info - A function that prints information
 * about a python list object
 * @p: The pointer to generic pyObject which is PyListObject type
 * Return: Nothing
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *py_file = NULL;
	size_t range = 0, k;
	const char *py_sort = NULL;

	range = PyList_Size(p);
	py_file = (PyListObject *)p;
	printf("[*] size of the Python List = %ld\n", range):
		printf("[*] Allocated = %ld\n", (signed long)(py_file->allocated));
	for (k = 0; k < range; k++)
	{
		py_sort = PY_TYPE(py_file->ob_item[k])->tp_name;
		printf("Element %ld: %s\n", k, py_file);
	}

}
