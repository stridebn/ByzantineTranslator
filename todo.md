# TODO

[Link to proposal](https://docs.google.com/document/d/1JAycElu2VLVazUdrnukzrj1UKbqQJbdXak-FltWnHb8/edit?usp=sharing)



### Decide on OCR Package or begin self-implementation
[ ] Tesseract

[ ] Keras-OCR

[ ] Yolo

[ ] OpenCV

### Training Data
[ ] Gather sufficient training data

[ ] Produce single-line or full document ground truth references

[ ] Train and test

### Testing Pipeline
[V] Determine solution for verification - Rip unicode characters via code (all training samples are PDF documents) to determine if music successfully read.

[ ] Prepare and formulate test and grading framework for analyzing results (all symbols have been read and processed successfully)

[ ] Post-translational: ensure all phrases maintain 

### Staff Music Writer
[ ] LilyPond?

[ ] music21?

### Music Translation Algorithm
[ ] Encode each note as an interval

[ ] Read and verify intervals using references in the document itself

[ ] Translate string of intervals into absolute notes

[ ] Implement scale reference for each tone

[ ] Implement dynamics and scale changes

[ ] Implement stress, ties, and accidentals

[ ] Implement lyrics rendering

### Packaging
[ ] Desktop application (simple gui, file import and output location)

[ ] (Stretch Goal) Mobile Application

