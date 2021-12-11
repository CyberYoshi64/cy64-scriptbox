#include <3ds.h>
#include <cwav.h>
#include <cstring>
#include "cycwar_svc.hpp"

CYW4CTR::FMT_CYCWAR::SVC::SVC() {
    sound = (CWAV*)malloc(sizeof(CWAV));
    toVolAmount = -1.f; toPitchAmount = -1.f;
}
CYW4CTR::FMT_CYCWAR::SVC::~SVC() {
    cwavFree(sound);
    if (sound->dataBuffer) linearFree(sound->dataBuffer);
    if (sound) free(sound);
}
bool CYW4CTR::FMT_CYCWAR::SVC::IsLoaded() {return isLoaded;}
void CYW4CTR::FMT_CYCWAR::SVC::Play() {
    if(isLoaded) {
        float bak = sound->volume;
        sound->volume *= masterVolume;
        cwavPlayResult res = cwavPlay(sound, 0, -1);
        sound->volume = bak;
        if (res.playStatus == CWAV_SUCCESS)
        {
            lChann = res.monoLeftChannel;
            rChann = -1;
        }
    }
}
void CYW4CTR::FMT_CYCWAR::SVC::EnsurePlaying() {currStopFrame = 0; if (!IsPlaying()) Play();}
void CYW4CTR::FMT_CYCWAR::SVC::StereoPlay() {
    if(isLoaded)
    {
        cwavPlayResult res = cwavPlay(sound, 0, 1);
        if (res.playStatus == CWAV_SUCCESS)
        {
            lChann = res.monoLeftChannel;
            rChann = res.rightChannel;
        }
    }        
}
void CYW4CTR::FMT_CYCWAR::SVC::Stop(){if(isLoaded){cwavStop(sound,-1,-1);lChann=rChann=-1;}}
bool CYW4CTR::FMT_CYCWAR::SVC::IsPlaying() {
    if(isLoaded) {
        return cwavIsPlaying(sound);
    } else {
        return isLoaded;
    }
}
void CYW4CTR::FMT_CYCWAR::SVC::SetPitch(float amount, bool affect) {
    if (!isLoaded)
        return;
    if (affect)
        sound->pitch = amount;
    else {
        fromPitchAmount = amount;
        toDPitchAmount = amount;
    }        
    if (IsPlaying() && affect)
    {
        if (rChann != -1)
        {
            ndspChnSetRate(rChann, sound->sampleRate * amount);
        }
        ndspChnSetRate(lChann, sound->sampleRate * amount);
    }
}
void CYW4CTR::FMT_CYCWAR::SVC::SetMasterVolume(float volume) {masterVolume=volume;SetVolume(sound->volume);}
void CYW4CTR::FMT_CYCWAR::SVC::SetVolume(float volume) {
    if (!isLoaded) return;
    float mix[12] = {0};
    sound->volume = volume;
    if (IsPlaying())
    {
        if (rChann == -1)
        {
            float rightPan = (sound->monoPan + 1.f) / 2.f;
            float leftPan = 1.f - rightPan;
            mix[0] = 0.8f * leftPan * volume * masterVolume; // Left front
            mix[2] = 0.2f * leftPan * volume * masterVolume; // Left back
            mix[1] = 0.8f * rightPan * volume * masterVolume; // Right front
            mix[3] = 0.2f * rightPan * volume * masterVolume; // Right back
            ndspChnSetMix(lChann, mix);
        } else {
            
            mix[0] = 0.8f * volume * masterVolume; // Left front
            mix[2] = 0.2f * volume * masterVolume; // Left back
            ndspChnSetMix(lChann, mix);
            memset(mix, 0, sizeof(mix));
            mix[1] = 0.8f  * volume * masterVolume; // Right front
            mix[3] = 0.2f  * volume * masterVolume; // Right back
            ndspChnSetMix(rChann, mix);
        }
        
    }
        
}
void CYW4CTR::FMT_CYCWAR::SVC::SetTargetVolume(float amount, int frames) {
    if (amount == toVolAmount) return;
    currVolFrame = frames;
    targetVolFrame = frames;
    fromVolAmount = sound->volume;
    toVolAmount = amount;
}
void CYW4CTR::FMT_CYCWAR::SVC::SetCreatePitch(float amount, int frames) {
    if (amount == toPitchAmount) return;
    currPitchFrame = frames;
    targetPitchFrame = frames;
    fromPitchAmount = sound->pitch;
    toPitchAmount = amount;
}
void CYW4CTR::FMT_CYCWAR::SVC::SetDecayPitch(float amount, int frames) {
    if (amount == toDPitchAmount) return;
    currDPitchFrame = frames;
    targetDPitchFrame = frames;
    fromDPitchAmount = sound->pitch;
    toDPitchAmount = amount;
}
void CYW4CTR::FMT_CYCWAR::SVC::SetTargetStop(int frames) {if (currStopFrame == 0 && IsPlaying()) currStopFrame = frames;}
void CYW4CTR::FMT_CYCWAR::SVC::Tick() {
    if (currVolFrame != 0) {
        float prog = 1.f - (--currVolFrame / (float)targetVolFrame);
        float newVol = fromVolAmount + (toVolAmount - fromVolAmount) * prog;
        SetVolume(newVol);
    }
    if (currPitchFrame != 0) {
        float prog = 1.f - (--currPitchFrame / (float)targetPitchFrame);
        float newPitch = fromPitchAmount + (toPitchAmount - fromPitchAmount) * prog;
        SetPitch(newPitch, true);
    }
    if (currDPitchFrame != 0) {
        float prog = 1.f - (--currDPitchFrame / (float)targetDPitchFrame);
        float newPitch = fromDPitchAmount + (toDPitchAmount - fromDPitchAmount) * prog;
        SetPitch(newPitch, true);
    }
    if (currStopFrame != 0) {
        if (!--currStopFrame) Stop();
    }
}

// float qrsqrt(float num){long i; float x2, y; const float th=1.5f; x2=num*0.5f; y=num; i=*(long*)&y; i=0x5f3759df-(i>>1); y=*(float*)&i; y=y*(th-(x2*y*y));}