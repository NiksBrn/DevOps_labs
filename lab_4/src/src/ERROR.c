#include "my_lib.h"

void error(int i){
    switch (i){
    case 1:
        //����� ����������� ����� �������, ���������� ��������� �����������
        wprintf(L"Error: an incorrect command number has been entered, and the program has been stopped");
        break;
    case 2:
        //������ ��� ��������� ��� ������������� ������, ���������� ��������� �����������
        wprintf(L"Error: an error occurred when allocating or overallocating memory, the program execution was stopped");
        break;
    case 3:
        wprintf(L"Error: the text is empty, the program execution was stopped");
        break;
    }
    exit(0);
}
