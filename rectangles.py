#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Main function, handles function calls and most print outputs
def __main__():
    fileName = "rectangles.txt"
    print("Starting")
    fileStatus = fileCheck(fileName)
    if fileStatus == False:
        print("Exiting")
        return
    fileContents = readInFile(fileName)
    print("Diagram to count rectangles in.")
    for line in fileContents:
        print(line, end="")
    print()
    vertList = vertexFinder(fileContents)
    print(f"Found Vertices, {vertList}")
    print("Checking for Rectangles")
    rectList = rectangleFinder(vertList)
    rectListNoDoubles = checkForDoubles(rectList)
    print(rectListNoDoubles)
    print("------ Number of Rectangles Found -------")
    if len(rectListNoDoubles) != 0:
        print(len(rectListNoDoubles))
    else:
        print("No Rectangles Found")

#Make sure we didn't double count any rectangles
def checkForDoubles(rectList):
    i = 0
    while i < len(rectList):
        j = i+1
        while j < len(rectList)-1:
            m = 0
            count = 0
            while m < len(rectList[i]):
                n = 0
                while n < len(rectList[j]):
                    if rectList[i][m] == rectList[j][n]:
                        count += 1
                        print("Shared Node Found")
                    n+=1
                if count == 4:
                    print ("Duplicate found.")
                    rectList.remove(rectList[i])
                m+=1
            j+=1
        i+=1
    return rectList

#Get a list of all the vertices in the text
def vertexFinder(fileList):
    vertexList = []
    i = 0
    while i < len(fileList):
        j = 0
        while j < len(fileList[i]):
            if fileList[i][j] == "+":
                vertexList.append([i,j])
            j+=1
        i+=1
    return vertexList
    
#Look for vertices that are on the same horizontal line
def rectangleFinder(vertList):
    rectList = []
    i = 0
    while i < len(vertList):
        j = i+1
        while j < len(vertList)-1:
            if vertList[j][0] == vertList[i][0]:
                vertPair = orthFinder(vertList, vertList[j], vertList[i])
                if vertPair != 0:
                    rectList.append([vertList[i],vertList[j],vertPair[0],vertPair[1]])
            j+=1
        i+=1
    return rectList

#Check for vertices that share the vertical with each of the two found vertices from the rectangleFinder function
def orthFinder(vertList, orthOne, orthTwo):
    possible = []
    for pair in vertList:
        if pair != orthOne and pair != orthTwo:
            if pair[1] == orthOne[1] or pair[1] == orthTwo[1]:
                possible.append(pair)
    i = 0
    while i < len(possible)-1:
        if possible[i][0] == possible[i+1][0]:
            return [possible[i], possible[i+1]]
        i+= 1
    return 0

#Read in lines from a text file
def readInFile(file):
    startList = []
    with open(file,'r') as file_handle:
        for line in file_handle:
            startList.append(line)
    return startList

#Make sure the file exists, handle not found error
def fileCheck(file):
    try:
        with open(file,'r') as name_handle:
            return True
    except FileNotFoundError:
        print("File not Found")
        print("Successfully handled a FileNotFound Error.")
        return False

__main__()
