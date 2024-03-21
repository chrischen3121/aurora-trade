cmake_minimum_required(VERSION 3.14)
project(MarketDataService VERSION 0.1.0 LANGUAGES CXX)

# set C++ standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find ZeroMQ Library
find_package(cppzmq REQUIRED)

# Find Protobuf Library
find_package(Protobuf REQUIRED)

# Set the build type to Release if not specified
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

add_subdirectory(src)
add_subdirectory(tests)
