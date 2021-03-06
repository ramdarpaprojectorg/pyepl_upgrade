'''OpenGL extension APPLE.row_bytes

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_APPLE_row_bytes'
_DEPRECATED = False
GL_PACK_ROW_BYTES_APPLE = constant.Constant( 'GL_PACK_ROW_BYTES_APPLE', 0x8A15 )
GL_UNPACK_ROW_BYTES_APPLE = constant.Constant( 'GL_UNPACK_ROW_BYTES_APPLE', 0x8A16 )


def glInitRowBytesAPPLE():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
