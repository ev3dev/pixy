cmake_minimum_required (VERSION 2.8)

add_subdirectory (src/host/libpixyusb)
add_subdirectory (src/host/libpixyusb_swig)

# PixyMon - using qmake build system

set (PIXYMON_DIR ${CMAKE_BINARY_DIR}/pixymon_qmake)
add_custom_command (OUTPUT ${PIXYMON_DIR}
    COMMAND mkdir -p ${PIXYMON_DIR}
}
)
add_custom_target (pixymon ALL
    COMMAND qmake-qt4 ${CMAKE_SOURCE_DIR}/src/host/pixymon/pixymon.pro
    COMMAND make -w
    WORKING_DIRECTORY ${PIXYMON_DIR}
    DEPENDS ${PIXYMON_DIR}
)
install (FILES ${PIXYMON_DIR}/PixyMon DESTINATION bin)
