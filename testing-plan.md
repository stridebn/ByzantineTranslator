The goal of the application is to turn a picture of byzantine music (in a recognizable font and not hand-written) into western notation

OCR
1 pre-processing: isolate unicode byzantine characters from PDF
2 processing: run character recognition algorithm
3 post-processing: ensure correctness in character recognition

Music Translation
OPTION 1:
Music analysis - generate midi file & ensure correctness by comparison with the music files online.

OPTION 2:
IF I can get a hold of the monks (the call center cannot help me), and get the source code, use that to check correctness

OPTION 3: 
As long as the byzantine music read correctly, the only issue is then ensuring my algorithm is correct. If I can prove each note translates correctly in terms of relative pitch, and then ensure that the pitch correctly returns to the notes listed in the music, the music is correct.

