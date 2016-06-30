#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import concourse.thriftapi.data.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
from concourse.utils import python_to_thrift, thrift_to_python
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class ComplexTObjectType:

    """
    The possible types for a {@link ComplexTObject}.
    """
    SCALAR = 1
    MAP = 2
    LIST = 3
    SET = 4
    TOBJECT = 5
    TCRITERIA = 6

    _VALUES_TO_NAMES = {
        1: "SCALAR",
        2: "MAP",
        3: "LIST",
        4: "SET",
        5: "TOBJECT",
        6: "TCRITERIA"
        }

    _NAMES_TO_VALUES = {
        "SCALAR": 1,
        "MAP": 2,
        "LIST": 3,
        "SET": 4,
        "TOBJECT": 5,
        "TCRITERIA": 6
        }


class ComplexTObject:
    """
    A recursive structure that encodes one or more {@link TObject TObjects}.

    <p>
    The most basic {@link ComplexTObject} is a
    {@link ComplexTObjectType#SCALAR scalar}, which is just a wrapped
    {@link TObject}. Beyond that, complex collections can be represented as a
    {@link Set}, {@link List} or {@link Map} of
    {@link ComplexTObject ComplexTObjects}.
    </p>

    Attributes:
     - type
     - tscalar
     - tmap
     - tlist
     - tset
    """

    thrift_spec = None

    @staticmethod
    def from_python_object(obj):
        """
        Convert a python object to the appropriate ComplexTObject

        :param obj: the object to wrap
        :return: the wrapper ComplexTObject
        """
        complex = ComplexTObject()
        if isinstance(obj, dict):
            complex.type = ComplexTObjectType.MAP
            tmap = {}
            print(obj)
            for k, v in obj.items():
                tmap[ComplexTObject.from_python_object(k)] = ComplexTObject.from_python_object(v)
            complex.tmap = tmap;
        elif isinstance(obj, list):
            complex.type = ComplexTObjectType.LIST
            tlist = []
            for elt in obj:
                tlist.append(ComplexTObject.from_python_object(elt))
            complex.tlist = tlist
        elif isinstance(obj, set):
            complex.type = ComplexTObjectType.SET
            tset = set()
            for elt in obj:
                tset.add(ComplexTObject.from_python_object(elt))
            complex.tset = tset
        else:
            complex.type = ComplexTObjectType.SCALAR
            complex.tscalar = python_to_thrift(obj)
        return complex

    def __init__(self, type=None, tscalar=None, tmap=None, tlist=None, tset=None,):
        self.type = type
        self.tscalar = tscalar
        self.tmap = tmap
        self.tlist = tlist
        self.tset = tset

    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.tscalar = concourse.thriftapi.data.ttypes.TObject()
                    self.tscalar.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.MAP:
                    self.tmap = {}
                    (_ktype1, _vtype2, _size0 ) = iprot.readMapBegin()
                    for _i4 in range(_size0):
                        _key5 = ComplexTObject()
                        _key5.read(iprot)
                        _val6 = ComplexTObject()
                        _val6.read(iprot)
                        self.tmap[_key5] = _val6
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.tlist = []
                    (_etype10, _size7) = iprot.readListBegin()
                    for _i11 in range(_size7):
                        _elem12 = ComplexTObject()
                        _elem12.read(iprot)
                        self.tlist.append(_elem12)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.SET:
                    self.tset = set()
                    (_etype16, _size13) = iprot.readSetBegin()
                    for _i17 in range(_size13):
                        _elem18 = ComplexTObject()
                        _elem18.read(iprot)
                        self.tset.add(_elem18)
                    iprot.readSetEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ComplexTObject')
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 1)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.tscalar is not None:
            oprot.writeFieldBegin('tscalar', TType.STRUCT, 2)
            self.tscalar.write(oprot)
            oprot.writeFieldEnd()
        if self.tmap is not None:
            oprot.writeFieldBegin('tmap', TType.MAP, 3)
            oprot.writeMapBegin(TType.STRUCT, TType.STRUCT, len(self.tmap))
            for kiter19,viter20 in list(self.tmap.items()):
                kiter19.write(oprot)
                viter20.write(oprot)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.tlist is not None:
            oprot.writeFieldBegin('tlist', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.tlist))
            for iter21 in self.tlist:
                iter21.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.tset is not None:
            oprot.writeFieldBegin('tset', TType.SET, 5)
            oprot.writeSetBegin(TType.STRUCT, len(self.tset))
            for iter22 in self.tset:
                iter22.write(oprot)
            oprot.writeSetEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.type is None:
            raise TProtocol.TProtocolException(message='Required field type is unset!')
        return


    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.type)
        value = (value * 31) ^ hash(self.tscalar)
        value = (value * 31) ^ hash(self.tmap)
        value = (value * 31) ^ hash(self.tlist)
        value = (value * 31) ^ hash(self.tset)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

    def get_python_object(self):
        """
        Return the Python object that is wrapped within this ComplexTObject

        :return: the wrapped Python object
        """
        if self.type == ComplexTObjectType.MAP:
            ret = {}
            for k, v in self.tmap.items():
                ret[k.get_python_object()] = v.get_python_object()
            return ret
        elif self.type == ComplexTObjectType.LIST:
            ret = []
            for elt in self.tlist:
                ret.append(elt.get_python_object())
            return ret
        elif self.type == ComplexTObjectType.SET:
            ret = set()
            for elt in self.tset:
                ret.add(elt.get_python_object())
            return ret
        else:
            return thrift_to_python(self.tscalar)

# Must declare thrift_spec after class definition since its self referential
ComplexTObject.thrift_spec = (
        None,  # 0
        (1, TType.I32, 'type', None, None, ), # 1
        (2, TType.STRUCT, 'tscalar', (concourse.thriftapi.data.ttypes.TObject, concourse.thriftapi.data.ttypes.TObject.thrift_spec), None, ), # 2
        (3, TType.MAP, 'tmap', (TType.STRUCT,(ComplexTObject, ComplexTObject.thrift_spec),TType.STRUCT,(ComplexTObject, ComplexTObject.thrift_spec)), None, ), # 3
        (4, TType.LIST, 'tlist', (TType.STRUCT,(ComplexTObject, ComplexTObject.thrift_spec)), None, ), # 4
        (5, TType.SET, 'tset', (TType.STRUCT,(ComplexTObject, ComplexTObject.thrift_spec)), None, ), # 5
        (6, TType.TOBJECT, 'tobject', (TType.STRUCT,(ComplexTObject, ComplexTObject.thrift_spec)), None, ), # 6
        (7, TType.TCRITERIA, 'tcriteria', (TType.STRUCT,(ComplexTObject, ComplexTObject.thrift_spec)), None, ), # 7
    )