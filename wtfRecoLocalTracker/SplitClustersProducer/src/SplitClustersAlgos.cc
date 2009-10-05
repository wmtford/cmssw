//
//  Implementation base for cluster splitting producer
//  Provides functions that can be shared with analysis classes.
//

// this class header
#include "wtfRecoLocalTracker/SplitClustersProducer/interface/SplitClustersAlgos.h"


//
//  Number of strips in the left sub-cluster of a splittable cluster
//
uint8_t SplitClustersAlgos::leftStripCount(const std::vector<uint8_t> amp,
    		   const std::vector<PSimHit> associated)
{
  float totalEnergy, leftAmplitudeFraction;
  return (leftStripCount(amp, associated, totalEnergy, leftAmplitudeFraction));
}

uint8_t SplitClustersAlgos::leftStripCount(const std::vector<uint8_t> amp,
    		   const std::vector<PSimHit> associated,
    		   float& totalEnergy,
    		   float& leftAmplitudeFraction)
{
  //Calculate the energy fraction of 1 of the 2 SimHits associated
  float leftEnergyFraction=0, leftEnergy = 0, middlex = 0, thisx = 0;
  totalEnergy = 0;
  std::vector<PSimHit>::const_iterator firstsimhit = associated.begin();
  middlex = firstsimhit->localPosition().x();
  leftEnergy = firstsimhit->energyLoss();
  for(std::vector<PSimHit>::const_iterator simhitsIter=firstsimhit; simhitsIter<associated.end(); simhitsIter++){
    totalEnergy += simhitsIter->energyLoss();
    if (middlex > (thisx = simhitsIter->localPosition().x())) {
      middlex = thisx;
      leftEnergy = simhitsIter->energyLoss();
    }
  }
  leftEnergyFraction = leftEnergy / totalEnergy;

  //Find # of strips from the left which in total have charge fraction ~ energy fraction
  float totalAmplitude =0, leftAmplitude =0;
  leftAmplitudeFraction = 0;
  uint8_t stripCounter = 0;
  for(size_t j=0; j < size_t(amp.size()); ++j) totalAmplitude += float(amp[j]);
  for(size_t j=0; j < size_t(amp.size()) && leftAmplitudeFraction <= leftEnergyFraction; ++j){
    leftAmplitude += float(amp[j]);
    leftAmplitudeFraction = leftAmplitude/totalAmplitude;
    stripCounter++;
  }
  return(stripCounter);
}
