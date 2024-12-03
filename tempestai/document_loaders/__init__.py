from tempestai.document_loaders.directory import DirectoryReader
from tempestai.document_loaders.docx import DocxReader
from tempestai.document_loaders.html import HTMLReader
from tempestai.document_loaders.json import JSONReader
from tempestai.document_loaders.pdf import PDFReader
from tempestai.document_loaders.s3 import S3Reader
from tempestai.document_loaders.watson_discovery import  WatsonDiscoveryReader

__all__ = [
    "DirectoryReader",
    "DocxReader",
    "HTMLReader",
    "JSONReader",
    "PDFReader",
    "S3Reader",
    "WatsonDiscoveryReader",
]
