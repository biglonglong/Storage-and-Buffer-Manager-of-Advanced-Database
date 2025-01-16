// Buffer.h

#ifndef BUFFER_H
#define BUFFER_H

#include <mutex>
#include "assert.h" 
using namespace std;

#ifdef DEBUG
#define DEFBUFSIZE 10         
#define MAXPAGES 500          
#define NUM_PAGR_REQUEST 1000 
#else
#define DEFBUFSIZE 1024                 // max num of frames in buffer
#define MAXPAGES 50000                  // max num of pages in disk
#define NUM_PAGR_REQUEST 500000         // request times
#endif

#define FRAMESIZE 4096                  // frame size
#define PAGESIZE 4096                   // page size
#define THREAD_NUM 4                    // thread num  
#define DB_FILENAME "../build/data.dbf"
#define DATA_FILENAME "../data/data-5w-50w-zipf.txt"

typedef int frame_id_t;
typedef int page_id_t;

struct bFrame
{
    char field[FRAMESIZE];
};

struct BCB
{
    int page_id;
    int frame_id;
    // int latex; // 内存锁
    int count;
    int dirty;
    BCB *next;

    BCB() : page_id(-1), frame_id(-1), count(0),
            dirty(0), next(nullptr){};
    BCB(int pid, int fid) : page_id(pid), frame_id(fid), count(1),
                            dirty(0), next(nullptr){};
};

class ReplaceAlg
{
public:
    ReplaceAlg() = default;
    virtual ~ReplaceAlg() = default;
    /* Pin the victim frame as defined by the replacement policy. */
    virtual frame_id_t Victim() = 0;
    /* Pins a frame, indicating that it should not be victimized until it is unpinned. */
    virtual void Pin(int frame_id) = 0;
    /* Unpins a frame, indicating that it can now be victimized. */
    virtual void Unpin(int frame_id) = 0;
};

/* Replacement Policies */
enum Policy
{
    Invalid = 0,
    Lru,
    TwoQ,
    Clock
};

#endif // BUFFER_H