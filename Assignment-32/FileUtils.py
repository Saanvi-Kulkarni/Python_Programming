import os
import sys
from simple_file_checksum import get_checksum

def ChecksumFile(DirectoryName, fobj):
    Ret = os.path.exists(DirectoryName)

    if (Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirectoryName)

    if (Ret == False):
        print("It is not a directory")
        return
    
    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        for f in FileName:
            FilePath = os.path.join(FolderName, f)
            Checksum = get_checksum(FilePath)
            fobj.write(f + " : " +Checksum + "\n")

def CheckDuplicate(DirName, fobj):
    Ret = os.path.exists(DirName)

    if (Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirName)

    if (Ret == False):
        print("It is not a directory")
        return

    for FolderName, SubFolder, FileName in os.walk(DirName):
        for f in FileName:
            FilePath = os.path.join(FolderName, f)
            for FolderName2, SubFolder2, FileName2 in os.walk(DirName):
                for f2 in FileName2:
                    FilePath2 = os.path.join(FolderName2, f2)
                    if (FilePath != FilePath2):
                        if (os.path.getsize(FilePath) == os.path.getsize(FilePath2)):
                            fobj.write("Duplicate file : " + FilePath + " and " + FilePath2 + "\n")

def DirectoryDuplicateRemover(DirName, fobj):
    Ret = os.path.exists(DirName)

    if (Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirName)

    if (Ret == False):
        print("It is not a directory")
        return

    for FolderName, SubFolder, FileName in os.walk(DirName):
        for f in FileName:
            FilePath = os.path.join(FolderName, f)
            if not os.path.exists(FilePath):        # ✅ add this
                continue    
            for FolderName2, SubFolder2, FileName2 in os.walk(DirName):
                for f2 in FileName2:
                    FilePath2 = os.path.join(FolderName2, f2)
                    if (FilePath != FilePath2):
                        if (os.path.getsize(FilePath) == os.path.getsize(FilePath2)):
                            os.remove(FilePath2)
                            fobj.write("Duplicate file removed : " + FilePath2 + "\n")
                            break