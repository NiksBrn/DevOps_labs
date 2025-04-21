cmake_minimum_required(VERSION 3.10)
project(cw_project C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

# Указываем расположение выходных файлов
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})

# Исходные файлы
set(SOURCE_FILES
    main.c
    DELL.c
    ERROR.c
    find.c
    Input_Sentence.c
    Input_Text.c
    Memory_Cleaning.c
    Replace.c
    Sort_low_cnt_wrd.c
    find_no_reg.c
)

# Заголовочные файлы
set(HEADER_FILES
    DELL.h
    ERROR.h
    find.h
    Input_Sentence.h
    Input_Text.h
    Memory_Cleaning.h
    my_lib.h
    Replace.h
    Sort_low_cnt_wrd.h
    find_no_reg.h
)

# Создаем исполняемый файл
add_executable(cw ${SOURCE_FILES} ${HEADER_FILES})
target_compile_options(cw PRIVATE -g)