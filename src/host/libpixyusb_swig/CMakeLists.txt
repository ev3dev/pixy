configure_file (setup.py.in setup.py @ONLY)
add_custom_command (OUTPUT
        ${CMAKE_CURRENT_BINARY_DIR}/pixy_wrap.cxx
        ${CMAKE_CURRENT_BINARY_DIR}/pixy.py
    COMMAND swig
        -c++
        -python
        -o ${CMAKE_CURRENT_BINARY_DIR}/pixy_wrap.cxx
        -outdir ${CMAKE_CURRENT_BINARY_DIR}
        ${CMAKE_CURRENT_SOURCE_DIR}/pixy.i
    DEPENDS
        pixy.i
)
add_custom_target (libpixyusb_swig ALL
    COMMAND pybuild
        --build
        --dir=${CMAKE_CURRENT_BINARY_DIR}
    DEPENDS
        ${CMAKE_CURRENT_BINARY_DIR}/pixy_wrap.cxx
        ${CMAKE_CURRENT_BINARY_DIR}/pixy.py
        ${CMAKE_CURRENT_BINARY_DIR}/setup.py
)
install (CODE "execute_process (COMMAND pybuild --install --dir=${CMAKE_CURRENT_BINARY_DIR})")
