
**Weight-Calculative AI Architecture** is a new-generation artificial intelligence framework based on the "Weight-Calculativism" cognitive theory. Starting from the first principles of cognitive science, it reconstructs human cognitive and decision-making processes through three core pillars: **logical atoms, pointing and comparison operations, and transparent weight calculation**, forming a theoretical model with fundamental explainability and value alignment potential. 

The project outlines a concrete engineering pathway—through **hierarchical cognitive library construction, graph-algorithm-driven symbolic computation, global workspace scheduling, and hybrid decision-making mechanisms**—to transform this theoretical vision into a buildable, verifiable, and scalable software system. Currently in the stage of theoretical exposition and conceptual validation, it includes two basic demonstration models that showcase core decision logic and cognitive workflows.

**We welcome researchers, engineers, and thinkers to join this open exploration—to collaborate, build, and evolve this architecture together toward transparent, value-aligned, and human-compatible general intelligence.**



## Cognitive Architecture Workflow

### Diagram Overview
This diagram illustrates the complete cognitive-decision workflow of the Weight-Calculative AI architecture, divided into three main systems:

1. **Perception System** (Blue): Processes sensory input into logical atoms
2. **Central System** (Yellow): Coordinates information integration and high-level decision-making  
3. **Decision System** (Red): Executes weight calculation and action selection

### Key Components
- **Logical Atoms**: Fundamental cognitive units (Red, Circular, Edibility)
- **Pointing Operations**: Dashed arrows showing activation propagation
- **Weight Calculation**: Core decision mechanism (Weight = Benefit × Probability)
- **Global Workspace**: Central computation area for information integration

````markdown
## Cognitive Architecture Workflow

```mermaid
graph TB
    %% ==================== 样式定义 ====================
    classDef perception fill:#e6f3ff,stroke:#0066cc,stroke-width:2px
    classDef central fill:#fff9e6,stroke:#cc9900,stroke-width:2px
    classDef decision fill:#ffe6e6,stroke:#cc0000,stroke-width:2px
    
    %% ==================== 第一部分：视觉感知过程 ====================
    subgraph PerceptionSystem[Perception System]
        direction TB
        SENSOR[Visual Sensor] --> PRE[Preprocessor<br/>Thalamus]
        PRE --> VIS[Text Visual Area]
        VIS --> CON[Concept Area]
        
        CON -.-> A1[Red]
        CON -.-> A2[Circular]
        CON -.-> A3[Edibility]
    end
    
    %% ==================== 第二部分：饥饿决策过程 ====================
    subgraph DecisionSystem[Decision System]
        direction TB
        NERV[Stomach Nerves] --> HUN[Hunger Sensation]
        HUN --> GOAL[Temporary Goal:<br/>Solve Hunger]
        GOAL --> ACT[Activate Cognitive<br/>Library]
        ACT --> SOL[Find Solution: Eat]
        SOL --> ALT[Possible Actions]
        
        ALT --> EAT[Eat Apple<br/>Weight: High]
        ALT --> NO[Not Eat Apple<br/>Weight: Low]
        
        EAT --> CAL[Calculate Weights]
        NO --> CAL
        CAL --> COMP[Compare Weights]
        COMP --> DEC[Final Decision]
    end
    
    %% ==================== 第三部分：中央系统 ====================
    subgraph CentralSystem[Central System]
        CENT[Central Computation Area<br/>Brain]
        DM[Decision Module]
    end
    
    %% ==================== 连接线 ====================
    %% 视觉感知流程
    SENSOR -- Visual Info --> CENT
    SENSOR -- Visual Info --> PRE
    CON -- Returns "Apple" --> CENT
    
    %% 认知原子激活（点线）
    CON -. Activates .-> A1
    CON -. Activates .-> A2
    CON -. Activates .-> A3
    
    %% 饥饿信号流程
    NERV -- Hunger Signal --> CENT
    CENT --> HUN
    
    %% 连接到认知系统（红色粗线）
    SOL -. Points to .-> A3
    SOL -. Points to Apple .-> CON
    
    %% 决策流程
    SOL --> ALT
    DEC --> DM
    
    %% 反馈到中枢（蓝色虚线）
    DEC -. Decision Feedback .-> CENT
    
    %% ==================== 应用样式 ====================
    class PerceptionSystem perception
    class DecisionSystem decision
    class CentralSystem central
```

### 图表说明
- **感知系统（蓝色）**：处理感官输入，生成逻辑原子
- **决策系统（红色）**：执行权重计算和行动选择
- **中央系统（黄色）**：信息整合与高层决策协调
- **点线**：指向操作（Pointing Operations）
- **红色连接**：权重计算路径
- **蓝色虚线**：决策反馈回路
