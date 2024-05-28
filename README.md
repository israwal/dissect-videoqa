# Dissecting Multimodality in VideoQA Transformer Models by Impairing Modality Fusion

## Project Page: [https://dissect-videoqa.github.io/]()

## QUAG and QUAG-attention

QUAG and QUAG-attention are variants of self-attention that impair specific modality interactions in multimodal models. The relative drop in performance with respect to the unperturbed model is representative of 

We provide a google colab demo to test QUAG and QUAG-attention and apply it to custom models in [`QUAG_QUAGAttention_Demo.ipynb`](/QUAG_QUAGAttention_Demo.ipynb)

## CLAVI
We provide the scripts to curate CLAVI dataset from Charades. CLAVI contains complement questions and videos, and the models are thoroughly evaluated using consistent accuracies. The detailed steps of curation can be found in [`/data/DATA.md`](/data/DATA.md)

## Citation
```
@InProceedings{rawal2024dissect,
  title = 	 {{{Dissecting Multimodality in VideoQA Transformer Models by Impairing Modality Fusion}}},
  author =       {Rawal, {Ishaan Singh} and Matyasko, Alexander and Jaiswal, Shantanu and Fernando, Basura and Tan, Cheston},
  booktitle = 	 {Proceedings of the 41st International Conference on Machine Learning},
  year = 	 {2024},
  publisher =    {PMLR}
}
```
