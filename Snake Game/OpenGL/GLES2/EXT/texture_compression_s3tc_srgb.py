'''OpenGL extension EXT.texture_compression_s3tc_srgb

This module customises the behaviour of the 
OpenGL.raw.GLES2.EXT.texture_compression_s3tc_srgb to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds new compressed color texture formats using S3TC with
	nonlinear sRGB color components.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/texture_compression_s3tc_srgb.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.EXT.texture_compression_s3tc_srgb import *
from OpenGL.raw.GLES2.EXT.texture_compression_s3tc_srgb import _EXTENSION_NAME

def glInitTextureCompressionS3TcSrgbEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION