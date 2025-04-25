# EvoTrace-CSN2-Phylogenetic-Analysis-of-CSN2-Orthologs-Across-Mammals
EvoTrace-CSN2 is a Python-powered workflow for analyzing evolutionary relationships between mammals using orthologous sequences of the CSN2 gene. EvoTrace-CSN2 is a Python-powered workflow for analyzing evolutionary relationships between mammals using orthologous sequences of the CSN2 gene. The project uses multiple bioinformatics tools and techniques—including sequence alignment, phylogeny reconstruction, and distance matrix computation—to trace genomic similarities across terrestrial and marine vertebrates. This project compares CSN2 orthologs from a diverse set of mammals: cattle, house mouse, dog, blue whale, harbor porpoise, hippopotamus, human, and tiger. The analysis includes:</br>
 - Pairwise sequence alignment.</br>
 - Construction of phylograms and radial trees.</br>
 - Manual computation of evolutionary distances.</br>
 - Tree reconstruction from distance matrices.</br>
 - Interpretation of marine mammal relationships in the context of evolution.</br>

# Methodology
Data Collection: Orthologs obtained from NCBI for each species.</br>
Tree Building: Used external phylogeny tools (e.g., Phylogeny.fr) to build radial and rectangular phylogenetic trees. Extended with hippopotamus, human, and tiger to assess evolutionary closeness.</br>
Distance Matrix Calculation: Implemented in a4.py to generate a pairwise distance matrix from manually aligned sequences.</br>
Manual Tree Drawing: Reconstructed phylogeny based on computed distances for validation.

# Key Insights
 - Blue whale and harbor porpoise form a marine mammal cluster.</br>
 - Hippopotamus emerges as the closest terrestrial relative to whales, supporting evolutionary hypotheses.</br>
 - Phylogenetic results from automated and manual approaches align, validating the methodology.
