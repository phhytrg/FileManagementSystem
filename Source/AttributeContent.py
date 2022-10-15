from AttributeHeader import *


class Attribute30:
    def __init__(self,header, filename_length, filename) -> None:
        self.header:AttributeHeader = header
        self.filename_length = filename_length
        self.filename = filename

class IndexEntry:
    def __init__(self, length_of_index_entry, length_of_stream, index_flags, 
    size_of_file, length_of_filename, filename) -> None:
        self.length_of_index_entry = length_of_index_entry
        self.length_of_stream = length_of_stream
        self.index_flags = index_flags
        self.size_of_file = size_of_file
        self.length_of_filename = length_of_filename
        self.filename = filename

class IndexRoot:
    def __init__(self, attribute_type, collation_rule, allocation_index_entry, 
    cluster_per_index_record) -> None:
        self.attribute_type = attribute_type
        self.collation_rule = collation_rule
        self.allocation_index_entry = allocation_index_entry
        self.cluster_per_index_record = cluster_per_index_record

class IndexHeader:
    def __init__(self, first_entry_offset, index_entries_size, allocated_size, has_subnode_flag) -> None:
        self.first_entry_offset = first_entry_offset
        self.index_entries_size = index_entries_size
        self.allocated_size = allocated_size
        self.has_subnode_flag = has_subnode_flag


class Attribute90:
    header:AttributeHeader
    index_root:IndexRoot
    index_header:IndexHeader
    index_entries:list[IndexEntry]
    def __init__(self, header,index_root, index_header, index_entries) -> None:
        self.header = header
        self.index_entries = index_entries
        self.index_root = index_root
        self.index_header = index_header
    

class File:
    filename:Attribute30 
    index_root:Attribute90
