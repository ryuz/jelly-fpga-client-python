# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: jelly_fpga_control.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'jelly_fpga_control.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18jelly_fpga_control.proto\x12\x12jelly_fpga_control\"\x07\n\x05\x45mpty\"\x1e\n\x0c\x42oolResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\"\x0e\n\x0cResetRequest\"\x1b\n\x0bLoadRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\",\n\x0cLoadResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x0c\n\x04slot\x18\x02 \x01(\x05\"\x1d\n\rUnloadRequest\x12\x0c\n\x04slot\x18\x01 \x01(\x05\"3\n\x15UploadFirmwareRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"%\n\x15RemoveFirmwareRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"$\n\x14LoadBitstreamRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1f\n\x0fLoadDtboRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1e\n\x0f\x44tsToDtbRequest\x12\x0b\n\x03\x64ts\x18\x01 \x01(\t\"/\n\x10\x44tsToDtbResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x0b\n\x03\x64tb\x18\x02 \x01(\x0c\"O\n\x15\x42itstreamToBinRequest\x12\x16\n\x0e\x62itstream_name\x18\x01 \x01(\t\x12\x10\n\x08\x62in_name\x18\x02 \x01(\t\x12\x0c\n\x04\x61rch\x18\x03 \x01(\t\"K\n\x0fOpenMmapRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x04\x12\x0c\n\x04size\x18\x03 \x01(\x04\x12\x0c\n\x04unit\x18\x04 \x01(\x04\",\n\x0eOpenUioRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04unit\x18\x02 \x01(\x04\"F\n\x12OpenUdmabufRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61\x63he_enable\x18\x02 \x01(\x08\x12\x0c\n\x04unit\x18\x03 \x01(\x04\"*\n\x0cOpenResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\n\n\x02id\x18\x02 \x01(\r\"\x1a\n\x0c\x43loseRequest\x12\n\n\x02id\x18\x01 \x01(\r\"I\n\x0fSubcloneRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0e\n\x06offset\x18\x02 \x01(\x04\x12\x0c\n\x04size\x18\x03 \x01(\x04\x12\x0c\n\x04unit\x18\x04 \x01(\x04\".\n\x10SubcloneResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\n\n\x02id\x18\x02 \x01(\r\"\x1c\n\x0eGetAddrRequest\x12\n\n\x02id\x18\x01 \x01(\r\"/\n\x0fGetAddrResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x0c\n\x04\x61\x64\x64r\x18\x02 \x01(\x04\"\x1c\n\x0eGetSizeRequest\x12\n\n\x02id\x18\x01 \x01(\r\"/\n\x0fGetSizeResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x0c\n\x04size\x18\x02 \x01(\x04\" \n\x12GetPhysAddrRequest\x12\n\n\x02id\x18\x01 \x01(\r\"8\n\x13GetPhysAddrResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x11\n\tphys_addr\x18\x02 \x01(\x04\"J\n\x10WriteMemURequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0e\n\x06offset\x18\x02 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x04\x12\x0c\n\x04size\x18\x04 \x01(\x04\"J\n\x10WriteMemIRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0e\n\x06offset\x18\x02 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x03\x12\x0c\n\x04size\x18\x04 \x01(\x04\":\n\x0eReadMemRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0e\n\x06offset\x18\x02 \x01(\x04\x12\x0c\n\x04size\x18\x03 \x01(\x04\"G\n\x10WriteRegURequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0b\n\x03reg\x18\x02 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x04\x12\x0c\n\x04size\x18\x04 \x01(\x04\"G\n\x10WriteRegIRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0b\n\x03reg\x18\x02 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x03\x12\x0c\n\x04size\x18\x04 \x01(\x04\"7\n\x0eReadRegRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0b\n\x03reg\x18\x02 \x01(\x04\x12\x0c\n\x04size\x18\x03 \x01(\x04\"-\n\rReadUResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x04\"-\n\rReadIResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x03\">\n\x12WriteMemF32Request\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0e\n\x06offset\x18\x02 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x02\">\n\x12WriteMemF64Request\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0e\n\x06offset\x18\x02 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x01\"/\n\x0fReadF32Response\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x02\"/\n\x0fReadF64Response\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x01\";\n\x12WriteRegF32Request\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0b\n\x03reg\x18\x02 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x02\";\n\x12WriteRegF64Request\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0b\n\x03reg\x18\x02 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x01\"<\n\x10MemCopyToRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0e\n\x06offset\x18\x02 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\">\n\x12MemCopyFromRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0e\n\x06offset\x18\x02 \x01(\x04\x12\x0c\n\x04size\x18\x03 \x01(\x04\"3\n\x13MemCopyFromResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x32\xdd\x17\n\x10JellyFpgaControl\x12K\n\x05Reset\x12 .jelly_fpga_control.ResetRequest\x1a .jelly_fpga_control.BoolResponse\x12I\n\x04Load\x12\x1f.jelly_fpga_control.LoadRequest\x1a .jelly_fpga_control.LoadResponse\x12M\n\x06Unload\x12!.jelly_fpga_control.UnloadRequest\x1a .jelly_fpga_control.BoolResponse\x12_\n\x0eUploadFirmware\x12).jelly_fpga_control.UploadFirmwareRequest\x1a .jelly_fpga_control.BoolResponse(\x01\x12]\n\x0eRemoveFirmware\x12).jelly_fpga_control.RemoveFirmwareRequest\x1a .jelly_fpga_control.BoolResponse\x12[\n\rLoadBitstream\x12(.jelly_fpga_control.LoadBitstreamRequest\x1a .jelly_fpga_control.BoolResponse\x12Q\n\x08LoadDtbo\x12#.jelly_fpga_control.LoadDtboRequest\x1a .jelly_fpga_control.BoolResponse\x12U\n\x08\x44tsToDtb\x12#.jelly_fpga_control.DtsToDtbRequest\x1a$.jelly_fpga_control.DtsToDtbResponse\x12]\n\x0e\x42itstreamToBin\x12).jelly_fpga_control.BitstreamToBinRequest\x1a .jelly_fpga_control.BoolResponse\x12Q\n\x08OpenMmap\x12#.jelly_fpga_control.OpenMmapRequest\x1a .jelly_fpga_control.OpenResponse\x12O\n\x07OpenUio\x12\".jelly_fpga_control.OpenUioRequest\x1a .jelly_fpga_control.OpenResponse\x12W\n\x0bOpenUdmabuf\x12&.jelly_fpga_control.OpenUdmabufRequest\x1a .jelly_fpga_control.OpenResponse\x12K\n\x05\x43lose\x12 .jelly_fpga_control.CloseRequest\x1a .jelly_fpga_control.BoolResponse\x12U\n\x08Subclone\x12#.jelly_fpga_control.SubcloneRequest\x1a$.jelly_fpga_control.SubcloneResponse\x12R\n\x07GetAddr\x12\".jelly_fpga_control.GetAddrRequest\x1a#.jelly_fpga_control.GetAddrResponse\x12R\n\x07GetSize\x12\".jelly_fpga_control.GetSizeRequest\x1a#.jelly_fpga_control.GetSizeResponse\x12^\n\x0bGetPhysAddr\x12&.jelly_fpga_control.GetPhysAddrRequest\x1a\'.jelly_fpga_control.GetPhysAddrResponse\x12S\n\tWriteMemU\x12$.jelly_fpga_control.WriteMemURequest\x1a .jelly_fpga_control.BoolResponse\x12S\n\tWriteMemI\x12$.jelly_fpga_control.WriteMemIRequest\x1a .jelly_fpga_control.BoolResponse\x12Q\n\x08ReadMemU\x12\".jelly_fpga_control.ReadMemRequest\x1a!.jelly_fpga_control.ReadUResponse\x12Q\n\x08ReadMemI\x12\".jelly_fpga_control.ReadMemRequest\x1a!.jelly_fpga_control.ReadIResponse\x12S\n\tWriteRegU\x12$.jelly_fpga_control.WriteRegURequest\x1a .jelly_fpga_control.BoolResponse\x12S\n\tWriteRegI\x12$.jelly_fpga_control.WriteRegIRequest\x1a .jelly_fpga_control.BoolResponse\x12Q\n\x08ReadRegU\x12\".jelly_fpga_control.ReadRegRequest\x1a!.jelly_fpga_control.ReadUResponse\x12Q\n\x08ReadRegI\x12\".jelly_fpga_control.ReadRegRequest\x1a!.jelly_fpga_control.ReadIResponse\x12W\n\x0bWriteMemF32\x12&.jelly_fpga_control.WriteMemF32Request\x1a .jelly_fpga_control.BoolResponse\x12W\n\x0bWriteMemF64\x12&.jelly_fpga_control.WriteMemF64Request\x1a .jelly_fpga_control.BoolResponse\x12U\n\nReadMemF32\x12\".jelly_fpga_control.ReadMemRequest\x1a#.jelly_fpga_control.ReadF32Response\x12U\n\nReadMemF64\x12\".jelly_fpga_control.ReadMemRequest\x1a#.jelly_fpga_control.ReadF64Response\x12W\n\x0bWriteRegF32\x12&.jelly_fpga_control.WriteRegF32Request\x1a .jelly_fpga_control.BoolResponse\x12W\n\x0bWriteRegF64\x12&.jelly_fpga_control.WriteRegF64Request\x1a .jelly_fpga_control.BoolResponse\x12U\n\nReadRegF32\x12\".jelly_fpga_control.ReadRegRequest\x1a#.jelly_fpga_control.ReadF32Response\x12U\n\nReadRegF64\x12\".jelly_fpga_control.ReadRegRequest\x1a#.jelly_fpga_control.ReadF64Response\x12S\n\tMemCopyTo\x12$.jelly_fpga_control.MemCopyToRequest\x1a .jelly_fpga_control.BoolResponse\x12^\n\x0bMemCopyFrom\x12&.jelly_fpga_control.MemCopyFromRequest\x1a\'.jelly_fpga_control.MemCopyFromResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'jelly_fpga_control_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EMPTY']._serialized_start=48
  _globals['_EMPTY']._serialized_end=55
  _globals['_BOOLRESPONSE']._serialized_start=57
  _globals['_BOOLRESPONSE']._serialized_end=87
  _globals['_RESETREQUEST']._serialized_start=89
  _globals['_RESETREQUEST']._serialized_end=103
  _globals['_LOADREQUEST']._serialized_start=105
  _globals['_LOADREQUEST']._serialized_end=132
  _globals['_LOADRESPONSE']._serialized_start=134
  _globals['_LOADRESPONSE']._serialized_end=178
  _globals['_UNLOADREQUEST']._serialized_start=180
  _globals['_UNLOADREQUEST']._serialized_end=209
  _globals['_UPLOADFIRMWAREREQUEST']._serialized_start=211
  _globals['_UPLOADFIRMWAREREQUEST']._serialized_end=262
  _globals['_REMOVEFIRMWAREREQUEST']._serialized_start=264
  _globals['_REMOVEFIRMWAREREQUEST']._serialized_end=301
  _globals['_LOADBITSTREAMREQUEST']._serialized_start=303
  _globals['_LOADBITSTREAMREQUEST']._serialized_end=339
  _globals['_LOADDTBOREQUEST']._serialized_start=341
  _globals['_LOADDTBOREQUEST']._serialized_end=372
  _globals['_DTSTODTBREQUEST']._serialized_start=374
  _globals['_DTSTODTBREQUEST']._serialized_end=404
  _globals['_DTSTODTBRESPONSE']._serialized_start=406
  _globals['_DTSTODTBRESPONSE']._serialized_end=453
  _globals['_BITSTREAMTOBINREQUEST']._serialized_start=455
  _globals['_BITSTREAMTOBINREQUEST']._serialized_end=534
  _globals['_OPENMMAPREQUEST']._serialized_start=536
  _globals['_OPENMMAPREQUEST']._serialized_end=611
  _globals['_OPENUIOREQUEST']._serialized_start=613
  _globals['_OPENUIOREQUEST']._serialized_end=657
  _globals['_OPENUDMABUFREQUEST']._serialized_start=659
  _globals['_OPENUDMABUFREQUEST']._serialized_end=729
  _globals['_OPENRESPONSE']._serialized_start=731
  _globals['_OPENRESPONSE']._serialized_end=773
  _globals['_CLOSEREQUEST']._serialized_start=775
  _globals['_CLOSEREQUEST']._serialized_end=801
  _globals['_SUBCLONEREQUEST']._serialized_start=803
  _globals['_SUBCLONEREQUEST']._serialized_end=876
  _globals['_SUBCLONERESPONSE']._serialized_start=878
  _globals['_SUBCLONERESPONSE']._serialized_end=924
  _globals['_GETADDRREQUEST']._serialized_start=926
  _globals['_GETADDRREQUEST']._serialized_end=954
  _globals['_GETADDRRESPONSE']._serialized_start=956
  _globals['_GETADDRRESPONSE']._serialized_end=1003
  _globals['_GETSIZEREQUEST']._serialized_start=1005
  _globals['_GETSIZEREQUEST']._serialized_end=1033
  _globals['_GETSIZERESPONSE']._serialized_start=1035
  _globals['_GETSIZERESPONSE']._serialized_end=1082
  _globals['_GETPHYSADDRREQUEST']._serialized_start=1084
  _globals['_GETPHYSADDRREQUEST']._serialized_end=1116
  _globals['_GETPHYSADDRRESPONSE']._serialized_start=1118
  _globals['_GETPHYSADDRRESPONSE']._serialized_end=1174
  _globals['_WRITEMEMUREQUEST']._serialized_start=1176
  _globals['_WRITEMEMUREQUEST']._serialized_end=1250
  _globals['_WRITEMEMIREQUEST']._serialized_start=1252
  _globals['_WRITEMEMIREQUEST']._serialized_end=1326
  _globals['_READMEMREQUEST']._serialized_start=1328
  _globals['_READMEMREQUEST']._serialized_end=1386
  _globals['_WRITEREGUREQUEST']._serialized_start=1388
  _globals['_WRITEREGUREQUEST']._serialized_end=1459
  _globals['_WRITEREGIREQUEST']._serialized_start=1461
  _globals['_WRITEREGIREQUEST']._serialized_end=1532
  _globals['_READREGREQUEST']._serialized_start=1534
  _globals['_READREGREQUEST']._serialized_end=1589
  _globals['_READURESPONSE']._serialized_start=1591
  _globals['_READURESPONSE']._serialized_end=1636
  _globals['_READIRESPONSE']._serialized_start=1638
  _globals['_READIRESPONSE']._serialized_end=1683
  _globals['_WRITEMEMF32REQUEST']._serialized_start=1685
  _globals['_WRITEMEMF32REQUEST']._serialized_end=1747
  _globals['_WRITEMEMF64REQUEST']._serialized_start=1749
  _globals['_WRITEMEMF64REQUEST']._serialized_end=1811
  _globals['_READF32RESPONSE']._serialized_start=1813
  _globals['_READF32RESPONSE']._serialized_end=1860
  _globals['_READF64RESPONSE']._serialized_start=1862
  _globals['_READF64RESPONSE']._serialized_end=1909
  _globals['_WRITEREGF32REQUEST']._serialized_start=1911
  _globals['_WRITEREGF32REQUEST']._serialized_end=1970
  _globals['_WRITEREGF64REQUEST']._serialized_start=1972
  _globals['_WRITEREGF64REQUEST']._serialized_end=2031
  _globals['_MEMCOPYTOREQUEST']._serialized_start=2033
  _globals['_MEMCOPYTOREQUEST']._serialized_end=2093
  _globals['_MEMCOPYFROMREQUEST']._serialized_start=2095
  _globals['_MEMCOPYFROMREQUEST']._serialized_end=2157
  _globals['_MEMCOPYFROMRESPONSE']._serialized_start=2159
  _globals['_MEMCOPYFROMRESPONSE']._serialized_end=2210
  _globals['_JELLYFPGACONTROL']._serialized_start=2213
  _globals['_JELLYFPGACONTROL']._serialized_end=5250
# @@protoc_insertion_point(module_scope)
