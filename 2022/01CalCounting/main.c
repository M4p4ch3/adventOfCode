/*
Advent of code 2022
Day 01 : Calorie Counting
https://adventofcode.com/2022/day/1
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define uint unsigned int

// int getLine(FILE * pFile, char * sData, uint dataLen)
// {
//     int ret = 0;
//     uint charIdx = 0;
//     char aChar = ' ';

//     if (pFile == NULL)
//     {
//         printf("ERROR %s pFile NULL\n", __func__);
//         return 1;
//     }

//     if (sData == NULL)
//     {
//         printf("ERROR %s sData NULL\n", __func__);
//         return 1;
//     }

//     charIdx = 0;
//     aChar = fgetc(pFile);
//     while (aChar != '\n' && !feof(pFile))
//     {
//         if (charIdx >= dataLen)
//         {
//             printf("ERROR %s line too long for data len\n", __func__);
//             return 1;
//         }

//         sData[charIdx] = aChar;
//         charIdx += 1;
//         aChar = fgetc(pFile);
//     }

//     if (charIdx >= dataLen)
//     {
//         printf("ERROR %s line too long for data len\n", __func__);
//         return 1;
//     }

//     sData[charIdx] = '\0';

//     return 0;
// }

int readFile(FILE * pFile, char ** psData, uint * pDataLen)
{
    int ret = 0;

    fseek(pFile, 0L, SEEK_END);
    *pDataLen = ftell(pFile);
    fseek(pFile, 0L, SEEK_SET);

    *psData = (char *) malloc(*pDataLen * sizeof(char));

    ret = fread(*psData, sizeof(char), *pDataLen, pFile);
    if (ret != *pDataLen)
    {
        printf("ERROR %s fread %lu Bytes FAILED\n", __func__, sizeof(char) * *pDataLen);
        free(*psData);
        return 1;
    }

    return 0;
}

int splitLines(const char * sData, uint dataLen, char *** pppLineData, uint * pLineCnt)
{
    uint dataIdx = 0;
    uint lineIdx = 0;
    uint lineDataIdx = 0;
    char * pLineData = NULL;
    // char ** ppLineData = NULL;

    dataIdx = 0;
    lineIdx = 0;
    while (dataIdx < dataLen)
    {
        if (sData[dataIdx] == '\n')
        {
            lineIdx += 1;
        }

        dataIdx += 1;
    }

    *pLineCnt = lineIdx;
    // printf("lineCnt=%u\n", *pLineCnt);
    *pppLineData = (char **) malloc(lineIdx * sizeof(char *));

    dataIdx = 0;
    lineIdx = 0;
    while (dataIdx < dataLen)
    {
        lineDataIdx = 0;
        while (dataIdx < dataLen && sData[dataIdx + lineDataIdx] != '\n')
        {
            lineDataIdx += 1;
        }

        // printf("line %u len=%u\n", lineIdx, lineDataIdx);
        (*pppLineData)[lineIdx] = (char *) malloc(lineDataIdx * sizeof(char));

        lineDataIdx = 0;
        while (dataIdx < dataLen && sData[dataIdx + lineDataIdx] != '\n')
        {
            // printf("data = %c\n", sData[dataIdx + lineDataIdx]);
            (*pppLineData)[lineIdx][lineDataIdx] = sData[dataIdx + lineDataIdx];
            lineDataIdx += 1;
        }

        if (lineIdx >= 20)
        {
            break;
        }

        lineIdx += 1;
        dataIdx += lineDataIdx + 1;
    }

    return 0;
}

int main(void)
{
    int ret = 0;
    uint fileLen = 0;
    char * sFileData = NULL;
    FILE * pFile = NULL;

    uint lineCnt = 0;
    uint lineIdx = 0;
    char ** ppLineData = NULL;

    pFile = fopen("inputEx.txt","r");
    if (pFile == NULL)
    {
        printf("ERROR %s fopen FAILED\n", __func__);
        goto out_free;
    }

    ret = readFile(pFile, &sFileData, &fileLen);
    if (ret != 0)
    {
        printf("ERROR %s readFile FAILED\n", __func__);
        (void) fclose(pFile);
        goto out_free;
    }

    printf("sFileData=[\n%s\n]\n", sFileData);

    ret = splitLines(sFileData, fileLen, &ppLineData, &lineCnt);
    if (ret != 0)
    {
        printf("ERROR %s splitLines FAILED\n", __func__);
        goto out_free;
    }

    for (lineIdx = 0; lineIdx < lineCnt; lineIdx += 1)
    {
        printf("line %u data=[%s]\n", lineIdx, ppLineData[lineIdx]);
    }

    // TODO
    // int calorie_cnt = 0;
    // calorie_cnt = atoi(sLineData);
    // printf("calorie_cnt=%d\n", calorie_cnt);

out_free:
    if (ppLineData != NULL)
    {
        for (lineIdx = 0; lineIdx < lineCnt; lineIdx += 1)
        {
            if (ppLineData[lineIdx] != NULL)
            {
                free(ppLineData[lineIdx]);
            }
        }

        free(ppLineData);
    }

    if (sFileData != NULL)
    {
        free(sFileData);
    }

    ret = fclose(pFile);
    if (ret != 0)
    {
        printf("ERROR %s fclose FAILED\n", __func__);
        return ret;
    }

    return 0;
}
