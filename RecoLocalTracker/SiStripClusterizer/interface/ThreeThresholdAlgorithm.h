#ifndef RecoLocalTracker_SiStripClusterizer_ThreeThresholdAlgorithm_h
#define RecoLocalTracker_SiStripClusterizer_ThreeThresholdAlgorithm_h
#include "RecoLocalTracker/SiStripClusterizer/interface/StripClusterizerAlgorithm.h"
#include "RecoLocalTracker/SiStripClusterizer/interface/SiStripApvShotCleaner.h"

class DetId;

class ThreeThresholdAlgorithm final : public StripClusterizerAlgorithm {

  friend class StripClusterizerAlgorithmFactory;

 public:

  void clusterizeDetUnit(const    edm::DetSet<SiStripDigi> &, output_t::FastFiller &);
  void clusterizeDetUnit(const edmNew::DetSet<SiStripDigi> &, output_t::FastFiller &);
  void clusterizeDetUnit(const    edm::DetSet<SiStripDigi> &, output_t::FastFiller &, const TrackerHitAssociator&);
  void clusterizeDetUnit(const edmNew::DetSet<SiStripDigi> &, output_t::FastFiller &, const TrackerHitAssociator&);

  bool stripByStripBegin(uint32_t id);

  // LazyGetter interface
  void stripByStripAdd(uint16_t strip, uint8_t adc, std::vector<SiStripCluster>& out);
  void stripByStripEnd(std::vector<SiStripCluster>& out);
  void addFed(sistrip::FEDZSChannelUnpacker & unpacker, uint16_t ipair, std::vector<SiStripCluster>& out) {
    while (unpacker.hasData()) {
      stripByStripAdd(unpacker.sampleNumber()+ipair*256,unpacker.adc(),out);
      unpacker++;
    }
  }

  // detset interface
  void addFed(sistrip::FEDZSChannelUnpacker & unpacker, uint16_t ipair, output_t::FastFiller & out) override {
    while (unpacker.hasData()) {
      stripByStripAdd(unpacker.sampleNumber()+ipair*256,unpacker.adc(),out);
      unpacker++;
    }
  }

  void stripByStripAdd(uint16_t strip, uint8_t adc, output_t::FastFiller & out) override {
    if(candidateEnded(strip)) endCandidate(out);
    addToCandidate(strip,adc);
  }

  void stripByStripEnd(output_t::FastFiller & out) override { endCandidate(out);}



 private:

  template<class T> void clusterizeDetUnit_(const T&, output_t::FastFiller&);
  template<class T> void clusterizeDetUnit_(const T&, output_t::FastFiller&, const TrackerHitAssociator&);
  ThreeThresholdAlgorithm(float, float, float, unsigned, unsigned, unsigned, std::string qualityLabel,
			  bool setDetId, bool removeApvShots=false);

  //state of the candidate cluster
  std::vector<uint8_t> ADCs;  
  uint16_t lastStrip;
  float noiseSquared;
  bool candidateLacksSeed;

  //constant methods with state information
  uint16_t firstStrip() const {return lastStrip - ADCs.size() + 1;}
  bool candidateEnded(const uint16_t&) const;
  bool candidateAccepted() const;

  //state modification methods
  template<class T> void endCandidate(T&);
  template<class T> void endCandidate(T&, const DetId&, const TrackerHitAssociator&);
  void clearCandidate() { candidateLacksSeed = true;  noiseSquared = 0;  ADCs.clear();}
  void addToCandidate(const SiStripDigi& digi) { addToCandidate(digi.strip(),digi.adc());}
  void addToCandidate(uint16_t strip, uint8_t adc);
  void appendBadNeighbors();
  void applyGains();

  float ChannelThreshold, SeedThreshold, ClusterThresholdSquared;
  uint8_t MaxSequentialHoles, MaxSequentialBad, MaxAdjacentBad;
  bool RemoveApvShots;

  SiStripApvShotCleaner ApvCleaner;
};

#endif
