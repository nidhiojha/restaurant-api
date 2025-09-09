# System Architecture Diagram

## Tech Stack

### Frontend/Client Technologies
- **Client VM**: Windows/Linux Virtual Machine
- **Bot Framework**: Python/Node.js for SAP automation
- **Screenshot Capture**: Selenium WebDriver, Puppeteer, or similar automation tools
- **File Processing**: Native OS file system operations

### Backend/Server Technologies
- **Existing Project**: REST API (Node.js/Python/Java)
- **API Gateway**: AWS API Gateway, Kong, or similar
- **Database**: PostgreSQL/MySQL/MongoDB for project data

### Cloud & Storage
- **S3 Storage**: AWS S3 for .exe file and dependencies storage
- **Cloud Provider**: AWS/Azure/GCP
- **File Transfer**: AWS CLI, SDK, or custom upload/download scripts

### Network & Security
- **VPN**: OpenVPN, WireGuard, or enterprise VPN solution
- **Network Security**: Firewall rules, VPC configuration
- **Authentication**: OAuth 2.0, JWT tokens, or enterprise SSO

### SAP Integration
- **SAP System**: SAP S/4HANA Cloud (SAAS)
- **SAP Automation**: SAP GUI Scripting, SAP RFC, or UI automation
- **Authentication**: SAP Single Sign-On (SSO) or basic authentication

### Monitoring & Logging
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana) or CloudWatch
- **Monitoring**: Prometheus, Grafana, or cloud monitoring solutions
- **Error Tracking**: Sentry or similar error tracking service

### DevOps & Deployment
- **Containerization**: Docker (optional for bot deployment)
- **CI/CD**: GitHub Actions, GitLab CI, or Jenkins
- **Infrastructure**: Terraform or CloudFormation for IaC
- **Version Control**: Git

## Network Integration and SAP Bot Feature

```mermaid
graph TB
    subgraph "Existing Project Network"
        EP[Existing Project]
        API[API Gateway]
    end
    
    subgraph "Intermediate Channel"
        IC[Intermediate Channel]
        TRANSFER[File Transfer]
    end
    
    subgraph "Client Network (VPN Protected)"
        VM[Client VM]
        S3[S3 Download]
        EXE[.exe File + Dependencies]
        BOT[SAP Bot]
        OUTPUT[Output Folder]
    end
    
    subgraph "SAP SAAS System (VPN Protected)"
        SAP[SAP System]
        LOGIN[Login Interface]
        SCREEN[Screenshot Capture]
    end
    
    subgraph "File Structure"
        EXE_FOLDER[.exe File Folder]
        EXE_FILE[Executable File]
        CONFIG[Configuration Files]
        DEPENDENCIES[Dependencies]
    end
    
    %% Main Flow
    EP -->|1. Provide .exe| IC
    IC -->|2. Upload to S3| S3
    S3 -->|3. Download| VM
    VM -->|4. Extract & Setup| EXE_FOLDER
    EXE_FOLDER -->|Contains| EXE_FILE
    EXE_FOLDER -->|Contains| CONFIG
    EXE_FOLDER -->|Contains| DEPENDENCIES
    
    EXE_FILE -->|5. Execute| BOT
    BOT -->|6. Login| SAP
    SAP -->|7. Authentication| LOGIN
    LOGIN -->|8. Success| BOT
    BOT -->|9. Collect Screenshots| SCREEN
    SCREEN -->|10. Store| OUTPUT
    
    %% Network Connections
    IC -.->|VPN Access| VM
    VM -.->|VPN Protected| SAP
    
    %% Styling
    classDef network fill:#e1f5fe
    classDef intermediate fill:#fff9c4
    classDef client fill:#f3e5f5
    classDef sap fill:#e8f5e8
    classDef files fill:#fff3e0
    
    class EP,API network
    class IC,TRANSFER intermediate
    class VM,S3,EXE,BOT,OUTPUT client
    class SAP,LOGIN,SCREEN sap
    class EXE_FOLDER,EXE_FILE,CONFIG,DEPENDENCIES files
```

## Process Flow Diagram

```mermaid
sequenceDiagram
    participant EP as Existing Project
    participant IC as Intermediate Channel
    participant S3 as S3 Storage
    participant VM as Client VM
    participant EXE as .exe File
    participant BOT as SAP Bot
    participant SAP as SAP SAAS
    participant OUTPUT as Output Folder
    
    EP->>IC: 1. Provide .exe file with dependencies
    IC->>S3: 2. Upload to S3 storage
    S3->>VM: 3. Download .exe file with dependencies
    VM->>EXE: 4. Extract and prepare files
    VM->>EXE: 5. Execute .exe file
    EXE->>BOT: 6. Initialize bot process
    BOT->>SAP: 7. Connect to SAP system (VPN)
    SAP-->>BOT: 8. Authentication response
    BOT->>SAP: 9. Login to SAP
    SAP-->>BOT: 10. Login successful
    BOT->>SAP: 11. Navigate and collect data
    BOT->>BOT: 12. Capture screenshots
    BOT->>OUTPUT: 13. Store screenshots in single file
```

## Network Topology Diagram

```mermaid
graph LR
    subgraph "Network A - Existing Project"
        A1[Project Server]
        A2[API Services]
        A3[Database]
    end
    
    subgraph "Intermediate Channel"
        IC[Intermediate Channel]
        S3[S3 Storage]
    end
    
    subgraph "Network B - Client Environment (VPN Protected)"
        B1[Client VM]
        B2[File System]
        B3[Bot Process]
    end
    
    subgraph "SAP Network (VPN Protected)"
        SAP[SAP SAAS System]
    end
    
    A1 -->|Provide .exe| IC
    IC -->|Upload| S3
    S3 -->|Download| B1
    B1 -->|Store Files| B2
    B1 -->|Execute| B3
    B3 -->|Connect VPN| SAP
    B3 -->|Store Results| B2
    
    classDef networkA fill:#bbdefb
    classDef intermediate fill:#fff9c4
    classDef networkB fill:#c8e6c9
    classDef sap fill:#e8f5e8
    
    class A1,A2,A3 networkA
    class IC,S3 intermediate
    class B1,B2,B3 networkB
    class SAP sap
```


### 1.1 Business Objectives
- Automate SAP screenshot collection process
- Integrate cloud storage for output file management
- Enhance security through centralized file storage
- Reduce manual intervention in the file handling process
- Maintain compatibility with existing Windows-based systems

---

## 2. Business Context

### 2.1 Current State
- Existing Autonomous Config project operates in a network environment
- Manual .exe file upload process through intermediate channel
- Output files stored locally on client VM
- Windows-based execution environment
- VPN-protected client network

### 2.2 Desired Future State
- Automated output file upload to cloud storage
- Centralized file management and access
- Enhanced security through cloud storage integration
- Streamlined file retrieval process
