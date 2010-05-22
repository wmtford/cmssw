#ifndef SplitClustersAlgos_h
#define SplitClustersAlgos_h

/** \class SplitClustersAlgos
 *  Implementation base for cluster splitting producer
 *  Provides functions that can be shared with analysis classes.
 *
 *  $Date: 2010/05/19 21:30:49 $
 *  $Revision: 1.3 $
 *  \author wtford
 */

#include <memory>

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "SimDataFormats/TrackingHit/interface/PSimHit.h"

class TrackerGeometry;
class SiStripCluster;

class SplitClustersAlgos {
  public:

  enum {byHits = 0, byTracks, noSplit, unknown};

  /// Constructor
    SplitClustersAlgos() { }
  
  /// Destructor
    virtual ~SplitClustersAlgos(){ }
  
 protected:

  //
  //  Number of strips in the left sub-cluster of a splittable cluster
  //
  uint8_t leftStripCount(const std::vector<uint8_t> amp,
			   const std::vector<PSimHit> associated,
			   const int);

  uint8_t leftStripCount(const std::vector<uint8_t> amp,
			   const std::vector<PSimHit> associated,
			   float& totalEnergy,
			   float& leftAmplitudeFraction,
			   const int);

  //
  // Initial vertex from pixel vertex list
  //
  void iniVertex(const reco::VertexCollection pixelVertexColl, reco::Vertex::Point& vtx);

  //
  // Initial vertex.z from pixel vertex list
  //
  void iniZvertex(const reco::VertexCollection pixelVertexColl, float& zv, float& zverr);

  //
  // Path length through sensor origin for straight track from pixel primary vertex
  //
  float straightPathlength(reco::Vertex::Point pixelPrimaryVertex, const TrackerGeometry &tracker, uint32_t detID);


  //
  // Path length through cluster for straight track from pixel primary vertex
  //
  float straightPathlength(reco::Vertex::Point pixelPrimaryVertex,
			   const TrackerGeometry &tracker,
			   uint32_t detID, const SiStripCluster* clust);
};

#endif
