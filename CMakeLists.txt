PROJECT(conangtest)
cmake_minimum_required(VERSION 2.8)
include(conanbuildinfo.cmake)
CONAN_BASIC_SETUP()
add_subdirectory("./gtest-1.7.0")
