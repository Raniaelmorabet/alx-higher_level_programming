i#include <Python.h>
#include <stdio.h>

void print_item_info(PyObject *prmItem, int prmItemIndex)
{
    char *itemName;

    itemName = (char *)Py_TYPE(prmItem)->tp_name;

    printf("Item %d: %s\n", prmItemIndex, itemName);
}

void print_python_tuple_info(PyObject *p)
{
    int itemIndex, objAllocatedNb = 0;
    PyObject *item;
    Py_ssize_t objTupleSize = 0;

    if (PyTuple_Check(p))
    {
        objTupleSize = PyTuple_Size(p);
        objAllocatedNb = ((PyTupleObject *)p)->ob_base.ob_refcnt - 1;

        printf("[*] Size of the Python Tuple = %d\n", (int)objTupleSize);
        printf("[*] Allocated = %d\n", objAllocatedNb);

        for (itemIndex = 0; itemIndex < objTupleSize; itemIndex++)
        {
            item = PyTuple_GetItem(p, itemIndex);
            print_item_info(item, itemIndex);
        }
    }
}
