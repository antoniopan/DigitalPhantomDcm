# .\volume_phantom.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2023-06-11 01:20:22.302156 by PyXB version 1.2.6 using Python 3.7.8.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:14aaef88-07b3-11ee-8b7e-ec5c682b06ac')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type volumePhantomType with content type ELEMENT_ONLY
class volumePhantomType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type volumePhantomType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'volumePhantomType')
    _XSDLocation = pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 5, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element origin uses Python identifier origin
    __origin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'origin'), 'origin', '__AbsentNamespace0_volumePhantomType_origin', False, pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 7, 3), )

    
    origin = property(__origin.value, __origin.set, None, None)

    
    # Element dimension uses Python identifier dimension
    __dimension = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dimension'), 'dimension', '__AbsentNamespace0_volumePhantomType_dimension', False, pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 8, 3), )

    
    dimension = property(__dimension.value, __dimension.set, None, None)

    
    # Element cube uses Python identifier cube
    __cube = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cube'), 'cube', '__AbsentNamespace0_volumePhantomType_cube', True, pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 9, 3), )

    
    cube = property(__cube.value, __cube.set, None, None)

    
    # Element cylinder uses Python identifier cylinder
    __cylinder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cylinder'), 'cylinder', '__AbsentNamespace0_volumePhantomType_cylinder', True, pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 10, 3), )

    
    cylinder = property(__cylinder.value, __cylinder.set, None, None)

    
    # Element ellipsoid uses Python identifier ellipsoid
    __ellipsoid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ellipsoid'), 'ellipsoid', '__AbsentNamespace0_volumePhantomType_ellipsoid', True, pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 11, 3), )

    
    ellipsoid = property(__ellipsoid.value, __ellipsoid.set, None, None)

    
    # Element sphere uses Python identifier sphere
    __sphere = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sphere'), 'sphere', '__AbsentNamespace0_volumePhantomType_sphere', True, pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 12, 3), )

    
    sphere = property(__sphere.value, __sphere.set, None, None)

    
    # Attribute dim_x uses Python identifier dim_x
    __dim_x = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dim_x'), 'dim_x', '__AbsentNamespace0_volumePhantomType_dim_x', pyxb.binding.datatypes.int, required=True)
    __dim_x._DeclarationLocation = pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 14, 2)
    __dim_x._UseLocation = pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 14, 2)
    
    dim_x = property(__dim_x.value, __dim_x.set, None, None)

    
    # Attribute dim_y uses Python identifier dim_y
    __dim_y = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dim_y'), 'dim_y', '__AbsentNamespace0_volumePhantomType_dim_y', pyxb.binding.datatypes.int, required=True)
    __dim_y._DeclarationLocation = pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 15, 2)
    __dim_y._UseLocation = pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 15, 2)
    
    dim_y = property(__dim_y.value, __dim_y.set, None, None)

    
    # Attribute dim_z uses Python identifier dim_z
    __dim_z = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dim_z'), 'dim_z', '__AbsentNamespace0_volumePhantomType_dim_z', pyxb.binding.datatypes.int, required=True)
    __dim_z._DeclarationLocation = pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 16, 2)
    __dim_z._UseLocation = pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 16, 2)
    
    dim_z = property(__dim_z.value, __dim_z.set, None, None)

    _ElementMap.update({
        __origin.name() : __origin,
        __dimension.name() : __dimension,
        __cube.name() : __cube,
        __cylinder.name() : __cylinder,
        __ellipsoid.name() : __ellipsoid,
        __sphere.name() : __sphere
    })
    _AttributeMap.update({
        __dim_x.name() : __dim_x,
        __dim_y.name() : __dim_y,
        __dim_z.name() : __dim_z
    })
_module_typeBindings.volumePhantomType = volumePhantomType
Namespace.addCategoryObject('typeBinding', 'volumePhantomType', volumePhantomType)


# Complex type pointType with content type EMPTY
class pointType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type pointType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pointType')
    _XSDLocation = pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 18, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute x uses Python identifier x
    __x = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'x'), 'x', '__AbsentNamespace0_pointType_x', pyxb.binding.datatypes.float, required=True)
    __x._DeclarationLocation = pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 19, 2)
    __x._UseLocation = pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 19, 2)
    
    x = property(__x.value, __x.set, None, None)

    
    # Attribute y uses Python identifier y
    __y = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'y'), 'y', '__AbsentNamespace0_pointType_y', pyxb.binding.datatypes.float, required=True)
    __y._DeclarationLocation = pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 20, 2)
    __y._UseLocation = pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 20, 2)
    
    y = property(__y.value, __y.set, None, None)

    
    # Attribute z uses Python identifier z
    __z = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'z'), 'z', '__AbsentNamespace0_pointType_z', pyxb.binding.datatypes.float, required=True)
    __z._DeclarationLocation = pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 21, 2)
    __z._UseLocation = pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 21, 2)
    
    z = property(__z.value, __z.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __x.name() : __x,
        __y.name() : __y,
        __z.name() : __z
    })
_module_typeBindings.pointType = pointType
Namespace.addCategoryObject('typeBinding', 'pointType', pointType)


# Complex type cubeType with content type ELEMENT_ONLY
class cubeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type cubeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cubeType')
    _XSDLocation = pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 23, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element center uses Python identifier center
    __center = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'center'), 'center', '__AbsentNamespace0_cubeType_center', False, pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 25, 3), )

    
    center = property(__center.value, __center.set, None, None)

    
    # Element dim uses Python identifier dim
    __dim = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dim'), 'dim', '__AbsentNamespace0_cubeType_dim', False, pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 26, 3), )

    
    dim = property(__dim.value, __dim.set, None, None)

    
    # Element p_value uses Python identifier p_value
    __p_value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'p_value'), 'p_value', '__AbsentNamespace0_cubeType_p_value', False, pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 27, 3), )

    
    p_value = property(__p_value.value, __p_value.set, None, None)

    _ElementMap.update({
        __center.name() : __center,
        __dim.name() : __dim,
        __p_value.name() : __p_value
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.cubeType = cubeType
Namespace.addCategoryObject('typeBinding', 'cubeType', cubeType)


# Complex type sphereType with content type ELEMENT_ONLY
class sphereType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type sphereType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'sphereType')
    _XSDLocation = pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 30, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element center uses Python identifier center
    __center = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'center'), 'center', '__AbsentNamespace0_sphereType_center', False, pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 32, 3), )

    
    center = property(__center.value, __center.set, None, None)

    
    # Element radius uses Python identifier radius
    __radius = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'radius'), 'radius', '__AbsentNamespace0_sphereType_radius', False, pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 33, 3), )

    
    radius = property(__radius.value, __radius.set, None, None)

    
    # Element p_value uses Python identifier p_value
    __p_value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'p_value'), 'p_value', '__AbsentNamespace0_sphereType_p_value', False, pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 34, 3), )

    
    p_value = property(__p_value.value, __p_value.set, None, None)

    _ElementMap.update({
        __center.name() : __center,
        __radius.name() : __radius,
        __p_value.name() : __p_value
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.sphereType = sphereType
Namespace.addCategoryObject('typeBinding', 'sphereType', sphereType)


# Complex type ellipsoidType with content type ELEMENT_ONLY
class ellipsoidType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ellipsoidType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ellipsoidType')
    _XSDLocation = pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 37, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element center uses Python identifier center
    __center = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'center'), 'center', '__AbsentNamespace0_ellipsoidType_center', False, pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 39, 3), )

    
    center = property(__center.value, __center.set, None, None)

    
    # Element a uses Python identifier a
    __a = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'a'), 'a', '__AbsentNamespace0_ellipsoidType_a', False, pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 40, 3), )

    
    a = property(__a.value, __a.set, None, None)

    
    # Element b uses Python identifier b
    __b = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'b'), 'b', '__AbsentNamespace0_ellipsoidType_b', False, pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 41, 3), )

    
    b = property(__b.value, __b.set, None, None)

    
    # Element c uses Python identifier c
    __c = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'c'), 'c', '__AbsentNamespace0_ellipsoidType_c', False, pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 42, 3), )

    
    c = property(__c.value, __c.set, None, None)

    
    # Element p_value uses Python identifier p_value
    __p_value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'p_value'), 'p_value', '__AbsentNamespace0_ellipsoidType_p_value', False, pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 43, 3), )

    
    p_value = property(__p_value.value, __p_value.set, None, None)

    _ElementMap.update({
        __center.name() : __center,
        __a.name() : __a,
        __b.name() : __b,
        __c.name() : __c,
        __p_value.name() : __p_value
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ellipsoidType = ellipsoidType
Namespace.addCategoryObject('typeBinding', 'ellipsoidType', ellipsoidType)


# Complex type cylinderType with content type ELEMENT_ONLY
class cylinderType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type cylinderType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cylinderType')
    _XSDLocation = pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 46, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element center uses Python identifier center
    __center = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'center'), 'center', '__AbsentNamespace0_cylinderType_center', False, pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 48, 3), )

    
    center = property(__center.value, __center.set, None, None)

    
    # Element height uses Python identifier height
    __height = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'height'), 'height', '__AbsentNamespace0_cylinderType_height', False, pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 49, 3), )

    
    height = property(__height.value, __height.set, None, None)

    
    # Element radius uses Python identifier radius
    __radius = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'radius'), 'radius', '__AbsentNamespace0_cylinderType_radius', False, pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 50, 3), )

    
    radius = property(__radius.value, __radius.set, None, None)

    
    # Element p_value uses Python identifier p_value
    __p_value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'p_value'), 'p_value', '__AbsentNamespace0_cylinderType_p_value', False, pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 51, 3), )

    
    p_value = property(__p_value.value, __p_value.set, None, None)

    _ElementMap.update({
        __center.name() : __center,
        __height.name() : __height,
        __radius.name() : __radius,
        __p_value.name() : __p_value
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.cylinderType = cylinderType
Namespace.addCategoryObject('typeBinding', 'cylinderType', cylinderType)


VolumePhantom = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'VolumePhantom'), volumePhantomType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 4, 1))
Namespace.addCategoryObject('elementBinding', VolumePhantom.name().localName(), VolumePhantom)



volumePhantomType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'origin'), pointType, scope=volumePhantomType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 7, 3)))

volumePhantomType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dimension'), pointType, scope=volumePhantomType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 8, 3)))

volumePhantomType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cube'), cubeType, scope=volumePhantomType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 9, 3)))

volumePhantomType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cylinder'), cylinderType, scope=volumePhantomType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 10, 3)))

volumePhantomType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ellipsoid'), ellipsoidType, scope=volumePhantomType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 11, 3)))

volumePhantomType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sphere'), sphereType, scope=volumePhantomType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 12, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 9, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 10, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 11, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 12, 3))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(volumePhantomType._UseForTag(pyxb.namespace.ExpandedName(None, 'origin')), pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 7, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(volumePhantomType._UseForTag(pyxb.namespace.ExpandedName(None, 'dimension')), pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 8, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(volumePhantomType._UseForTag(pyxb.namespace.ExpandedName(None, 'cube')), pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 9, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(volumePhantomType._UseForTag(pyxb.namespace.ExpandedName(None, 'cylinder')), pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 10, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(volumePhantomType._UseForTag(pyxb.namespace.ExpandedName(None, 'ellipsoid')), pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 11, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(volumePhantomType._UseForTag(pyxb.namespace.ExpandedName(None, 'sphere')), pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 12, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
volumePhantomType._Automaton = _BuildAutomaton()




cubeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'center'), pointType, scope=cubeType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 25, 3)))

cubeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dim'), pointType, scope=cubeType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 26, 3)))

cubeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'p_value'), pyxb.binding.datatypes.int, scope=cubeType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 27, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cubeType._UseForTag(pyxb.namespace.ExpandedName(None, 'center')), pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 25, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cubeType._UseForTag(pyxb.namespace.ExpandedName(None, 'dim')), pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 26, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cubeType._UseForTag(pyxb.namespace.ExpandedName(None, 'p_value')), pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 27, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
cubeType._Automaton = _BuildAutomaton_()




sphereType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'center'), pointType, scope=sphereType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 32, 3)))

sphereType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'radius'), pyxb.binding.datatypes.float, scope=sphereType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 33, 3)))

sphereType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'p_value'), pyxb.binding.datatypes.int, scope=sphereType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 34, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(sphereType._UseForTag(pyxb.namespace.ExpandedName(None, 'center')), pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 32, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(sphereType._UseForTag(pyxb.namespace.ExpandedName(None, 'radius')), pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 33, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(sphereType._UseForTag(pyxb.namespace.ExpandedName(None, 'p_value')), pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 34, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
sphereType._Automaton = _BuildAutomaton_2()




ellipsoidType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'center'), pointType, scope=ellipsoidType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 39, 3)))

ellipsoidType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'a'), pyxb.binding.datatypes.float, scope=ellipsoidType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 40, 3)))

ellipsoidType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'b'), pyxb.binding.datatypes.float, scope=ellipsoidType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 41, 3)))

ellipsoidType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'c'), pyxb.binding.datatypes.float, scope=ellipsoidType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 42, 3)))

ellipsoidType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'p_value'), pyxb.binding.datatypes.int, scope=ellipsoidType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 43, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ellipsoidType._UseForTag(pyxb.namespace.ExpandedName(None, 'center')), pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 39, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ellipsoidType._UseForTag(pyxb.namespace.ExpandedName(None, 'a')), pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ellipsoidType._UseForTag(pyxb.namespace.ExpandedName(None, 'b')), pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ellipsoidType._UseForTag(pyxb.namespace.ExpandedName(None, 'c')), pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ellipsoidType._UseForTag(pyxb.namespace.ExpandedName(None, 'p_value')), pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ellipsoidType._Automaton = _BuildAutomaton_3()




cylinderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'center'), pointType, scope=cylinderType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 48, 3)))

cylinderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'height'), pyxb.binding.datatypes.float, scope=cylinderType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 49, 3)))

cylinderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'radius'), pyxb.binding.datatypes.float, scope=cylinderType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 50, 3)))

cylinderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'p_value'), pyxb.binding.datatypes.int, scope=cylinderType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 51, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cylinderType._UseForTag(pyxb.namespace.ExpandedName(None, 'center')), pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 48, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cylinderType._UseForTag(pyxb.namespace.ExpandedName(None, 'height')), pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 49, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cylinderType._UseForTag(pyxb.namespace.ExpandedName(None, 'radius')), pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 50, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cylinderType._UseForTag(pyxb.namespace.ExpandedName(None, 'p_value')), pyxb.utils.utility.Location('E:\\Code\\Python\\DigitalPhantomDcm\\geometry\\volume_phantom.xsd', 51, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
cylinderType._Automaton = _BuildAutomaton_4()

