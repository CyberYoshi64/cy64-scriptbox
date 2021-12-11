/**
 * @file cycwar_svc.hpp
 * @brief CYW4CTR - CYCWAR - 3DS BCWAV archive format - Service from YAMKC3DS by PabloMK7
*/

#pragma once
#include <string>
#include <3ds.h>
#include <cwav.h>

namespace CYW4CTR::FMT_CYCWAR {
    class SVC {
        public:
        SVC();
        ~SVC();
        bool IsLoaded();
        bool IsPlaying();
        void Play();
        void EnsurePlaying();
        void StereoPlay();
        void Stop();
        void SetMasterVolume(float volume);
        void SetVolume(float volume);
        void SetPitch(float amount, bool affect = false);
        void SetTargetVolume(float amount, int frames);
        void SetCreatePitch(float amount, int frames);
        void SetDecayPitch(float amount, int frames);
        void SetTargetStop(int frames);
        void Tick();
        CWAV* sound;
        bool isLoaded;
        float masterVolume = 1.f;
        int lChann = -1, rChann = -1;
        int targetVolFrame, targetPitchFrame, targetDPitchFrame;
        int currVolFrame = 0, currPitchFrame = 0, currDPitchFrame = 0, currStopFrame = 0;
        float fromVolAmount, fromPitchAmount, fromDPitchAmount;
        float toVolAmount, toPitchAmount, toDPitchAmount;
    };
}