import os
import sys
import shutil

def DirectoryScan(DirName, Extension, fobj):
    Border = "-"*50
    
    Ret = os.path.exists(DirName)

    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirName)

    if(Ret == False):
        print("It is not a directory")
        return
    
    TotalFiles = 0
    MatchedFiles = 0
    
    for FolderName, SubFoler, FileName in os.walk(DirName):
        for f in FileName:
            TotalFiles = TotalFiles + 1
            if f.endswith(Extension):
                MatchedFiles = MatchedFiles + 1
                fobj.write("File found : " + f +"\n")

    fobj.write(Border + "\n")
    fobj.write("Total number of files : " + str(TotalFiles) + "\n")
    fobj.write("Matched files : " + str(MatchedFiles) + "\n")
    fobj.write(Border + "\n")

def RenameFile(DirName, OldExtension, NewExtension, fobj):
    Border = "-"*50
    
    Ret = os.path.exists(DirName)

    if(Ret == False):
        print("There is no such directory")
        return 
    
    Ret = os.path.isdir(DirName)
    
    if(Ret == False):
        print("It is not a directory")
        return
    
    TotalFiles = 0
    RenamedFiles = 0

    for FolderName, SubFolder, FileName in os.walk(DirName):
        for f in FileName:
            TotalFiles = TotalFiles + 1
            if f.endswith(OldExtension):
                OldFilePath = os.path.join(FolderName, f)
                NewFileName = f.replace(OldExtension, NewExtension)
                NewFilePath = os.path.join(FolderName, NewFileName)
                os.rename(OldFilePath, NewFilePath)
                RenamedFiles = RenamedFiles + 1
                fobj.write("Renamed : " + f + " --> " + NewFileName + "\n")

    print(Border + "\n")
    fobj.write("Total files scanned : " + str(TotalFiles)   + "\n")
    fobj.write("Total files renamed : " + str(RenamedFiles) + "\n")
    fobj.write(Border + "\n")

def DirectoryCopy(FirstDirectory, SecondDirectory, fobj):
    Border = "-"*50
     
    Ret = os.path.exists(FirstDirectory)
    if(Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(FirstDirectory)
    if(Ret == False):
        print("It is not a directory")
        return
    
    if not os.path.exists(SecondDirectory):
        os.mkdir(SecondDirectory) 

    TotalFiles = 0
    CopiedFiles = 0
    
    for FolderName, SubFolder, FileName in os.walk(FirstDirectory):
        for f in FileName:
            TotalFiles = TotalFiles + 1
            SourceFilePath = os.path.join(FolderName, f)
            DestinationFilePath = os.path.join(SecondDirectory, f)
            shutil.copy2(SourceFilePath, DestinationFilePath)
            CopiedFiles = CopiedFiles + 1
            fobj.write("Copied : " + f + "\n")

    fobj.write("Total files scanned : " + str(TotalFiles)  + "\n")
    fobj.write("Total files copied  : " + str(CopiedFiles) + "\n")


def DirectoryCopySpecific(FirstDirectory, SecondDirectory, Extension, fobj):

    Ret = os.path.exists(FirstDirectory)

    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(FirstDirectory)

    if(Ret == False):
        print("It is not a directory")
        return
    
    if not os.path.exists(SecondDirectory):
        os.mkdir(SecondDirectory)

    TotalFiles = 0
    CopiedFiles = 0

    for FolderName, SunFolder, FileName in os.walk(FirstDirectory):
        for f in FileName:
            TotalFiles = TotalFiles + 1
            FirstFilePath = os.path.join(FolderName, f)
            SecondFilePath = os.path.join(SecondDirectory, f)
            if f.endswith(Extension):
                shutil.copy2(FirstFilePath, SecondFilePath)
                CopiedFiles = CopiedFiles + 1
                fobj.write("Copied : " + f + "\n")
    fobj.write("Total files scanned : " + str(TotalFiles)  + "\n")
    fobj.write("Total files copied  : " + str(CopiedFiles) + "\n")