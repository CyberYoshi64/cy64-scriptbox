#include <stdio.h>
#include <string.h>
#include <3ds.h>

int main(int argc, char* argv[]) {
    aptInit();
    gfxInitDefault();
    hidInit();
    cfguInit();

    Result res;
    u8 countryInfo[4];
    u16 countryName[16][64];
    u16 areaName[16][64];
    u16 eulaInfo[2];
    u8  userName[0x1C];
    u32 globecoords;

    u16 namebuf[64];
    char text[512];

    PrintConsole topScreen;
    consoleInit(GFX_TOP, &topScreen);
    consoleSelect(&topScreen);

    if R_FAILED(res = CFGU_GetConfigInfoBlk2(4, 0xB0000, countryInfo))
        printf("Failed to get CountryInfo. (%08lX)\n", res);

    if R_FAILED(res = CFGU_GetConfigInfoBlk2(0x800, 0xB0001, countryName))
        printf("Failed to get CountryNames. (%08lX)\n", res);

    if R_FAILED(res = CFGU_GetConfigInfoBlk2(0x800, 0xB0002, areaName))
        printf("Failed to get AreaNames. (%08lX)\n", res);

    if R_FAILED(res = CFGU_GetConfigInfoBlk2(4, 0xB0003, &globecoords))
        printf("Failed to get GlobeCoords. (%08lX)\n", res);

    if R_FAILED(res = CFGU_GetConfigInfoBlk2(4, 0xD0000, eulaInfo))
        printf("Failed to get EulaInfo. (%08lX)\n", res);

    if R_FAILED(res = CFGU_GetConfigInfoBlk2(0x1C, 0xA0000, userName))
        printf("Failed to get UserName. (%08lX)\n", res);

    const char* countryNewName = "Nowhere";
    const char* areaNewName = "Shame, isn't it?";
    globecoords = 0xDEADBEEF; // Antarctica? But coincidence!
    eulaInfo[0] = 0xFFFF; // Agreed (max)
    eulaInfo[1] = 0x0200; // Latest EULA (fake 2.0)
    
    // These will break NNID auth until corrected
    // in System Settings
    countryInfo[0] = 0;  // IDK what that is, has to be 0
    countryInfo[1] = 0;  // IDK what that is, has to be 0
    countryInfo[2] = 14; // Saxony
    countryInfo[3] = 78; // Germany

    *(u32*)(userName + 0x14) = 0;
    *(u32*)(userName + 0x18) = 0xFFFFFFFF;

    memset(namebuf, 0, sizeof(namebuf));
    utf8_to_utf16(namebuf, (u8*)countryNewName, 64);
    for (u32 i = 0; i < 16; i++)
        memcpy(countryName[i], namebuf, sizeof(namebuf));

    memset(namebuf, 0, sizeof(namebuf));
    utf8_to_utf16(namebuf, (u8*)areaNewName, 64);
    for (u32 i = 0; i < 16; i++)
        memcpy(areaName[i], namebuf, sizeof(namebuf));

    if R_FAILED(res = CFG_SetConfigInfoBlk8(0x800, 0xB0001, countryName))
        printf("Failed to set CountryNames. (%08lX)\n", res);
    else
        printf("SUCCESS: Set CountryNames to '%s'\n", countryNewName);

    if R_FAILED(res = CFG_SetConfigInfoBlk8(0x800, 0xB0002, areaName))
        printf("Failed to set AreaNames. (%08lX)\n", res);
    else
        printf("SUCCESS: Set AreaNames to '%s'\n", areaNewName);

    if R_FAILED(res = CFG_SetConfigInfoBlk8(4, 0xB0003, &globecoords))
        printf("Failed to set GlobeCoords. (%08lX)\n", res);
    else
        printf("SUCCESS: Set GlobeCoords to %08lX\n", globecoords);

    if R_FAILED(res = CFG_SetConfigInfoBlk8(4, 0xB0000, countryInfo))
        printf("Failed to set CountryInfo. (%08lX)\n", res);
    else
        printf("SUCCESS: Set CountryInfo to %2d, %2d\n", countryInfo[2], countryInfo[3]);

    if R_FAILED(res = CFG_SetConfigInfoBlk8(4, 0xD0000, eulaInfo))
        printf("Failed to set EulaInfo. (%08lX)\n", res);
    else
        printf("SUCCESS: Set EulaInfo to %04X, %04X\n", eulaInfo[0], eulaInfo[1]);

    if R_FAILED(res = CFG_SetConfigInfoBlk8(0x1C, 0xA0000, userName))
        printf("Failed to set UserName. (%08lX)\n", res);
    else
        printf("SUCCESS: Set UserName.\n");

    printf("Press START to exit\n");

    while(aptMainLoop()) {
        hidScanInput();
        if (hidKeysDown() & KEY_START) break;
    }
    
    if R_FAILED(res = CFG_UpdateConfigSavegame()) {
        errorConf e;
        errorInit(&e, ERROR_TEXT_WORD_WRAP, 0);
        sprintf(text, "Failed to write to the config savegame.\n(Res code: %08lX)\n\nIt's uncertain whether the changes will apply properly.", res);
        errorText(&e, text);
        errorDisp(&e);
    }
    
    aptExit();
    gfxExit();
    hidExit();
    cfguExit();
    return 0;
}