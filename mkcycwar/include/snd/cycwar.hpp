/**
 * @file cycwar.hpp
 * @brief CYW4CTR - CYCWAR - 3DS BCWAV archive format
*/

#pragma once

#include "cycwar_svc.hpp"

namespace CYW4CTR {
	namespace FMT_CYCWAR {
		/// Internal CYCWAR struct
		typedef struct {
		CYW4CTR::FMT_CYCWAR::SVC* snd;
		int fileId;
		bool active;
		char name[64];
		size_t fsz;
		char flg;
		} INTERNAL_SE;

		/**
		 * @brief Get total amount of BCWAV slots
		*/
		size_t GetArrSz();

		/**
		 * @brief Get amount of BCWAV active slots
		*/
		size_t GetActiveSfxNum();

		/**
		 * @brief Free all CYCWAR elements (or certain from a file given by the file ID)
		 * @param fid File ID to free contents of (If -1 is specified, free everything)
		*/
		void Free(int fid);

		/**
		 * @brief Load CYCWAR and extract data from it
		 * @param fname Path to the source file
		 * @param fid Integer to return file ID to
		*/
		int LoadCYCWAR(const char* fname, int* fid);

		/**
		 * @brief (Only for use internally) Get internal sound ID based on name
		 * @param name Internal name to find its ID of
		 * @return Internal ID as integer
		*/
		size_t GetID(const char* name);

		/**
		 * @brief Get internal sound struct specified by internal name
		 * @param name Internal name
		 * @return Struct containing CWAV and generic info about sound
		*/
		INTERNAL_SE* GetSfx(const char* name);

		/**
		 * @brief Get internal sound struct specified by internal ID
		 * @param idx Internal ID
		 * @return Struct containing CWAV and generic info about sound
		*/
		INTERNAL_SE* GetSfxFromID(size_t idx);
		/**
		 * @brief Play a sound specified by internal name
		 * @param name Internal name
		*/
		void Play(const char* name);

		/**
		 * @brief Play a sound specified by internal ID (Internal use only)
		 * @param idx Internal ID
		*/
		void PlayID(size_t idx);

		/**
		 * @brief Stop a sound specified by name
		 * @param name Internal name
		*/
		void Stop(const char* name);

		/**
		 * @brief Stop a sound specified by internal ID (Internal use only)
		 * @param idx Internal ID
		*/
		void StopID(size_t idx);

		/**
		 * @brief Set the volume of a sound specified by name
		 * @param name Internal name
		 * @param vol Volume in percent (0.0-1.0)
		*/
		void SetVolume(const char* name, float vol);

		/**
		 * @brief Set the volume of a sound specified by internal ID (Internal use only)
		 * @param idx Internal ID
		 * @param vol Volume in percent (0.0-1.0)
		*/
		void SetVolumeWithID(size_t idx, float vol);

		/**
		 * @brief Set pitch of a sound specified by name
		 * @param name Internal name
		 * @param pth Pitch in percent (1.0 = default)
		*/
		void SetPitch(const char* name, float pth);

		/**
		 * @brief Set pitch of a sound specified by internal ID (Internal use only)
		 * @param idx Internal ID
		 * @param pth Pitch in percent (1.0 = default)
		*/
		void SetPitchWithID(size_t idx, float pth);

		/**
		 * @brief Fade volume of a sound specified by name
		 * @param name Internal name
		 * @param vol Volume in percent to fade to (0.0-1.0)
		*/
		void FadeVolume(const char* name, float vol, int frm);

		/**
		 * @brief Fade volume of a sound specified by internal ID (Internal use only)
		 * @param idx Internal ID
		 * @param vol Volume in percent to fade to (0.0-1.0)
		*/
		void FadeVolumeWithID(size_t idx, float vol, int frm);

		/**
		 * @brief Fade pitch of a sound specified by name
		 * @param name Internal name
		 * @param pth Pitch in percent to fade to (1.0 = default)
		*/
		void FadePitch(const char* name, float pth, int frm);

		/**
		 * @brief Fade pitch of a sound specified by internal ID (Internal use only)
		 * @param idx Internal ID
		 * @param pth Pitch in percent to fade to (1.0 = default)
		*/
		void FadePitchWithID(size_t idx, float pth, int frm);

		/**
		 * @brief Update sounds (volume/pitch fading, etc.)
		 * 
		 * Please call it once per frame.
		*/
		void Tick();
	}
}