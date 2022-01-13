# Classification of biological organisms based on their codon usage frequencies

This project aims to correctly classify organisms to their correct kingdoms based on their codon usage frequencies.  As observed in the chart below, different kingdoms of organisms exhibit codons relating to amino acid expression at different frequencies.  

![](Data/codons.png)

Using data sourced from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Codon+usage), these codon frequencies could subsequently be used as a feature to classify organisms into their proper kingdoms through machine learning and deep learning.  As an additional feature engineering step, these codons were translated to their corresponding amino acids such that amino acid frequency could also be employed in the model.  


At present, classification models have been trained using sklearn's **Random Forest Classifier** and **Support Vector Machines Classifier** as well as a **Deep Neural Network** in Keras. The top performing model is the **Keras Neural Network**, with an accuracy score of just over 94%.  




