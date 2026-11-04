# 药物发现（Drug Discovery）文献调研报告

> 范围：经典奠基文献（CADD 时代至今）+ 前沿方法文献，重点在 AI/深度学习分子设计
> 体例：按主题分类，每篇附 1–3 句注解。文献格式为简化引用（作者/年份/标题/出处），未附卷页号。
> 标注：★ = 领域里程碑（必读）｜[经典] = 奠基性工作｜[前沿] = 近年活跃方向
> 说明：本清单基于通识性文献知识整理，个别出版细节（卷/页/DOI）未逐一核对，引用前请以 Google Scholar / PubMed 为准。

---

## 0. 领域脉络速览（30 秒版）

| 时代 | 主线 | 代表工作 |
|---|---|---|
| 1960s–1990s | QSAR、计算化学起步 | Hansch 1962；SMILES 1988 |
| 1980s–2010s | 分子对接、虚拟筛选、基于物理的方法 | DOCK 1982；AutoDock/Vina；Glide |
| 2017–2020 | 深度学习进入化学：图网络、SMILES 生成模型 | MPNN 2017；JT-VAE 2018；Chemprop 2019 |
| 2020–2021 | 蛋白质结构预测革命 + 首个 AI 制药里程碑 | AlphaFold2；DDR1 抑制剂（21 天） |
| 2022–2024 | 等变网络 + 扩散模型统治分子生成与对接 | DiffDock；TargetDiff；RFdiffusion；AlphaFold3 |
| 2024–2025 | LLM 进入药物研发全流程、多模态基础模型 | Tx-LLM；ChemCrow；Boltz-2；AlphaFlow |

---

## 1. 经典 CADD 基础（1962–2015）[经典]

1. **Hansch et al. (1962).** *Correlation of biological activity of phenoxyacetic acids with Hammett substituent constants and partition coefficients.* Nature. ★
   定量构效关系（QSAR）开山之作，把活性与电子/疏水参数建立线性回归，现代 QSAR 的起点。

2. **Free & Wilson (1964).** *A mathematical contribution to structure-activity studies.* J. Med. Chem.
   取代基贡献加和模型，与 Hansch 分析并列为 QSAR 两大流派。

3. **Kuntz et al. (1982).** *A geometric approach to macromolecule-ligand interactions.* J. Mol. Biol. ★
   DOCK 程序：把分子对接定义为"受体口袋与配体的几何互补匹配"，第一个通用对接算法。

4. **Goodford (1985).** *A computational procedure for determining energetically favorable binding sites.* J. Med. Chem.
   GRID 程序：用探针原子计算作用力场，是 CoMFA、药效团设计乃至分子对接打分函数的思想源头之一。

5. **Weininger (1988).** *SMILES, a chemical language and information system.* J. Chem. Inf. Comput. Sci. ★
   SMILES 线性分子表示，至今仍是机器学习分子表示的主流格式，直接影响后来所有基于字符串的生成模型。

6. **Bemis & Murcko (1996).** *The properties of known drugs. 1. Molecular frameworks.* J. Med. Chem.
   对已知药物做"骨架-侧链"分解，发现药物骨架高度集中（前 32 个骨架覆盖约一半药物），是分子库设计与骨架跃迁（scaffold hopping）的经典依据。

7. **Lipinski et al. (1997).** *Experimental and computational approaches to estimate solubility and permeability.* Adv. Drug Deliv. Rev. ★
   "五规则"（Rule of Five）：类药性（drug-likeness）经验判据，虚拟筛选初筛标准至今仍在用。

8. **Jones et al. (1997).** *Development and validation of a genetic algorithm for flexible docking.* J. Mol. Biol.
   GOLD：遗传算法柔性对接的代表，开创了启发式搜索配体构象的路线。

9. **Morris et al. (1998).** *Automated docking using a Lamarckian genetic algorithm and an empirical binding free energy function.* J. Comput. Chem.
   AutoDock：Lamarckian 遗传算法 + 经验打分函数，学术界使用最广的对接程序之一。

10. **Berman et al. (2000).** *The Protein Data Bank.* Nucleic Acids Res.
    PDB 蛋白质结构数据库，所有基于结构的药物设计（SBDD）的数据基础。

11. **Friesner et al. (2004).** *Glide: a new approach for rapid, accurate docking and scoring. 1.* J. Med. Chem.
    Schrödinger Glide：工业界虚拟筛选的主力对接工具，分层过滤 + 经验打分。

12. **Kitchen et al. (2004).** *Docking and scoring in virtual screening for drug discovery: methods and applications.* Nat. Rev. Drug Discov. ★
    对接与打分函数领域的权威综述，至今仍是该方向的标准入门文献。

13. **Irwin & Shoichet (2005).** *ZINC – a free database of commercially available compounds for virtual screening.* J. Chem. Inf. Model.
    ZINC 可购买化合物数据库（数亿级），虚拟筛选的标准化合物来源。

14. **Trott & Olson (2010).** *AutoDock Vina: improving the speed and accuracy of docking.* J. Comput. Chem. ★
    Vina：AutoDock 的重大改进版（速度提升约两个数量级），迄今引用量最高的对接程序论文，也是后来 DL 对接模型的性能对比基线。

15. **Rogers & Hahn (2010).** *Extended-connectivity fingerprints.* J. Chem. Inf. Model. ★
    ECFP（Morgan 指纹）：圆形拓扑指纹，分子相似性检索与 QSAR 的默认特征，至今仍是图网络时代的强基线。

16. **Sliwoski et al. (2014).** *Computational methods in drug discovery.* Pharmacol. Rev.
    CADD 全景综述（QSAR、药效团、对接、MD、虚拟筛选），AI 时代之前的学科总览。

17. **Wang et al. (2015).** *Accurate and reliable prediction of relative ligand binding potency in prospective drug discovery by way of a modern free energy calculation protocol and force field.* J. Am. Chem. Soc.
    Schrödinger FEP+：相对结合自由能微扰的大规模验证，确立了 FEP 在苗头化合物优化阶段的实用地位（至今仍是 AI 方法难以替代的"物理金标准"之一）。

18. **Genheden & Ryde (2015).** *The MM/PBSA and MM/GBSA methods to estimate ligand-binding affinities.* Expert Opin. Drug Discov.
    MM-PBSA/GBSA 综述：从 MD 轨迹快速估算结合自由能的性价比方法。

19. **Mendez et al. (2019).** *ChEMBL: towards direct deposition of bioassay data.* Nucleic Acids Res.
    ChEMBL：数百万条化合物-活性-靶标注释数据，绝大多数 ML 药物发现模型的训练数据来源。

20. **Kim et al. (2019).** *PubChem 2019 update.* Nucleic Acids Res.
    PubChem：化合物/生物活性公开数据库，与 ChEMBL 互补。

---

## 2. 深度学习基础与分子表示（2017–2020）[经典]

21. **Gilmer et al. (2017).** *Neural message passing for quantum chemistry.* ICML. ★
    MPNN 框架：消息传递图神经网络（GNN）的统一表述，几乎所有后续分子 GNN（DMPNN、SchNet 等）都可以看作其特例。

22. **Schütt et al. (2018).** *SchNet – a deep learning architecture for molecules and materials.* J. Chem. Phys. ★
    连续滤波卷积 + 原子间距离建模，第一个成功的分子连续卷积网络，直接催生了力场学习方向。

23. **Thomas et al. (2018).** *Tensor field networks: rotation- and translation-equivariant neural networks for 3D point clouds.* NeurIPS.
    3D 等变网络的理论奠基，把 SO(3)/SE(3) 群论引入深度学习，是后来所有等变分子模型的数学基础。

24. **Wu et al. (2018).** *MoleculeNet: a benchmark for molecular machine learning.* Chem. Sci. ★
    首个大规模分子机器学习基准（700+ 数据集任务），让分子性质预测可以横向比较。

25. **Yang et al. (2019).** *Analyzing learned molecular representations for property prediction.* J. Chem. Inf. Model.
    Chemprop（DMPNN）：把 MPNN 做到实用水平，至今仍是中小规模 QSAR 数据集上的强基线，也是许多组的第一选择。

26. **Krenn et al. (2020).** *Self-referencing embedded strings (SELFIES): a 100% robust molecular string representation.* Mach. Learn. Sci. Technol.
    SELFIES：保证任意字符串都能解码为合法分子，解决了 SMILES 生成中"语法无效"的老问题。

27. **Chithrananda et al. (2020).** *ChemBERTa: large-scale self-supervised pretraining for molecular property prediction.* arXiv.
    用 BERT 式掩码语言模型在百万级 SMILES 上预训练，开辟了"化学语言模型"路线。

28. **Hu et al. (2020).** *Strategies for pre-training graph neural networks.* ICLR.
    图级预训练策略（上下文/属性/图结构预测），分子 GNN 预训练的重要参考。

29. **Rong et al. (2020).** *Self-supervised graph transformer on large-scale molecular data.* NeurIPS.
    GROVER：分子图 Transformer + 大规模自监督预训练，图 Transformer 路线的早期代表作。

30. **Chen et al. (2018).** *The rise of deep learning in drug discovery.* Drug Discov. Today.
    早期 DL+药物发现综述，梳理了 2018 年前后的代表性应用（生成、预测、合成规划）。

---

## 3. 分子生成模型第一代：VAE / RNN / RL / GAN / 流（2017–2021）[经典]

31. **Gómez-Bombarelli et al. (2018).** *Automatic chemical design using a data-driven continuous representation of molecules.* ACS Cent. Sci. ★
    字符级 VAE + SMILES：把分子映射到连续隐空间并用贝叶斯优化搜索性质，是"隐空间分子设计"范式的开山作。

32. **Olivecrona et al. (2017).** *Molecular de-novo design through deep reinforcement learning.* J. Cheminform.
    REINVENT：策略梯度 RL 微调 RNN，把生成过程直接对准打分函数优化，工业界最常用的生成框架之一。

33. **Segler et al. (2018).** *Generating focused molecule libraries for drug discovery with recurrent neural networks.* ACS Cent. Sci.
    迁移学习 + RNN：用少量活性化合物 fine-tune 预训练 RNN，生成聚焦化合物库。

34. **Popova et al. (2018).** *Deep reinforcement learning for de novo drug design.* Sci. Adv.
    ReLeaSE：RNN + RL 双网络（生成器+预测器），"生成-预测-奖励"闭环设计的代表作。

35. **Jin et al. (2018).** *Junction tree variational autoencoder for molecular graph generation.* ICML. ★
    JT-VAE：树-图两级生成，保证图解码 100% 合法，图生成模型的奠基作。

36. **De Cao & Kipf (2018).** *MolGAN: an implicit generative model for small molecular graphs.* arXiv (ICML workshop).
    GAN 生成分子图 + RL 奖励引导，隐式生成模型的代表（GAN 在分子生成中后来因训练不稳定逐渐让位）。

37. **Liu et al. (2018).** *Learning deep generative models of graphs.* NeurIPS.
    CGVAE：图结构 VAE 的通用框架，被大量分子生成工作引用。

38. **Gebauer et al. (2019).** *Symmetry-adapted generation of 3D point sets for the targeted discovery of molecules.* NeurIPS.
    G-SchNet：最早直接在 3D 空间中逐原子生成分子的工作之一。

39. **Shi et al. (2020).** *GraphAF: a flow-based autoregressive model for molecular graph generation.* ICLR.
    自回归流模型生成图：把规范化流与逐节点生成结合，可计算精确似然。

40. **Zang & Wang (2020).** *MoFlow: an invertible flow model for generating molecular graphs.* ICML.
    图流模型：键流 + 原子流两步可逆生成，精确似然训练，生成质量一度领先。

41. **Bengio et al. (2021).** *Flow network based generative models for non-iterative diverse candidate generation.* NeurIPS.
    GFlowNet：把生成建模为流网络上的采样过程，训练目标是"以与奖励成正比的概率采样"，无需 RL 奖励工程，适合多样性优先的分子发现。

42. **Bagal et al. (2022).** *MolGPT: molecular generation using a transformer-decoder model.* J. Chem. Inf. Model.
    GPT 式自回归分子生成，与 CharRNN 类方法对比显示 Transformer 的优势。

---

## 4. 等变网络与几何深度学习（2020–2023）[前沿]

43. **Gasteiger et al. (2021).** *Fast and uncertainty-aware directional message passing for non-equilibrium molecules.* arXiv (DimeNet++).
    DimeNet/DimeNet++：方向消息传递（键角信息）显著提升 QM9 等任务精度，是当时分子性质预测 SOTA。

44. **Satorras et al. (2021).** *E(n) equivariant graph neural networks.* ICML.
    EGNN：无需群表示理论的简单 E(n) 等变网络设计，成为大量后续工作的基础组件。

45. **Schütt et al. (2021).** *Equivariant message passing for the prediction of tensorial properties and molecular spectra.* ICML.
    PaiNN：向量型消息传递，等变 + 快速，力场和性质预测两用。

46. **Batatia et al. (2022).** *MACE: higher order equivariant message passing neural networks for fast and accurate force fields.* NeurIPS.
    MACE 系列：高阶等变消息传递力场，Foundation Model（MACE-MP-0）化后成为通用势函数的主流选择。

47. **Zhou et al. (2023).** *Uni-Mol: a universal 3D molecular representation learning framework.* ICLR. ★
    Uni-Mol：3D 构象级预训练（原子对表示 + 位置预测），覆盖性质预测、构象生成、口袋预测三大任务的通用框架。

48. **Lu et al. (2023).** *Uni-Mol+: a deeper integration of molecular representation with quantum chemistry.* ICLR.
    Uni-Mol 升级版：引入量子化学描述符与构象优化，精度进一步提升。

49. **Atz, Grisoni & Schneider (2021).** *Geometric deep learning on molecular representations.* WIREs Comput. Mol. Sci.
    几何深度学习综述，适合作为从"图/序列"到"3D/等变"升级的入门地图。

---

## 5. 蛋白质结构预测与设计（2021–2025）[里程碑+前沿]

50. **Jumper et al. (2021).** *Highly accurate protein structure prediction with AlphaFold.* Nature. ★
    AlphaFold2：CASP14 颠覆性成果，把单链结构预测推进到实验精度，重塑了整个结构生物与药物发现。

51. **Baek et al. (2021).** *Accurate prediction of protein structures and interactions using a three-track neural network.* Science. ★
    RoseTTAFold：三轨网络（序列/距离/坐标），与 AF2 同期、完全独立达到接近精度，且开源可商用。

52. **Varadi et al. (2022).** *AlphaFold Protein Structure Database.* Nucleic Acids Res.
    AFDB：百万级预测结构免费开放，让"无结构靶点"的 SBDD 成为可能。

53. **Evans et al. (2022).** *Protein complex prediction with AlphaFold-Multimer.* bioRxiv.
    AlphaFold-Multimer：复合物预测扩展，蛋白-蛋白相互作用界面的标准工具。

54. **Merchant et al. (2023).** *Scaling structural coverage of the AlphaFold database to 200 million proteins.* Nature.
    AFDB 扩展到 2 亿结构，覆盖几乎所有已知蛋白。

55. **Lin et al. (2023).** *Evolutionary-scale prediction of atomic-level protein structure with a language model.* Science. ★
    ESMFold：纯语言模型（无 MSA）做结构预测，精度略低但速度快两个数量级，适合宏基因组规模筛查，也是"蛋白质语言模型"路线的证明。

56. **Dauparas et al. (2022).** *Robust deep learning-based protein sequence design using ProteinMPNN.* Science. ★
    ProteinMPNN：给定骨架反推序列的图网络，蛋白设计（固定骨架）的标配工具，成功率远超 Rosetta 时代方法。

57. **Watson et al. (2023).** *De novo design of protein structure and function with RFdiffusion.* Nature. ★
    RFdiffusion：扩散模型做蛋白骨架从头设计，功能蛋白、结合蛋白设计均达实用水平。

58. **Ingraham et al. (2023).** *Illuminating protein space with a programmable generative model.* Nature.
    Chroma：可编程约束（对称性、形状、功能基序）的蛋白生成扩散模型。

59. **Yim et al. (2023).** *SE(3) diffusion model with application to protein backbone generation.* ICML.
    FrameDiff：SE(3) 上定义蛋白骨架扩散，理论最干净的蛋白扩散框架之一。

60. **Alamdari et al. (2023).** *Protein generation with evolutionary diffusion: sequence is all you need.* bioRxiv.
    EvoDiff：序列空间蛋白生成，代表"生成+预测"分开的路线。

61. **Ferruz et al. (2022).** *ProtGPT2 is a deep unsupervised language model for protein design.* Nat. Commun.
    ProtGPT2：蛋白语言模型无监督生成，自然进化式的新蛋白序列。

62. **Abramson et al. (2024).** *Accurate structure prediction of biomolecular interactions with AlphaFold 3.* Nature. ★
    AlphaFold3：统一扩散框架预测蛋白-配体、蛋白-核酸、修饰等复合物，配体结合预测虽非"对接级"，但作为通用结构预测基座影响巨大。

63. **Krishna et al. (2024).** *Generalized biomolecular modeling and design with RoseTTAFold All-Atom.* Science.
    RFAA：全原子（蛋白+小分子+核酸）建模与设计，可设计结合口袋，与 AF3 同期开源。

64. **Chai Discovery (2024).** *Chai-1: decoding the molecular interactions of life.* bioRxiv.
    Chai-1：多模态（序列/MSA/模板）复合物预测，多项基准与 AF3 相当，权重开放商用。

65. **Jing et al. (2024).** *AlphaFlow: improved protein structure prediction and generation with flow matching.* arXiv (后刊于 JACS, 2025).
    AlphaFlow：AlphaFold 架构 + flow matching，结构预测与构象系综生成一体化。

66. **Boltz-2 (2025).** *Boltz-2: robust, fast, and accurate biomolecular structure prediction with multimodal diffusion.* bioRxiv/GitHub.
    Boltz-2：MIT 开源的多模态扩散复合物预测模型，在配体结合预测基准上表现突出，是 AF3 最强开源替代之一。

67. **Zambaldi et al. (2024).** *De novo design of high-affinity protein binders with AlphaProteo.* Nature.
    AlphaProteo：给定靶标生成高亲和蛋白 binder（实验验证纳摩尔级），生成式蛋白设计落地标志。

---

## 6. 结构基础药物设计（SBDD）与深度学习对接（2021–2025）[前沿]

68. **McNutt et al. (2021).** *GNINA 1.0: molecular docking with deep learning.* J. Cheminform.
    GNINA：CNN 打分函数 + 蒙特卡洛采样，第一个实用化深度学习对接程序，开源易用。

69. **Stärk et al. (2022).** *EquiBind: geometric deep learning for drug binding structure prediction.* ICML.
    EquiBind：E(3) 等变网络直接预测结合构象（回归式，无需采样），把"对接"重新表述为几何预测问题。

70. **Corso et al. (2023).** *DiffDock: diffusion steps, twists, and turns for molecular docking.* ICLR (Outstanding Paper). ★
    DiffDock：在配体自由度（平移/旋转/扭转）上定义扩散过程，盲对接精度大幅超越 Vina/Glide 等传统工具，是 DL 对接的转折点。

71. **Yu et al. (2023).** *FABind: fast and accurate protein-ligand binding.* NeurIPS.
    FABind：快速姿态初始化 + 精细修正两阶段网络，速度比 DiffDock 快一个量级、精度相当。

72. **Qiao et al. (2024).** *State-specific protein-ligand complex structure prediction with a multiscale deep generative model.* Nat. Mach. Intell. (NeuralPLexer).
    NeuralPLexer：对接+构象变化联合建模，可处理柔性口袋，向"生成式结构预测"融合。

73. **Luo et al. (2022).** *A 3D generative model for structure-based drug design.* ICLR.
    3D 自回归模型：在蛋白口袋中逐原子生成 3D 配体，SBDD 3D 生成的奠基作。

74. **Peng et al. (2022).** *Pocket2Mol: efficient molecular sampling based on 3D protein pockets.* ICML.
    Pocket2Mol：几何约束图网络逐原子生成，强调化学合理性与效率。

75. **Ragoza et al. (2022).** *Generating 3D molecules conditional on receptor binding sites with deep generative models.* J. Chem. Inf. Model.
    LiGANN：将分子生成视为"密度学习"（like AF2 的密度图），与 AF2 风格统一的 SBDD 生成路线。

76. **Schneuing et al. (2023).** *Structure-based drug design with equivariant diffusion models.* ICLR.
    DiffSBDD：口袋条件 3D 扩散生成 + 分子图重建，SBDD 进入扩散模型时代。

77. **Guan et al. (2023).** *3D equivariant diffusion for target-aware molecule generation and affinity prediction.* ICLR.
    TargetDiff（含 DecompDiff）：3D 原子坐标扩散 + 局部结构约束，同时给出生成与亲和力预测，SBDD 扩散模型标杆。

78. **Igashov et al. (2023).** *Equivariant 3D-conditional diffusion model for molecular linker design.* arXiv.
    DiffLinker：片段连接（linker design）任务的扩散模型，输入两个片段生成中间连接区。

79. **Lei et al. (2024).** *Molecular dynamics of diffusion for virtual screening.* ICLR.
    MDM：无口袋结构时用"虚拟受体"做 3D 生成筛选，扩散模型的虚拟筛选应用。

80. **Gao et al. (2024).** *DrugCLIP: contrastive protein-molecule representation learning for virtual screening.* arXiv / Nat. Mach. Intell.
    DrugCLIP：蛋白-分子对比学习（CLIP 式）+ 对接集成，把虚拟筛选做成检索问题。

---

## 7. 扩散模型与 3D 分子生成（2020–2024）[前沿]

81. **Ho et al. (2020).** *Denoising diffusion probabilistic models.* NeurIPS. ★
    DDPM：扩散生成模型奠基论文（虽是通用 ML，但整个分子扩散浪潮由此而起）。

82. **Song et al. (2021).** *Score-based generative modeling through stochastic differential equations.* ICLR.
    Score SDE：统一扩散与分数匹配的连续框架，理论根基。

83. **Hoogeboom et al. (2022).** *Equivariant diffusion for molecule generation in 3D.* ICML.
    E(3) Equivariant Diffusion Model（EDM）：3D 分子坐标的等变扩散生成，稳定分子的 3D 生成代表作。

84. **Xu et al. (2022).** *GeoDiff: a geometric diffusion model for molecular conformation generation.* ICLR.
    GeoDiff：构象生成扩散模型，聚焦多样且合理的低能构象。

85. **Jing et al. (2022).** *Torsional diffusion for molecular conformer generation.* NeurIPS.
    Torsional Diffusion：只在扭转角空间扩散（保持键长键角），构象生成速度与质量俱佳。

86. **Vignac et al. (2023).** *DiGress: discrete denoising diffusion for graph generation.* ICLR.
    DiGress：离散扩散生成分子图（原子类型+键类型+电荷），图生成任务 SOTA。

87. **Lipman et al. (2023).** *Flow matching for generative modeling.* ICLR.
    Flow Matching：连续归一化流训练新范式，比扩散更快，成为 2024 年后主流生成框架之一。

88. **Klein et al. (2023).** *Equivariant flow matching.* NeurIPS.
    把 flow matching 与 SE(3) 等变网络结合，3D 分子/蛋白生成的高效方案。

89. **Anstine & Isayev (2023).** *Generative models as an emerging paradigm in the chemical sciences.* JACS Au.
    化学生成模型综述：从 SMILES 到 3D 扩散的完整谱系，适合系统性补课。

---

## 8. 大语言模型（LLM）与药物发现（2022–2025）[前沿]

90. **Ross et al. (2022).** *Large-scale chemical language representations capture molecular structure and properties.* Nat. Mach. Intell. ★
    MolFormer：基于分子指纹的化学语言模型预训练，证明"化学 LM 规模化"有效，后续 MolFormer-XL 等的基础。

91. **Edwards et al. (2022).** *Translation between molecules and natural language.* EMNLP.
    MolT5：分子-自然语言互译（分子→描述、描述→分子），把化学知识引入 T5 架构。

92. **Fang et al. (2023).** *Mol-Instructions: a large-scale biomolecular instruction dataset for large language models.* arXiv.
    Mol-Instructions：分子/蛋白/文本指令微调数据集，LLM+生物分子指令跟随的常用数据。

93. **Boiko et al. (2023).** *Autonomous chemical research with large language models.* Nature.
    Coscientist：GPT-4 驱动、调用工具（文档检索、代码执行、自动化仪器）自主完成化学实验设计，LLM 智能体路线的标志。

94. **Bran et al. (2024).** *Augmenting large language models with chemistry tools.* Nat. Mach. Intell.
    ChemCrow：LLM + 18 种化学工具（合成规划、性质预测、检索），LLM 做"化学任务调度中枢"的范式。

95. **Chaves et al. (2025).** *Tx-LLM: a large language model for therapeutics.* Nature. ★
    Tx-LLM：多任务治疗学 LLM（709 个任务，覆盖小分子、蛋白、核酸、适应症、ADMET），药物研发任务统一建模的代表作。

96. **AlphaChem (2025).** *Google DeepMind.* preprint/GitHub.
    AlphaChem：DeepMind 面向逆合成与反应预测的强化学习框架（AlphaZero 思想），验证已知合成路线并发现更优路线。

---

## 9. 里程碑应用案例 [经典+前沿]

97. **Zhavoronkov et al. (2019).** *Deep learning enables rapid identification of potent DDR1 kinase inhibitors.* Nat. Biotechnol. ★
    Insilico Medicine：GENTRL（GAN+RL 生成）从零设计 DDR1 抑制剂，46 天出苗头（含合成验证仅 21 天设计周期），"AI 制药"出圈之作。

98. **Segler et al. (2018).** *Planning chemical syntheses with deep neural networks and symbolic AI.* Nature. ★
    3N-MCTS：将逆合成视为树搜索（类似 AlphaGo），双盲测试中路线被化学家偏好率超过文献路线，AI 逆合成里程碑。

99. **Stokes et al. (2020).** *A deep learning approach to antibiotic discovery.* Cell. ★
    Halicin：用 GNN 从 ZINC15 库筛选出结构全新的广谱抗生素并实验验证，DL 药物重定向/从头发现范式。

100. **Wong et al. (2024).** *Discovery of a structural class of antibiotics with explainable deep learning.* Nature.
     Abaucin：图解释（可解释 GNN）+ 大规模筛选发现抗 MRSA 新结构类型，强调"可解释性"的实际价值。

101. **Ren et al. (2025).** *A small-molecule TNIK inhibitor (INS018_055) for idiopathic pulmonary fibrosis: Phase 2a results.* Nat. Biotechnol.
     Insilico Medicine：从靶点发现到 IIa 期临床的全程 AI 驱动管线（第一例公布 II 期结果的 AI 设计药物），AI 制药可复现性争论的重要数据点。

102. **Swanson et al. (2024).** *ADMET-AI: a machine learning ADMET platform for evaluation of large-scale chemical libraries.* Bioinformatics.
     ADMET-AI：Chemprop 系模型包 + 大规模 ADMET 预测平台，开源、适合亿级库过滤。

---

## 10. 数据资源与基准 [经典+前沿]

103. **Liu et al. (2017).** *PDBbind database: protein-ligand binding affinities.* J. Med. Chem. (v2017 版).
     PDBbind：蛋白-配体复合物结构 + 实验亲和力，对接打分函数与 DL 亲和力模型的核心训练/评估集。

104. **Francoeur et al. (2020).** *Three-dimensional convolutional neural networks and a cross-docked dataset for pose prediction.* J. Chem. Inf. Model.
     CrossDocked2020：跨对接构象数据集，DiffDock 等几乎所有 DL 对接模型的训练数据。

105. **Axelrod & Gómez-Bombarelli (2022).** *GEOM: energy-annotated molecular conformations.* Sci. Data.
     GEOM：450K 分子的 DFT 标注构象集，3D 生成/构象模型的默认基准。

106. **Huang et al. (2021).** *Therapeutics Data Commons: machine learning datasets and tasks for drug discovery and development.* NeurIPS. ★
     TDC：药物研发全流程（靶点-分子-临床）统一基准库，AI 制药评估的标准基础设施（已有 TDC-3 扩展）。

107. **Tingle et al. (2023).** *ZINC-22 – a free multi-billion-scale database of tangible compounds for ligand discovery.* J. Chem. Inf. Model.
     ZINC-22：370 亿级可购买化合物空间，大规模虚拟筛选数据底座。

108. **Grygorenko et al. (2020).** *Generating multibillion chemical space of readily accessible screening compounds.* iScience.
     Enamine REAL 空间：数十亿级"可合成即买"化合物枚举，DEL/虚拟筛选的现实化学空间边界。

109. **Luukkonen et al. (2024).** *Polaris: a guided drug discovery platform for benchmarking.* arXiv / Chem. Sci.
     Polaris：众包基准平台（含分时评估防止数据泄露），试图解决药物发现基准"刷榜但不可复现"的问题。

---

## 11. 综合性综述（按主题速查）[经典]

| 主题 | 推荐综述 |
|---|---|
| CADD 全景（传统） | Sliwoski et al. (2014), Pharmacol. Rev. |
| 对接与虚拟筛选 | Kitchen et al. (2004), Nat. Rev. Drug Discov. |
| ML 在药物发现的应用 | Vamathevan et al. (2019), Nat. Rev. Drug Discov. ★ |
| AI 辅助药物设计概念 | Yang et al. (2019), Chem. Rev. |
| AI 时代药物设计反思 | Schneider et al. (2020), Nat. Rev. Drug Discov. |
| 分子几何深度学习 | Atz et al. (2021), WIREs Comput. Mol. Sci. |
| 生成模型谱系 | Anstine & Isayev (2023), JACS Au |

---

## 12. 综合分析：趋势、争议与空白

### 12.1 方法演进主线

**表示层的三次升级**：1D 字符串/指纹（ECFP→SMILES）→ 2D 分子图（MPNN/JT-VAE/Chemprop）→ 3D 等变表示（SchNet→EGNN→MACE/Uni-Mol）。每一次升级都伴随精度跃迁，当前 SOTA 性质预测与生成几乎全部是 3D/等变架构；但 2D 方法在虚拟筛选规模任务上仍有性价比优势。

**生成范式五次迭代**：VAE 隐空间优化（Gómez-Bombarelli 2018）→ RNN/RL 序列生成（REINVENT/ReLeaSE 2017-18）→ 流模型与图生成（MoFlow/GraphAF 2020）→ 扩散模型（Hoogeboom 2022 → TargetDiff/DiffDock 2023）→ flow matching（2024 起渐成主流）。整体趋势是：**从"优化隐空间"到"在 3D 几何空间中生成合法分子"，从 1D/2D 到以口袋为条件的 3D 生成**。

**对接范式的转移**：传统采样+打分（Vina/Glide）→ 回归式直接预测（EquiBind）→ 扩散式生成姿态（DiffDock）。注意 2024-2025 的新动向是**结构预测与对接合流**（AF3/RFAA/Boltz-2 把"配体在口袋里的构象"作为复合物预测的一部分输出），对接可能被吸收进通用结构预测基座。

**蛋白质侧的范式统一**：结构预测（AF2）→ 序列设计（ProteinMPNN）→ 骨架设计（RFdiffusion）→ 全原子复合物建模与设计（RFAA/AF3/Chai-1/Boltz-2）→ 结合剂设计（AlphaProteo）。"预测-设计"闭环在蛋白侧已基本打通，小分子侧尚未达到同等成熟度。

### 12.2 当前前沿热点（2024–2025）

1. **复合物级基础模型竞争**：AF3（闭源权重） vs Chai-1 vs Boltz-2 vs RFAA 的开源竞赛，配体结合姿态预测质量是核心战场。
2. **LLM/多模态大模型进入研发全流程**：Tx-LLM 式任务统一 vs ChemCrow/Coscientist 式智能体调度，两条路线并存；LLM 直接做分子生成尚未证明优于专用小模型，但作为"研发流程编排者"的落地更快。
3. **flow matching 替代扩散**：训练/采样更快，AlphaFlow 与等变流匹配在蛋白-分子两侧同步推进。
4. **生成-验证闭环与自动化实验**：生成模型输出进入湿实验验证（Insilico 管线、自驱动实验室），评价标准从"benchmark 分数"转向"实验命中率"。
5. **可解释性与不确定性量化**：Abaucin 式的图解释、TDC/Polaris 的数据泄露防护，反映领域从"刷 SOTA"转向"可信部署"。

### 12.3 主要争议与未解决问题

- **benchmark 与现实的差距**：CrossDocked/DOCKSTRING 等基准上的 SOTA（如 DiffDock 相对 Vina 的倍数提升）在真实苗头筛选场景中往往缩水；Polaris 等平台试图修复但尚未形成共识。
- **生成分子的可合成性**：3D/图生成模型产出的分子常含合成难点，SA score 等代理指标粗糙；与逆合成模型（3N-MCTS、AlphaChem）联动的"生成即合成"闭环仍缺标准方案。
- **AI 设计的药物是否真的"AI 设计"**：Insilico TNIK 抑制剂等案例中人类专家干预程度存在争议（Zhavoronkov 2019 被质疑"21 天"叙事），领域缺乏披露标准。
- **自由能级别精度缺口**：DL 亲和力预测整体尚未稳定达到 FEP 级别精度，物理方法在苗头优化阶段仍不可替代。
- **小分子与蛋白两侧成熟度不对称**：蛋白设计已进入"从头设计-实验闭环"时代（AlphaProteo），小分子 3D 生成尚无同级别的端到端实证。
- **LLM 幻觉与化学正确性**：LLM 直接产出分子/路线存在合法性与安全性风险，工具增强（ChemCrow）是当前折中方案。
- **数据瓶颈**：高质量活性/结合数据远少于图像文本；隐私与专利墙导致药企数据难以共享，催生联邦学习与生成数据增广研究。

### 12.4 建议的入门阅读路径

- 第一天（领域地图）：Sliwoski 2014 → Vamathevan 2019 → Schneider 2020
- 第二天（表示与预测）：Weininger 1988 → ECFP 2010 → MPNN 2017 → Chemprop 2019 → Uni-Mol 2023
- 第三天（生成主线）：Gómez-Bombarelli 2018 → JT-VAE 2018 → MoFlow 2020 → EDM 2022 → DiGress 2023
- 第四天（SBDD 与对接）：Vina 2010 → GNINA 2021 → EquiBind 2022 → DiffDock 2023 → TargetDiff 2023
- 第五天（蛋白与前沿）：AF2 2021 → ProteinMPNN 2022 → RFdiffusion 2023 → AF3 2024 → Tx-LLM 2025

---

## 13. 局限性与说明

1. 本清单为"广度优先"的粗粒度调研：覆盖 10 个主题约 110 条，未做系统性数据库检索（无 PRISMA 流程），可能存在重要遗漏（如分子动力学增强采样、DEL 计算筛选、RNA/共价药物、抗体验证等方向仅点到为止）。
2. 引用格式为简化版：卷/期/页码与部分 DOI 未逐一核对；标注 arXiv/preprint 的条目请以正式发表版本为准。
3. 截至 2025 年末：该领域月均产出量大，2025 下半年的最新工作（如 TDC-3、AlphaFold 更新、更多 LLM 基座）未完全覆盖，建议配合 Google Scholar 提醒持续跟踪。
4. AI 辅助调研声明：本报告由 AI 工具基于领域知识整理生成，文献选择存在主观性，正式引用前请逐一核对原始出处。
