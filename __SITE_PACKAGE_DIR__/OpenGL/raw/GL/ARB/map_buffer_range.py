'''OpenGL extension ARB.map_buffer_range

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_map_buffer_range'
_DEPRECATED = False
GL_MAP_READ_BIT = constant.Constant( 'GL_MAP_READ_BIT', 0x1 )
GL_MAP_WRITE_BIT = constant.Constant( 'GL_MAP_WRITE_BIT', 0x2 )
GL_MAP_INVALIDATE_RANGE_BIT = constant.Constant( 'GL_MAP_INVALIDATE_RANGE_BIT', 0x4 )
GL_MAP_INVALIDATE_BUFFER_BIT = constant.Constant( 'GL_MAP_INVALIDATE_BUFFER_BIT', 0x8 )
GL_MAP_FLUSH_EXPLICIT_BIT = constant.Constant( 'GL_MAP_FLUSH_EXPLICIT_BIT', 0x10 )
GL_MAP_UNSYNCHRONIZED_BIT = constant.Constant( 'GL_MAP_UNSYNCHRONIZED_BIT', 0x20 )
glMapBufferRange = platform.createExtensionFunction( 
'glMapBufferRange',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=ctypes.c_void_p, 
argTypes=(constants.GLenum,constants.GLintptr,constants.GLsizeiptr,constants.GLbitfield,),
doc='glMapBufferRange(GLenum(target), GLintptr(offset), GLsizeiptr(length), GLbitfield(access)) -> ctypes.c_void_p',
argNames=('target','offset','length','access',),
deprecated=_DEPRECATED,
)

glFlushMappedBufferRange = platform.createExtensionFunction( 
'glFlushMappedBufferRange',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLintptr,constants.GLsizeiptr,),
doc='glFlushMappedBufferRange(GLenum(target), GLintptr(offset), GLsizeiptr(length)) -> None',
argNames=('target','offset','length',),
deprecated=_DEPRECATED,
)


def glInitMapBufferRangeARB():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
