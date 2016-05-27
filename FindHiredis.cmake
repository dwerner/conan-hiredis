# Try to find hiredis
# Once done, this will define
#
# HIREDIS_FOUND        - system has hiredis
# HIREDIS_INCLUDE_DIRS - hiredis include directories
# HIREDIS_LIBRARIES    - libraries need to use hiredis

find_path(
	HIREDIS_INCLUDE_DIR
	NAMES hiredis.h
	PATHS ${CONAN_INCLUDE_DIRS_HIREDIS}
	)

find_library(
	HIREDIS_LIBRARY
	NAMES hiredis
	PATHS ${CONAN_LIB_DIRS_HIREDIS}
	)

set(HIREDIS_FOUND TRUE)
set(HIREDIS_INCLUDE_DIRS ${HIREDIS_INCLUDE_DIR})
set(HIREDIS_LIBRARIES ${HIREDIS_LIBRARY})

mark_as_advanced(HIREDIS_LIBRARY HIREDIS_INCLUDE_DIR)
