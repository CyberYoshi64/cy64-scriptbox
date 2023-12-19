VR_Maximum = 99999
CECMeets_Maximum = 0x7FFFFFFF
Coins_Maximum = 0x7FFFFFFF
Nothing = 0
All = 2**32-1

class GrandPrixCups:
    Mushroom_50cc       = 0
    Flower_50cc         = 1
    Star_50cc           = 2
    Special_50cc        = 3
    Shell_50cc          = 4
    Banana_50cc         = 5
    Leaf_50cc           = 6
    Lightning_50cc      = 7
    Mushroom_100cc      = 8
    Flower_100cc        = 9
    Star_100cc          = 10
    Special_100cc       = 11
    Shell_100cc         = 12
    Banana_100cc        = 13
    Leaf_100cc          = 14
    Lightning_100cc     = 15
    Mushroom_150cc      = 16
    Flower_150cc        = 17
    Star_150cc          = 18
    Special_150cc       = 19
    Shell_150cc         = 20
    Banana_150cc        = 21
    Leaf_150cc          = 22
    Lightning_150cc     = 23
    Mushroom_Mirror     = 24
    Flower_Mirror       = 25
    Star_Mirror         = 26
    Special_Mirror      = 27
    Shell_Mirror        = 28
    Banana_Mirror       = 29
    Leaf_Mirror         = 30
    Lightning_Mirror    = 31
    Amount              = 32

class RankType:
    Rank_None   = 0
    Rank_C      = 1
    Rank_B      = 2
    Rank_A      = 3
    Rank_1Star  = 4
    Rank_2Stars = 5
    Rank_3Stars = 6
    Maximum     = 7

class TrophyType:
    Tro_None    = 0
    Tro_Bronze  = 1
    Tro_Silver  = 2
    Tro_Gold    = 3
    Maximum     = 4

class UnlockMask:
    class Kart:
        Standard    = 0
        Egg1        = 1
        TinyTug     = 2
        Cloud9      = 4
        Zucchini    = 8
        BDasher     = 16
        Bruiser     = 32
        BumbleV     = 64
        KoopaClown  = 128
        PipeFrame   = 256
        BlueSeven   = 512
        CactX       = 1024
        BarrelTrain = 2048
        SodaJet     = 4096
        Gold        = 8192
        All         = 0x3FFF

    class Tire:
        Standard    = 0
        Slick       = 1
        Slim        = 2
        Sponge      = 4
        RedMonster  = 8
        Mushroom    = 16
        Wood        = 32
        Gold        = 64
        All         = 0x7F

    class Glider:
        Standard    = 0
        Parafoil    = 1
        Parasol     = 2
        Flower      = 4
        Swoop       = 8
        Beast       = 16
        Gold        = 32
        All         = 0x3F

    class Character:
        Standard    = 0
        Daisy       = 1
        Wario       = 2
        Rosalina    = 4
        Metal       = 8
        ShyGuy      = 16
        HoneyQueen  = 32
        Wiggler     = 64
        Lakitu      = 128
        Mii         = 256
        All         = 0x1FF

    class Cup:
        Standard    = 0
        Flower      = 1
        Star        = 2
        Special     = 4
        Banana      = 8
        Leaf        = 16
        Lightning   = 32
        All         = 0x3F