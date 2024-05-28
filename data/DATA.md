This is the code to curate the CLAVI diagnostic dataset proposed in our paper "Dissecting Multimodality in VideoQA Transformer Models by Impairing Modality Fusion".

CLAVI is curated from Charades. Please download the Charades Videos from the official providers [[link](https://prior.allenai.org/projects/charades)]

Usage: To curate CLAVI, execute the command    ```python process_videos.py  --charades_vid_dir=<CHARADES_DIR> --output_directory=<OUTPUT_DIR>```
where, ```<CHARADES_DIR>``` is the path of the directory containing videos from Charades and  ```<OUTPUT_DIR>``` is the output path where videos for CLAVI will be stored.

The folder ```json_files``` contains the files containing questions, answers and annotations of the video segment (used for curating the videos from Charades).

The table below provides a map of the question types. Note that V and V' refer to the video and the complement video respectively. Similarly, Q and Q' refer to the question and the complement question. 


| Type | Question-Type           | Answer |
|------|-------------------------|--------|
| 0    | E-type (V)              | Yes    |
| 1    | E-type N.C. (V)         | No     |
| 4    | BE-type (V, Q)          | Yes    |
| 5    | BE-type (V, Q')         | No     |
| 8    | BA-type (V, Q)          | Yes    |
| 9    | BA-type (V, Q')         | No     |
| 10   | BA-type N.C. (V, Q/Q')  | No     |
| 16   | E-type (V')             | Yes    |
| 17   | E-type N.C. (V')        | No     |
| 20   | BE-type (V', Q)         | No     |
| 21   | BE-type (V', Q')        | Yes    |
| 24   | BA-type (V', Q)         | No     |
| 25   | BA-type (V', Q')        | Yes    |
| 26   | BA-type N.C. (V', Q/Q') | No     |

Also, the ```video_name``` attribute if of the form XXXXXXXX_1 for the original video segment and XXXXXXXX_2 for the complement video segment, where XXXXXXXX is a unique 8-digit video id.
