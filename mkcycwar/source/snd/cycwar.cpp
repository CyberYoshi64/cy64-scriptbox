#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <vector>
#include <3ds.h>
#include "cycwar_svc.hpp"
#include "cycwar.hpp"

std::vector<CYW4CTR::FMT_CYCWAR::INTERNAL_SE> sfx;
int latestFileID=0;

void CYW4CTR::FMT_CYCWAR::Free(int fid){
	u32 i=0;
	while (i < sfx.size()){
		if (sfx.at(i).fileId == fid || fid < 0){
			sprintf(sfx.at(i).name,"%s","");
			sfx.at(i).active=false;
			delete sfx.at(i).snd;
		}
		i++;
	}
}
size_t CYW4CTR::FMT_CYCWAR::GetArrSz(){return sfx.size();}
size_t CYW4CTR::FMT_CYCWAR::GetActiveSfxNum(){
	int res=0;
	for (size_t i=0; i<sfx.size(); i++){
		res += sfx[i].active;
	}
	return res;
}
int CYW4CTR::FMT_CYCWAR::LoadCYCWAR(const char* fname, int* fid){
	int err=0; u16 csar_i, byte2, sfx_c;
	size_t idx, sfxi=0; char byte; u32 sfxsrci, cwavo=0;
	CYW4CTR::FMT_CYCWAR::INTERNAL_SE tmpsfx;
	std::ifstream csar(fname,std::fstream::binary);
	char* fbuf;
	fbuf=new char[8];
	csar.read(fbuf, 8);
	if (memcmp(fbuf,"CY64CWAR",8)!=0) {err=1; goto end;}
	csar.read((char*)&byte2,2); if (byte2 != 3){err=2; goto end;}
	csar.read((char*)&sfx_c,2);
	csar.read((char*)&cwavo,4);
	delete fbuf; fbuf=new char[64];
	fid=&latestFileID;
	tmpsfx.fileId=latestFileID++;
	while(sfxi < sfx_c){
		idx=0; memset(fbuf,0,64);
		while(true){
			if (idx>63){err=2; break;}
			csar.read(&byte,1);
			if (!byte) break;
			fbuf[idx++]=byte;
		}
		sprintf(tmpsfx.name,"%s",fbuf);
		csar.read((char*)&tmpsfx.fsz,4);
		csar.read(&tmpsfx.flg,1);
		tmpsfx.snd = new CYW4CTR::FMT_CYCWAR::SVC();
		void* cwavbuf=linearAlloc(tmpsfx.fsz);
		if(!cwavbuf) svcBreak(USERBREAK_PANIC);
		csar_i=csar.tellg();
		csar.seekg(cwavo, csar.beg);
		csar.read((char*)cwavbuf,tmpsfx.fsz);
		cwavLoad(tmpsfx.snd->sound,cwavbuf,tmpsfx.flg>>1);
		tmpsfx.snd->isLoaded = tmpsfx.snd->sound->loadStatus == CWAV_SUCCESS;
		tmpsfx.active=true;
		for(sfxsrci=0; sfxsrci<sfx.size(); sfxsrci++){
			if(sfx[sfxsrci].active);
		}
		if (sfxsrci>=sfx.size()){
			sfx.push_back(tmpsfx);
		}
		cwavo += tmpsfx.fsz; sfxi++;
		csar.seekg(csar_i, csar.beg);
	}
	end:
	if (fbuf) delete fbuf;
	csar.close();
	return err;
}
size_t CYW4CTR::FMT_CYCWAR::GetID(const char* name){
	for(size_t i=0; i<sfx.size(); i++){
		if(memcmp(name,sfx.at(i).name,strlen(name))==0) return i;
	}
	return 0xDEAD;
}
CYW4CTR::FMT_CYCWAR::INTERNAL_SE* CYW4CTR::FMT_CYCWAR::GetSfx(const char* name){
	size_t idx=GetID(name);
	if (idx!=0xDEAD) return &sfx[idx];
	return NULL;
}
CYW4CTR::FMT_CYCWAR::INTERNAL_SE* CYW4CTR::FMT_CYCWAR::GetSfxFromID(size_t idx){
	if (idx>sfx.size()) return NULL;
	return &sfx[idx];
}
void CYW4CTR::FMT_CYCWAR::Play(const char* name){
	size_t idx=GetID(name);
	if (idx!=0xDEAD) PlayID(idx);
}
void CYW4CTR::FMT_CYCWAR::PlayID(size_t idx){
	if(idx >= sfx.size()) return;
	if(sfx[idx].flg & 1){sfx[idx].snd->StereoPlay();}else{sfx[idx].snd->Play();}
}
void CYW4CTR::FMT_CYCWAR::Stop(const char* name){
	size_t idx=GetID(name);
	if (idx!=0xDEAD) StopID(idx);
}
void CYW4CTR::FMT_CYCWAR::StopID(size_t idx){
	if(idx >= sfx.size()) return;
	sfx[idx].snd->Stop();
}
void CYW4CTR::FMT_CYCWAR::SetVolume(const char* name, float vol){
	size_t idx=GetID(name);
	if (idx!=0xDEAD) SetVolumeWithID(idx,vol);
}
void CYW4CTR::FMT_CYCWAR::SetVolumeWithID(size_t idx, float vol){
	if(idx >= sfx.size()) return;
	sfx[idx].snd->SetVolume(vol);
}
void CYW4CTR::FMT_CYCWAR::SetPitch(const char* name, float pth){
	size_t idx=GetID(name);
	if (idx!=0xDEAD) SetPitchWithID(idx,pth);
}
void CYW4CTR::FMT_CYCWAR::SetPitchWithID(size_t idx, float pth){
	if(idx >= sfx.size()) return;
	sfx[idx].snd->SetPitch(pth,1);
}
void CYW4CTR::FMT_CYCWAR::FadeVolume(const char* name, float vol, int frm){
	size_t idx=GetID(name);
	if (idx!=0xDEAD) FadeVolumeWithID(idx,vol,frm);
}
void CYW4CTR::FMT_CYCWAR::FadeVolumeWithID(size_t idx, float vol, int frm){
	if(idx >= sfx.size()) return;
	sfx[idx].snd->SetTargetVolume(vol,frm);
}
void CYW4CTR::FMT_CYCWAR::FadePitch(const char* name, float pth, int frm){
	size_t idx=GetID(name);
	if (idx!=0xDEAD) FadePitchWithID(idx,pth,frm);
}
void CYW4CTR::FMT_CYCWAR::FadePitchWithID(size_t idx, float pth, int frm){
	if(idx >= sfx.size()) return;
	sfx[idx].snd->SetCreatePitch(pth,frm);
}
void CYW4CTR::FMT_CYCWAR::Tick(){
	for(size_t i=0; i<sfx.size(); i++){
		sfx.at(i).snd->Tick();
	}
}
