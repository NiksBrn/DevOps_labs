#include <iostream>
#include <string>

int main() {
    std::string name;
    int age;

    std::cout << "Введите ваше имя: ";
    std::getline(std::cin, name);

    std::cout << "Введите ваш возраст: ";
    std::cin >> age;

    std::cout << "Привет, " << name << "! Вам " << age << " лет." << std::endl;

    return 0;
}
