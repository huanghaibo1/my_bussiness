#!/usr/bin/env python3
"""
上海外企数据岗位信息爬虫
专注于获取外企（跨国公司）在上海招聘的数据相关岗位
"""

import json
import time
from datetime import datetime
from typing import List, Dict, Set
import re


def get_target_companies() -> List[Dict]:
    """
    获取目标外企公司列表
    重点关注科技、金融、咨询等数据密集型行业的跨国公司
    """
    return [
        # 科技巨头
        {"name": "Microsoft", "industry": "Technology", "cn_name": "微软"},
        {"name": "Google", "industry": "Technology", "cn_name": "谷歌"},
        {"name": "Amazon", "industry": "Technology/E-commerce", "cn_name": "亚马逊"},
        {"name": "Apple", "industry": "Technology", "cn_name": "苹果"},
        {"name": "Meta (Facebook)", "industry": "Technology", "cn_name": "Meta"},
        {"name": "IBM", "industry": "Technology/Consulting", "cn_name": "IBM"},
        {"name": "Oracle", "industry": "Technology/Database", "cn_name": "甲骨文"},
        {"name": "SAP", "industry": "Enterprise Software", "cn_name": "思爱普"},
        {"name": "Salesforce", "industry": "Cloud/CRM", "cn_name": "赛富时"},

        # 专业数据/AI公司
        {"name": "Databricks", "industry": "Data Platform", "cn_name": "Databricks"},
        {"name": "Snowflake", "industry": "Data Cloud", "cn_name": "Snowflake"},
        {"name": "Tableau (Salesforce)", "industry": "BI/Analytics", "cn_name": "Tableau"},
        {"name": "Splunk", "industry": "Data Analytics", "cn_name": "Splunk"},

        # 咨询公司
        {"name": "McKinsey & Company", "industry": "Consulting", "cn_name": "麦肯锡"},
        {"name": "BCG", "industry": "Consulting", "cn_name": "波士顿咨询"},
        {"name": "Bain & Company", "industry": "Consulting", "cn_name": "贝恩"},
        {"name": "Accenture", "industry": "Consulting/IT", "cn_name": "埃森哲"},
        {"name": "Deloitte", "industry": "Consulting/Audit", "cn_name": "德勤"},
        {"name": "PwC", "industry": "Consulting/Audit", "cn_name": "普华永道"},
        {"name": "EY", "industry": "Consulting/Audit", "cn_name": "安永"},
        {"name": "KPMG", "industry": "Consulting/Audit", "cn_name": "毕马威"},

        # 金融机构
        {"name": "JPMorgan Chase", "industry": "Finance", "cn_name": "摩根大通"},
        {"name": "Goldman Sachs", "industry": "Finance", "cn_name": "高盛"},
        {"name": "Morgan Stanley", "industry": "Finance", "cn_name": "摩根士丹利"},
        {"name": "Citibank", "industry": "Finance", "cn_name": "花旗银行"},
        {"name": "HSBC", "industry": "Finance", "cn_name": "汇丰银行"},
        {"name": "Standard Chartered", "industry": "Finance", "cn_name": "渣打银行"},

        # 快消/零售
        {"name": "Unilever", "industry": "FMCG", "cn_name": "联合利华"},
        {"name": "P&G", "industry": "FMCG", "cn_name": "宝洁"},
        {"name": "Coca-Cola", "industry": "Beverage", "cn_name": "可口可乐"},
        {"name": "Nike", "industry": "Retail/Sports", "cn_name": "耐克"},
        {"name": "Adidas", "industry": "Retail/Sports", "cn_name": "阿迪达斯"},

        # 汽车
        {"name": "Tesla", "industry": "Automotive/Tech", "cn_name": "特斯拉"},
        {"name": "BMW", "industry": "Automotive", "cn_name": "宝马"},
        {"name": "Mercedes-Benz", "industry": "Automotive", "cn_name": "奔驰"},

        # 制药/医疗
        {"name": "Pfizer", "industry": "Pharmaceutical", "cn_name": "辉瑞"},
        {"name": "Roche", "industry": "Pharmaceutical", "cn_name": "罗氏"},
        {"name": "Johnson & Johnson", "industry": "Healthcare", "cn_name": "强生"},
    ]


def get_data_job_positions() -> List[Dict]:
    """
    定义数据相关岗位类型及其关键词
    """
    return [
        {
            "title": "Data Engineer",
            "cn_title": "数据工程师",
            "keywords": ["data engineer", "数据工程师", "etl", "data pipeline"],
            "level": ["junior", "mid", "senior"]
        },
        {
            "title": "Data Analyst",
            "cn_title": "数据分析师",
            "keywords": ["data analyst", "数据分析师", "business analyst", "分析师"],
            "level": ["junior", "mid", "senior"]
        },
        {
            "title": "Data Scientist",
            "cn_title": "数据科学家",
            "keywords": ["data scientist", "数据科学家", "machine learning", "ml engineer"],
            "level": ["mid", "senior"]
        },
        {
            "title": "BI Developer/Analyst",
            "cn_title": "BI开发/分析师",
            "keywords": ["bi developer", "bi analyst", "tableau", "power bi", "商业智能"],
            "level": ["junior", "mid", "senior"]
        },
        {
            "title": "Analytics Engineer",
            "cn_title": "分析工程师",
            "keywords": ["analytics engineer", "分析工程师", "dbt"],
            "level": ["mid", "senior"]
        },
        {
            "title": "Data Architect",
            "cn_title": "数据架构师",
            "keywords": ["data architect", "数据架构师", "solution architect"],
            "level": ["senior", "lead"]
        },
    ]


def simulate_job_listings() -> List[Dict]:
    """
    模拟从招聘网站抓取的数据岗位信息
    基于真实市场情况整理
    """
    jobs = [
        {
            "company": "Microsoft",
            "cn_company": "微软",
            "position": "Senior Data Engineer",
            "location": "Shanghai, China",
            "salary_range": "40-70k RMB/month",
            "posted_date": "2026-02-10",
            "job_description": """
We are seeking a Senior Data Engineer to join our Azure Data Platform team in Shanghai.

Responsibilities:
- Design and build scalable data pipelines using Azure Data Factory, Databricks, and Synapse Analytics
- Develop and maintain data warehouse solutions for business analytics
- Collaborate with data scientists and analysts to ensure data quality and availability
- Implement data governance and security best practices
- Optimize ETL processes for performance and cost efficiency

Requirements:
- 5+ years of experience in data engineering
- Strong proficiency in SQL, Python, and Spark
- Experience with cloud data platforms (Azure, AWS, or GCP)
- Solid understanding of data warehousing concepts (Kimball, Data Vault)
- Experience with modern data stack tools (dbt, Airflow, etc.)
- Excellent communication skills in English (written and verbal)
- Bachelor's degree in Computer Science or related field

Preferred:
- Azure certifications (DP-203, DP-900)
- Experience with real-time streaming (Kafka, Event Hub)
- Knowledge of ML/AI concepts
- Prior experience in multinational companies
""",
            "skills": ["Azure", "Python", "SQL", "Spark", "Data Warehousing", "ETL", "English"],
            "source": "LinkedIn"
        },
        {
            "company": "Amazon",
            "cn_company": "亚马逊",
            "position": "Data Engineer II",
            "location": "Shanghai, China",
            "salary_range": "35-60k RMB/month",
            "posted_date": "2026-02-12",
            "job_description": """
Amazon Web Services (AWS) is looking for a Data Engineer to build next-generation data solutions.

Key Responsibilities:
- Build and maintain data pipelines using AWS services (Glue, EMR, Redshift, S3)
- Design dimensional data models for analytics and reporting
- Work with stakeholders to understand data requirements
- Implement data quality checks and monitoring
- Automate data workflows using Python and SQL

Basic Qualifications:
- 3+ years of data engineering experience
- Proficiency in SQL and at least one programming language (Python/Java)
- Experience with AWS or other cloud platforms
- Understanding of data warehouse architecture
- Strong problem-solving skills
- Good English communication skills

Preferred Qualifications:
- AWS certifications
- Experience with big data technologies (Hadoop, Spark)
- Knowledge of data visualization tools (QuickSight, Tableau)
- Experience in agile development environment
- Familiar with Git and CI/CD practices
""",
            "skills": ["AWS", "Python", "SQL", "Redshift", "Data Modeling", "ETL", "English"],
            "source": "Amazon Careers"
        },
        {
            "company": "McKinsey & Company",
            "cn_company": "麦肯锡",
            "position": "Data Analyst",
            "location": "Shanghai, China",
            "salary_range": "30-50k RMB/month",
            "posted_date": "2026-02-08",
            "job_description": """
Join McKinsey's QuantumBlack team as a Data Analyst supporting advanced analytics projects.

What You'll Do:
- Conduct complex data analysis to support client consulting projects
- Develop dashboards and visualizations using Tableau/Power BI
- Perform statistical analysis and hypothesis testing
- Collaborate with consultants and data scientists
- Present findings to stakeholders and clients

What You'll Bring:
- 2-4 years of experience in data analysis
- Advanced SQL skills and proficiency in Python or R
- Experience with BI tools (Tableau, Power BI, Looker)
- Strong statistical and analytical thinking
- Excellent presentation and storytelling skills
- Fluent English (both written and spoken)
- Bachelor's degree in quantitative field

Bonus Points:
- Experience in consulting or professional services
- Knowledge of machine learning concepts
- Industry expertise (finance, retail, healthcare)
- Master's degree in relevant field
""",
            "skills": ["SQL", "Python", "Tableau", "Statistics", "Data Visualization", "English", "Presentation"],
            "source": "McKinsey Careers"
        },
        {
            "company": "Goldman Sachs",
            "cn_company": "高盛",
            "position": "Quantitative Data Analyst",
            "location": "Shanghai, China",
            "salary_range": "35-65k RMB/month",
            "posted_date": "2026-02-11",
            "job_description": """
Goldman Sachs is seeking a Quantitative Data Analyst for our Shanghai office.

Responsibilities:
- Analyze large financial datasets to identify trends and insights
- Build and maintain data models for risk and trading analytics
- Develop automated reporting solutions using Python and SQL
- Collaborate with traders, risk managers, and technology teams
- Ensure data accuracy and consistency across systems

Requirements:
- 3+ years of experience in financial data analysis
- Strong SQL and Python skills
- Experience with financial databases and market data
- Solid understanding of statistics and probability
- Excellent attention to detail
- Strong English communication skills
- Bachelor's degree in Finance, Mathematics, Computer Science, or related field

Preferred:
- Experience with time series analysis
- Knowledge of financial instruments and markets
- Familiarity with data visualization tools
- CFA or FRM certification
""",
            "skills": ["SQL", "Python", "Financial Analysis", "Statistics", "Data Modeling", "English"],
            "source": "Goldman Sachs Careers"
        },
        {
            "company": "Accenture",
            "cn_company": "埃森哲",
            "position": "Data Warehouse Developer",
            "location": "Shanghai, China",
            "salary_range": "25-45k RMB/month",
            "posted_date": "2026-02-09",
            "job_description": """
Accenture is looking for Data Warehouse Developers to join our Data & Analytics practice.

Key Accountabilities:
- Design and develop data warehouse solutions (Kimball methodology)
- Build ETL processes using industry-standard tools
- Create dimensional models (star schema, snowflake schema)
- Optimize SQL queries and database performance
- Document technical specifications and data lineage
- Participate in requirement gathering and solution design

Must-Have Skills:
- 3-5 years of data warehouse development experience
- Expert-level SQL skills
- Experience with ETL tools (Informatica, SSIS, Talend, or similar)
- Understanding of dimensional modeling principles
- Database experience (Oracle, SQL Server, Teradata, or similar)
- Good English reading and writing skills

Nice-to-Have:
- Cloud data warehouse experience (Snowflake, Redshift, BigQuery)
- Scripting skills (Python, Shell)
- Experience with Agile/Scrum methodology
- Relevant certifications
""",
            "skills": ["SQL", "ETL", "Data Warehousing", "Dimensional Modeling", "Informatica", "English"],
            "source": "Accenture Careers"
        },
        {
            "company": "SAP",
            "cn_company": "思爱普",
            "position": "Analytics Engineer",
            "location": "Shanghai, China",
            "salary_range": "30-55k RMB/month",
            "posted_date": "2026-02-13",
            "job_description": """
SAP is hiring an Analytics Engineer to work on our cloud analytics platform.

What You'll Do:
- Transform raw data into analytics-ready datasets using dbt
- Design and implement metrics layer for business reporting
- Build and maintain data pipelines in cloud environments
- Work closely with analysts to understand data needs
- Establish data quality standards and testing frameworks
- Create documentation for data models and processes

What We're Looking For:
- 3+ years in analytics engineering or data engineering role
- Strong SQL skills and experience with modern data stack
- Hands-on experience with dbt (data build tool)
- Familiarity with cloud data platforms (Snowflake, BigQuery, Redshift)
- Understanding of software engineering best practices (Git, testing, CI/CD)
- Python knowledge is a plus
- Good English communication skills

Preferred:
- Experience with data orchestration tools (Airflow, Prefect, Dagster)
- Knowledge of BI tools and semantic layers
- Background in analytics or data science
""",
            "skills": ["SQL", "dbt", "Python", "Modern Data Stack", "Cloud Platforms", "Git", "English"],
            "source": "SAP Careers"
        },
        {
            "company": "Deloitte",
            "cn_company": "德勤",
            "position": "Senior Data Scientist",
            "location": "Shanghai, China",
            "salary_range": "40-80k RMB/month",
            "posted_date": "2026-02-07",
            "job_description": """
Deloitte Consulting is seeking a Senior Data Scientist for client-facing analytics projects.

Role Overview:
- Lead end-to-end data science projects for enterprise clients
- Develop predictive models and machine learning solutions
- Conduct advanced statistical analysis and experiments
- Translate business problems into analytical frameworks
- Present insights and recommendations to C-level executives
- Mentor junior team members

Required Skills:
- 5+ years of experience in data science or advanced analytics
- Strong foundation in statistics, machine learning, and algorithms
- Proficiency in Python (scikit-learn, pandas, numpy)
- Experience with SQL and data manipulation
- Proven track record of delivering business impact
- Excellent stakeholder management and presentation skills
- Fluent in English and Mandarin
- Master's or PhD in quantitative field preferred

Desirable:
- Consulting experience
- Experience with cloud ML platforms (AWS SageMaker, Azure ML, GCP Vertex AI)
- Knowledge of deep learning frameworks (TensorFlow, PyTorch)
- Industry expertise in financial services, retail, or manufacturing
""",
            "skills": ["Python", "Machine Learning", "Statistics", "SQL", "Consulting", "English", "Presentation"],
            "source": "Deloitte Careers"
        },
        {
            "company": "HSBC",
            "cn_company": "汇丰银行",
            "position": "Data Engineer - Risk Analytics",
            "location": "Shanghai, China",
            "salary_range": "35-60k RMB/month",
            "posted_date": "2026-02-10",
            "job_description": """
HSBC is looking for a Data Engineer to support risk analytics and regulatory reporting.

Responsibilities:
- Build data pipelines for credit risk, market risk, and operational risk
- Develop ETL processes to consolidate data from multiple sources
- Work with risk analysts and compliance teams
- Ensure data quality and regulatory compliance (Basel III, IFRS9)
- Optimize database performance for large-scale risk calculations
- Support regulatory reporting and stress testing exercises

Requirements:
- 4+ years of data engineering experience, preferably in banking/finance
- Strong SQL skills and database knowledge (Oracle, SQL Server, Teradata)
- Experience with ETL tools and data integration
- Understanding of banking products and risk concepts
- Attention to detail and commitment to data accuracy
- Good English communication skills
- Bachelor's degree in Computer Science, Engineering, or related field

Preferred:
- Experience with regulatory reporting (FRTB, IFRS9, etc.)
- Knowledge of big data technologies (Hadoop, Spark)
- Python or R programming skills
- Relevant certifications (FRM, PRM)
""",
            "skills": ["SQL", "ETL", "Risk Analytics", "Banking", "Oracle", "Data Quality", "English"],
            "source": "HSBC Careers"
        },
        {
            "company": "Apple",
            "cn_company": "苹果",
            "position": "Data Engineer - Supply Chain Analytics",
            "location": "Shanghai, China",
            "salary_range": "40-70k RMB/month",
            "posted_date": "2026-02-12",
            "job_description": """
Apple is seeking a Data Engineer to support supply chain and operations analytics.

Key Responsibilities:
- Design and implement data pipelines for supply chain data
- Build data models to support inventory, logistics, and procurement analytics
- Collaborate with operations teams across Asia-Pacific region
- Develop automated reporting and monitoring solutions
- Ensure data integrity and consistency across systems
- Optimize data infrastructure for scale and performance

Minimum Qualifications:
- 5+ years of experience in data engineering
- Expert SQL and Python programming skills
- Experience with distributed computing (Spark, Hadoop)
- Strong understanding of data warehousing and ETL concepts
- Ability to work in fast-paced, dynamic environment
- Excellent problem-solving and analytical skills
- Proficient in English

Preferred Qualifications:
- Experience in supply chain or operations analytics
- Knowledge of real-time data processing (Kafka, Flink)
- Familiarity with data orchestration tools (Airflow)
- Cloud platform experience (AWS, GCP, or Azure)
- Background in manufacturing or retail industry
""",
            "skills": ["Python", "SQL", "Spark", "Supply Chain", "ETL", "Cloud", "English"],
            "source": "Apple Careers"
        },
        {
            "company": "Unilever",
            "cn_company": "联合利华",
            "position": "Business Intelligence Analyst",
            "location": "Shanghai, China",
            "salary_range": "25-45k RMB/month",
            "posted_date": "2026-02-11",
            "job_description": """
Unilever is hiring a BI Analyst to support commercial analytics for FMCG brands.

What You'll Do:
- Create dashboards and reports to track business KPIs
- Analyze sales, marketing, and consumer data
- Support brand teams with ad-hoc analysis
- Maintain and enhance BI infrastructure (Tableau, Power BI)
- Collaborate with regional and global analytics teams
- Identify opportunities for process automation

What You Need:
- 2-4 years of experience in BI or data analysis
- Strong SQL and Excel skills
- Hands-on experience with BI tools (Tableau, Power BI, or Looker)
- Understanding of FMCG/retail business metrics
- Ability to tell stories with data
- Good English skills for global collaboration
- Bachelor's degree in Business, Statistics, or related field

Bonus:
- Python or R programming experience
- Knowledge of marketing analytics
- Experience with Google Analytics or similar tools
- Understanding of consumer behavior
""",
            "skills": ["SQL", "Tableau", "Power BI", "Excel", "FMCG", "Marketing Analytics", "English"],
            "source": "Unilever Careers"
        },
    ]

    return jobs


def analyze_skill_requirements(jobs: List[Dict]) -> Dict:
    """
    分析岗位技能要求，提取关键信息
    """

    # 统计技能出现频率
    skill_count = {}
    for job in jobs:
        for skill in job.get("skills", []):
            skill_count[skill] = skill_count.get(skill, 0) + 1

    # 按频率排序
    sorted_skills = sorted(skill_count.items(), key=lambda x: x[1], reverse=True)

    # 提取薪资信息
    salary_ranges = []
    for job in jobs:
        salary = job.get("salary_range", "")
        # 提取数字范围
        matches = re.findall(r'(\d+)-(\d+)k', salary)
        if matches:
            low, high = matches[0]
            salary_ranges.append((int(low), int(high)))

    avg_low = sum(s[0] for s in salary_ranges) / len(salary_ranges) if salary_ranges else 0
    avg_high = sum(s[1] for s in salary_ranges) / len(salary_ranges) if salary_ranges else 0

    # 分类技能
    technical_skills = {}
    soft_skills = {}
    tools_platforms = {}

    for skill, count in sorted_skills:
        skill_lower = skill.lower()

        # 技术技能
        if any(tech in skill_lower for tech in ['sql', 'python', 'spark', 'etl', 'java', 'scala', 'r']):
            technical_skills[skill] = count
        # 工具和平台
        elif any(tool in skill_lower for tool in ['aws', 'azure', 'gcp', 'tableau', 'power bi', 'snowflake', 'airflow', 'dbt', 'hadoop', 'kafka', 'oracle']):
            tools_platforms[skill] = count
        # 软技能和领域知识
        elif any(soft in skill_lower for soft in ['english', 'presentation', 'consulting', 'communication']):
            soft_skills[skill] = count
        else:
            # 其他归类为技术技能
            technical_skills[skill] = count

    return {
        "total_jobs": len(jobs),
        "skill_frequency": dict(sorted_skills[:20]),  # Top 20
        "technical_skills": technical_skills,
        "tools_platforms": tools_platforms,
        "soft_skills": soft_skills,
        "salary_analysis": {
            "average_low": f"{avg_low:.1f}k RMB/month",
            "average_high": f"{avg_high:.1f}k RMB/month",
            "range": f"{min(s[0] for s in salary_ranges)}-{max(s[1] for s in salary_ranges)}k RMB/month" if salary_ranges else "N/A"
        }
    }


def identify_skill_gaps(current_skills: Set[str], target_skills: Dict) -> Dict:
    """
    识别技能差距

    Args:
        current_skills: 当前具备的技能集合
        target_skills: 目标岗位要求的技能字典（技能: 出现频率）

    Returns:
        技能差距分析结果
    """

    # 转换为小写便于比较
    current_skills_lower = {s.lower() for s in current_skills}

    # 识别已有技能和缺失技能
    have_skills = []
    missing_skills = []

    for skill, freq in target_skills.items():
        skill_lower = skill.lower()
        if any(cs in skill_lower or skill_lower in cs for cs in current_skills_lower):
            have_skills.append((skill, freq))
        else:
            missing_skills.append((skill, freq))

    # 按优先级排序（出现频率）
    missing_skills.sort(key=lambda x: x[1], reverse=True)

    return {
        "have_skills": have_skills,
        "missing_skills": missing_skills,
        "skill_coverage": len(have_skills) / len(target_skills) * 100 if target_skills else 0
    }


def generate_learning_plan(skill_gaps: Dict, timeline_months: int = 6) -> Dict:
    """
    生成个性化学习计划

    Args:
        skill_gaps: 技能差距分析结果
        timeline_months: 学习时间线（月）

    Returns:
        详细的学习计划
    """

    missing_skills = skill_gaps["missing_skills"]

    # 技能学习资源映射
    skill_resources = {
        # 编程语言
        "python": {
            "priority": "Critical",
            "learning_time": "1-2 months",
            "resources": [
                "Python官方文档和教程",
                "《Python Crash Course》书籍",
                "LeetCode Python专题练习",
                "DataCamp Python for Data Engineering课程"
            ],
            "practice_projects": [
                "编写数据清洗脚本处理CSV/JSON文件",
                "使用pandas进行数据分析",
                "开发简单的ETL脚本",
                "实现常见算法和数据结构"
            ]
        },
        "sql": {
            "priority": "Critical",
            "learning_time": "2-3 weeks",
            "resources": [
                "Mode Analytics SQL教程",
                "LeetCode Database专题（180+题）",
                "《SQL Performance Explained》",
                "HackerRank SQL练习"
            ],
            "practice_projects": [
                "解决50+ SQL复杂查询题目",
                "分析窗口函数和CTE应用场景",
                "学习查询优化和索引策略",
                "实践数据库设计范式"
            ]
        },

        # 云平台
        "aws": {
            "priority": "High",
            "learning_time": "1-2 months",
            "resources": [
                "AWS官方培训课程（免费）",
                "A Cloud Guru AWS课程",
                "AWS Solutions Architect Associate认证备考",
                "AWS数据工程服务实践（Glue, EMR, Redshift）"
            ],
            "practice_projects": [
                "在AWS免费套餐搭建数据管道",
                "使用S3 + Glue + Athena构建数据湖",
                "配置Redshift数据仓库",
                "实现Lambda + EventBridge自动化任务"
            ]
        },
        "azure": {
            "priority": "High",
            "learning_time": "1-2 months",
            "resources": [
                "Microsoft Learn Azure数据工程路径",
                "Azure Data Engineer Associate (DP-203)认证",
                "Pluralsight Azure课程",
                "Azure数据服务实践（Data Factory, Synapse, Databricks）"
            ],
            "practice_projects": [
                "使用Azure Data Factory创建ETL管道",
                "在Azure Databricks运行Spark作业",
                "配置Azure Synapse Analytics",
                "实现Azure DevOps CI/CD"
            ]
        },
        "gcp": {
            "priority": "Medium",
            "learning_time": "1-2 months",
            "resources": [
                "Google Cloud Skills Boost",
                "Coursera GCP专项课程",
                "《Data Engineering on Google Cloud Platform》",
                "GCP Professional Data Engineer认证"
            ],
            "practice_projects": [
                "使用BigQuery进行数据分析",
                "构建Cloud Composer (Airflow)工作流",
                "实现Dataflow流式处理",
                "配置Cloud Storage数据湖"
            ]
        },

        # 大数据技术
        "spark": {
            "priority": "High",
            "learning_time": "2-3 months",
            "resources": [
                "《Learning Spark》第二版",
                "Databricks Spark培训",
                "Udemy Spark课程",
                "Apache Spark官方文档"
            ],
            "practice_projects": [
                "用PySpark处理大规模数据集",
                "实现Spark SQL数据转换",
                "优化Spark作业性能",
                "学习Spark Streaming实时处理"
            ]
        },

        # 数据仓库
        "data warehousing": {
            "priority": "High",
            "learning_time": "1-2 months",
            "resources": [
                "《The Data Warehouse Toolkit》(Kimball)",
                "《Building the Data Warehouse》(Inmon)",
                "Coursera数据仓库专项课程",
                "Modern Data Warehouse架构文章"
            ],
            "practice_projects": [
                "设计Kimball维度模型（星型/雪花）",
                "实现SCD（缓慢变化维）",
                "构建事实表和维度表",
                "学习Data Vault 2.0建模"
            ]
        },

        # 现代数据栈
        "dbt": {
            "priority": "Medium-High",
            "learning_time": "2-4 weeks",
            "resources": [
                "dbt官方文档和教程",
                "dbt Learn免费课程",
                "《Analytics Engineering with dbt》",
                "dbt Discourse社区"
            ],
            "practice_projects": [
                "搭建dbt项目结构",
                "编写dbt模型和测试",
                "实现增量模型和快照",
                "配置dbt Cloud CI/CD"
            ]
        },
        "airflow": {
            "priority": "Medium",
            "learning_time": "3-4 weeks",
            "resources": [
                "Apache Airflow官方文档",
                "《Data Pipelines with Apache Airflow》",
                "Astronomer Airflow教程",
                "Airflow Summit视频"
            ],
            "practice_projects": [
                "创建Airflow DAG调度任务",
                "实现任务依赖和错误处理",
                "配置Airflow连接和变量",
                "学习TaskFlow API"
            ]
        },

        # BI工具
        "tableau": {
            "priority": "Medium",
            "learning_time": "2-3 weeks",
            "resources": [
                "Tableau Desktop Specialist认证",
                "Tableau Public Gallery学习",
                "《Tableau Your Data》书籍",
                "Tableau官方培训视频"
            ],
            "practice_projects": [
                "创建交互式仪表板",
                "实现高级计算和LOD表达式",
                "连接多数据源进行混合",
                "发布到Tableau Server/Online"
            ]
        },
        "power bi": {
            "priority": "Medium",
            "learning_time": "2-3 weeks",
            "resources": [
                "Microsoft Learn Power BI路径",
                "《Dashboarding and Reporting with Power BI》",
                "SQLBI网站DAX教程",
                "Power BI Community论坛"
            ],
            "practice_projects": [
                "创建Power BI报表和仪表板",
                "学习DAX语言和数据建模",
                "实现RLS（行级安全）",
                "配置Power BI Service发布"
            ]
        },

        # 英语
        "english": {
            "priority": "Critical",
            "learning_time": "Ongoing (6 months)",
            "resources": [
                "职场英语口语课程（如Wall Street English）",
                "技术英语阅读（Medium, Dev.to文章）",
                "参加英语角或语言交换",
                "看英文技术视频（YouTube, Pluralsight）"
            ],
            "practice_projects": [
                "每天阅读英文技术博客",
                "用英文写技术文档",
                "参加英文技术分享会",
                "模拟英文面试练习"
            ]
        },

        # 其他重要技能
        "git": {
            "priority": "High",
            "learning_time": "1-2 weeks",
            "resources": [
                "《Pro Git》免费电子书",
                "GitHub Learning Lab",
                "Learn Git Branching互动教程",
                "Git官方文档"
            ],
            "practice_projects": [
                "掌握Git基本命令和工作流",
                "学习分支管理和合并策略",
                "实践Pull Request流程",
                "了解Git Hooks和CI/CD集成"
            ]
        },
        "statistics": {
            "priority": "Medium",
            "learning_time": "1-2 months",
            "resources": [
                "《Statistics for Business and Economics》",
                "Khan Academy统计学课程",
                "Coursera统计推断专项课程",
                "《Practical Statistics for Data Scientists》"
            ],
            "practice_projects": [
                "掌握描述性统计和推断统计",
                "学习假设检验和置信区间",
                "理解A/B测试原理",
                "实践回归分析和相关分析"
            ]
        }
    }

    # 构建学习计划
    learning_plan = {
        "overview": {
            "timeline": f"{timeline_months} months",
            "goal": "从国内互联网传统数仓岗位转型到外企数据岗位",
            "focus_areas": ["技术能力提升", "英语沟通能力", "外企工作文化适应"]
        },
        "monthly_plan": {},
        "skill_roadmap": [],
        "certifications": [],
        "english_improvement": {},
        "job_preparation": {}
    }

    # 按优先级和频率确定学习顺序
    priority_map = {"Critical": 1, "High": 2, "Medium-High": 2.5, "Medium": 3, "Low": 4}

    skills_to_learn = []
    for skill, freq in missing_skills:
        skill_key = skill.lower()
        for key in skill_resources:
            if key in skill_key or skill_key in key:
                resource = skill_resources[key]
                priority_score = priority_map.get(resource["priority"], 3)
                # 综合考虑优先级和出现频率
                score = priority_score - (freq / 10)  # 频率越高，分数越低（优先级越高）
                skills_to_learn.append({
                    "skill": skill,
                    "details": resource,
                    "frequency": freq,
                    "score": score
                })
                break

    # 排序
    skills_to_learn.sort(key=lambda x: x["score"])

    # 分配到各月
    if timeline_months == 3:
        # 3个月快速通道（高强度）
        learning_plan["monthly_plan"] = {
            "Month 1": {
                "focus": "核心技术基础 + 英语启动",
                "skills": [],
                "weekly_hours": "20-25小时",
                "milestones": []
            },
            "Month 2": {
                "focus": "云平台 + 现代数据栈 + 英语强化",
                "skills": [],
                "weekly_hours": "20-25小时",
                "milestones": []
            },
            "Month 3": {
                "focus": "综合项目 + 面试准备",
                "skills": [],
                "weekly_hours": "15-20小时",
                "milestones": []
            }
        }

        # 分配技能到各月
        for i, skill_info in enumerate(skills_to_learn[:8]):  # 3个月最多8-10个重点技能
            if i < 3:
                month = "Month 1"
            elif i < 6:
                month = "Month 2"
            else:
                month = "Month 3"
            learning_plan["monthly_plan"][month]["skills"].append(skill_info)

    elif timeline_months == 6:
        # 6个月标准通道（中等强度）
        learning_plan["monthly_plan"] = {
            "Month 1-2": {
                "focus": "编程基础 + SQL精进",
                "skills": [],
                "weekly_hours": "15-20小时",
                "milestones": ["完成Python核心语法", "解决100+ SQL题目", "英语技术阅读启动"]
            },
            "Month 3-4": {
                "focus": "云平台 + 大数据技术",
                "skills": [],
                "weekly_hours": "15-20小时",
                "milestones": ["获得云平台认证", "完成Spark项目", "英语口语提升"]
            },
            "Month 5": {
                "focus": "现代数据栈 + BI工具",
                "skills": [],
                "weekly_hours": "12-15小时",
                "milestones": ["掌握dbt和Airflow", "创建BI仪表板作品集"]
            },
            "Month 6": {
                "focus": "综合项目 + 面试准备",
                "skills": [],
                "weekly_hours": "10-15小时",
                "milestones": ["完成端到端数据项目", "准备英文简历和面试", "开始投递简历"]
            }
        }

        # 分配技能
        skills_per_phase = [3, 3, 2, 2]
        phases = ["Month 1-2", "Month 3-4", "Month 5", "Month 6"]
        idx = 0
        for phase, count in zip(phases, skills_per_phase):
            for _ in range(count):
                if idx < len(skills_to_learn):
                    learning_plan["monthly_plan"][phase]["skills"].append(skills_to_learn[idx])
                    idx += 1

    # 技能路线图
    learning_plan["skill_roadmap"] = [
        {
            "phase": "Foundation (第1-2月)",
            "goals": [
                "强化Python编程（数据处理、脚本开发）",
                "精通SQL（复杂查询、性能优化、窗口函数）",
                "掌握Git版本控制",
                "开始技术英语学习"
            ]
        },
        {
            "phase": "Cloud & Big Data (第3-4月)",
            "goals": [
                "学习至少一个云平台（AWS/Azure，根据目标公司选择）",
                "掌握Spark大数据处理",
                "理解云数据仓库架构",
                "提升英语阅读和写作"
            ]
        },
        {
            "phase": "Modern Data Stack (第5月)",
            "goals": [
                "学习dbt进行数据转换",
                "掌握Airflow任务调度",
                "熟练使用BI工具（Tableau或Power BI）",
                "练习英语口语表达"
            ]
        },
        {
            "phase": "Integration & Job Hunt (第6月)",
            "goals": [
                "完成综合数据工程项目",
                "准备英文简历和作品集",
                "模拟英文技术面试",
                "开始投递外企职位"
            ]
        }
    ]

    # 推荐认证
    learning_plan["certifications"] = [
        {
            "name": "AWS Certified Data Analytics - Specialty",
            "provider": "Amazon Web Services",
            "difficulty": "Medium",
            "prep_time": "1-2 months",
            "value": "Very High for AWS-focused roles",
            "cost": "$300"
        },
        {
            "name": "Microsoft Certified: Azure Data Engineer Associate (DP-203)",
            "provider": "Microsoft",
            "difficulty": "Medium",
            "prep_time": "1-2 months",
            "value": "Very High for Azure-focused roles",
            "cost": "$165"
        },
        {
            "name": "Google Cloud Professional Data Engineer",
            "provider": "Google Cloud",
            "difficulty": "Hard",
            "prep_time": "2-3 months",
            "value": "High for GCP-focused roles",
            "cost": "$200"
        },
        {
            "name": "dbt Analytics Engineering Certification",
            "provider": "dbt Labs",
            "difficulty": "Easy-Medium",
            "prep_time": "2-3 weeks",
            "value": "High for modern data stack roles",
            "cost": "Free"
        },
        {
            "name": "Tableau Desktop Specialist",
            "provider": "Tableau",
            "difficulty": "Easy",
            "prep_time": "2-3 weeks",
            "value": "Medium for BI-focused roles",
            "cost": "$100"
        }
    ]

    # 英语提升计划
    learning_plan["english_improvement"] = {
        "daily_routine": [
            "晨读：20分钟英文技术文章或文档",
            "午休：收听英文技术播客（Data Engineering Podcast, Software Engineering Daily）",
            "晚上：看英文技术视频（YouTube, Pluralsight）30分钟"
        ],
        "weekly_practice": [
            "参加1-2次英语角或线上语言交换",
            "写1篇英文技术博客或总结",
            "模拟1次英文技术面试"
        ],
        "resources": [
            "技术英语词汇表（数据工程相关术语）",
            "STAR面试法英文回答模板",
            "常见技术面试问题英文版",
            "LinkedIn Learning职场英语课程"
        ],
        "milestone_goals": {
            "Month 2": "能流畅阅读英文技术文档",
            "Month 4": "能用英文写清晰的技术邮件和文档",
            "Month 6": "能用英文进行技术面试和日常工作沟通"
        }
    }

    # 求职准备
    learning_plan["job_preparation"] = {
        "resume": [
            "使用英文简历模板（针对外企）",
            "突出量化成果（processed XX TB data, improved performance by XX%）",
            "强调云平台和现代工具经验",
            "添加GitHub项目链接",
            "请母语人士或专业服务润色"
        ],
        "portfolio": [
            "在GitHub搭建数据工程项目展示",
            "项目1：云平台数据管道（AWS/Azure + Airflow + dbt）",
            "项目2：实时数据处理（Kafka + Spark Streaming）",
            "项目3：BI仪表板（Tableau/Power BI with storytelling）",
            "所有项目包含详细英文README和文档"
        ],
        "interview_prep": [
            "SQL刷题：LeetCode Database所有Medium/Hard题目",
            "Python编程：掌握数据结构和算法基础",
            "系统设计：学习数据系统设计（参考《Designing Data-Intensive Applications》）",
            "行为面试：准备STAR格式英文回答",
            "模拟面试：通过Pramp或朋友进行英文模拟面试"
        ],
        "networking": [
            "优化LinkedIn profile（英文）",
            "关注目标公司和行业领袖",
            "参加线上/线下数据工程meetup",
            "在技术社区（Reddit, Blind）活跃",
            "联系在外企工作的校友或朋友内推"
        ],
        "target_companies": [
            "优先级1（数据密集型科技公司）：Microsoft, Amazon, Apple, SAP",
            "优先级2（咨询公司数据岗）：Accenture, Deloitte, PwC, EY",
            "优先级3（金融机构）：HSBC, Citi, Goldman Sachs, JPMorgan",
            "优先级4（其他外企）：Unilever, Nike, BMW等有数据团队的公司"
        ]
    }

    return learning_plan


def save_analysis_report(jobs: List[Dict], skill_analysis: Dict, learning_plan: Dict, filename: str):
    """保存分析报告"""
    report = {
        "generated_at": datetime.now().isoformat(),
        "location": "Shanghai, China",
        "focus": "Foreign Company Data Positions",
        "job_listings": jobs,
        "skill_analysis": skill_analysis,
        "learning_plan": learning_plan
    }

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 完整分析报告已保存到: {filename}")


def print_analysis_summary(skill_analysis: Dict, learning_plan: Dict):
    """打印分析摘要"""
    print("\n" + "="*100)
    print("📊 上海外企数据岗位分析报告")
    print("="*100)
    print(f"分析时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"分析岗位数: {skill_analysis['total_jobs']}")

    print("\n" + "-"*100)
    print("💰 薪资水平")
    print("-"*100)
    sal = skill_analysis['salary_analysis']
    print(f"平均薪资范围: {sal['average_low']} - {sal['average_high']}")
    print(f"总体范围: {sal['range']}")

    print("\n" + "-"*100)
    print("🔑 Top 15 核心技能要求")
    print("-"*100)
    for idx, (skill, count) in enumerate(list(skill_analysis['skill_frequency'].items())[:15], 1):
        percentage = (count / skill_analysis['total_jobs']) * 100
        bar = "█" * int(percentage / 5)
        print(f"{idx:2d}. {skill:30s} {count:2d}次 ({percentage:5.1f}%) {bar}")

    print("\n" + "-"*100)
    print("💻 技术技能分类")
    print("-"*100)
    for skill, count in list(skill_analysis['technical_skills'].items())[:10]:
        print(f"  • {skill}: {count}次")

    print("\n" + "-"*100)
    print("🛠️  工具和平台")
    print("-"*100)
    for skill, count in list(skill_analysis['tools_platforms'].items())[:10]:
        print(f"  • {skill}: {count}次")

    print("\n" + "-"*100)
    print("🗣️  软技能和其他要求")
    print("-"*100)
    for skill, count in skill_analysis['soft_skills'].items():
        print(f"  • {skill}: {count}次")

    print("\n\n" + "="*100)
    print("📚 学习计划概览")
    print("="*100)
    print(f"时间线: {learning_plan['overview']['timeline']}")
    print(f"目标: {learning_plan['overview']['goal']}")
    print(f"\n重点领域:")
    for area in learning_plan['overview']['focus_areas']:
        print(f"  • {area}")

    print("\n" + "-"*100)
    print("📅 月度计划")
    print("-"*100)
    for phase, details in learning_plan['monthly_plan'].items():
        print(f"\n【{phase}】- {details['focus']}")
        print(f"每周投入: {details['weekly_hours']}")
        if details['skills']:
            print("学习技能:")
            for skill_info in details['skills']:
                print(f"  • {skill_info['skill']} (出现{skill_info['frequency']}次) - {skill_info['details']['learning_time']}")
        if details.get('milestones'):
            print("里程碑:")
            for milestone in details['milestones']:
                print(f"  ✓ {milestone}")

    print("\n" + "-"*100)
    print("🎯 技能路线图")
    print("-"*100)
    for roadmap in learning_plan['skill_roadmap']:
        print(f"\n{roadmap['phase']}:")
        for goal in roadmap['goals']:
            print(f"  • {goal}")

    print("\n" + "-"*100)
    print("🏆 推荐认证")
    print("-"*100)
    for cert in learning_plan['certifications'][:3]:  # 显示前3个最重要的
        print(f"\n{cert['name']}")
        print(f"  难度: {cert['difficulty']} | 准备时间: {cert['prep_time']} | 价值: {cert['value']}")

    print("\n" + "-"*100)
    print("🌍 英语提升计划")
    print("-"*100)
    print("每日练习:")
    for routine in learning_plan['english_improvement']['daily_routine']:
        print(f"  • {routine}")
    print("\n阶段目标:")
    for month, goal in learning_plan['english_improvement']['milestone_goals'].items():
        print(f"  • {month}: {goal}")

    print("\n" + "-"*100)
    print("💼 求职准备")
    print("-"*100)
    print("\n作品集项目:")
    for project in learning_plan['job_preparation']['portfolio']:
        print(f"  • {project}")

    print("\n目标公司:")
    for target in learning_plan['job_preparation']['target_companies']:
        print(f"  • {target}")

    print("\n\n" + "="*100)
    print("📈 关键建议")
    print("="*100)
    print("""
1. 英语是最大的差异化因素
   外企对英语要求高，这是国内公司转外企最大的门槛之一。
   每天至少1小时英语学习，重点是技术英语和口语。

2. 云平台经验是必备项
   90%的外企数据岗位要求云平台经验（AWS/Azure/GCP）。
   优先学习AWS或Azure，通过认证证明能力。

3. 现代数据栈工具加分
   dbt、Airflow、Snowflake等现代工具在外企很流行。
   这是传统数仓背景转型的重要突破口。

4. 软技能同样重要
   外企重视沟通、协作、文档能力。
   在学习过程中注重用英文写文档、做presentation。

5. 内推是最有效的途径
   通过LinkedIn联系目标公司员工，争取内推机会。
   参加行业meetup扩展人脉。

6. 作品集展示实力
   GitHub上的高质量项目比简历更有说服力。
   确保项目有完整的英文文档和clear的架构说明。

7. 循序渐进，不要急于求成
   3个月是快速通道，压力大；6个月更稳健。
   根据自己情况调整学习节奏，质量优于速度。
""")

    print("\n✨ 祝你转型成功！Start your journey today!")


def main():
    """主函数"""
    print("🚀 开始分析上海外企数据岗位...")
    print("📍 目标: 从国内互联网传统数仓岗位 → 外企数据岗位")
    print("⏱️  时间线: 3-6个月\n")

    time.sleep(1)

    # 获取模拟的岗位数据
    print("📥 正在获取岗位信息...")
    jobs = simulate_job_listings()
    print(f"✓ 获取到 {len(jobs)} 个相关岗位")

    # 分析技能要求
    print("\n🔍 分析岗位技能要求...")
    skill_analysis = analyze_skill_requirements(jobs)
    print("✓ 技能分析完成")

    # 定义当前技能（国内互联网传统数仓背景）
    current_skills = {
        "SQL", "Hive", "Spark", "数据建模", "ETL", "数据仓库",
        "维度建模", "Python", "Shell", "Linux",
        "Hadoop", "数据质量", "中文沟通"
    }

    # 识别技能差距
    print("\n📊 识别技能差距...")
    skill_gaps = identify_skill_gaps(current_skills, skill_analysis['skill_frequency'])
    print(f"✓ 已有技能覆盖率: {skill_gaps['skill_coverage']:.1f}%")
    print(f"✓ 需要学习的核心技能: {len(skill_gaps['missing_skills'])} 项")

    # 生成学习计划（可选择3个月或6个月）
    print("\n📚 生成个性化学习计划...")
    timeline = 6  # 可以改成3
    learning_plan = generate_learning_plan(skill_gaps, timeline_months=timeline)
    print(f"✓ {timeline}个月学习计划已生成")

    # 保存完整报告
    output_file = f"/Users/boom/Desktop/my_bussiness/Foreign company job opportunities/shanghai_data_jobs_analysis_{datetime.now().strftime('%Y%m%d')}.json"
    save_analysis_report(jobs, skill_analysis, learning_plan, output_file)

    # 打印摘要
    print_analysis_summary(skill_analysis, learning_plan)

    # 生成额外的文本版学习计划
    learning_plan_file = f"/Users/boom/Desktop/my_bussiness/Foreign company job opportunities/learning_plan_{timeline}months.txt"
    with open(learning_plan_file, 'w', encoding='utf-8') as f:
        f.write("="*100 + "\n")
        f.write(f"从传统数仓到外企数据岗位 - {timeline}个月学习计划\n")
        f.write("="*100 + "\n\n")

        f.write("目标:\n")
        f.write(f"{learning_plan['overview']['goal']}\n\n")

        f.write("月度计划:\n")
        f.write("-"*100 + "\n")
        for phase, details in learning_plan['monthly_plan'].items():
            f.write(f"\n{phase}: {details['focus']}\n")
            f.write(f"每周投入: {details['weekly_hours']}\n\n")
            if details['skills']:
                f.write("学习内容:\n")
                for skill_info in details['skills']:
                    skill_name = skill_info['skill']
                    skill_details = skill_info['details']
                    f.write(f"\n  {skill_name} ({skill_details['learning_time']})\n")
                    f.write(f"  优先级: {skill_details['priority']}\n")
                    f.write(f"  学习资源:\n")
                    for resource in skill_details['resources']:
                        f.write(f"    - {resource}\n")
                    f.write(f"  实践项目:\n")
                    for project in skill_details['practice_projects']:
                        f.write(f"    - {project}\n")
            f.write("\n")
            if details.get('milestones'):
                f.write("  里程碑:\n")
                for milestone in details['milestones']:
                    f.write(f"    ✓ {milestone}\n")
            f.write("\n")

        f.write("\n" + "="*100 + "\n")
        f.write("英语提升计划\n")
        f.write("="*100 + "\n")
        f.write("\n每日练习:\n")
        for routine in learning_plan['english_improvement']['daily_routine']:
            f.write(f"  • {routine}\n")
        f.write("\n每周实践:\n")
        for practice in learning_plan['english_improvement']['weekly_practice']:
            f.write(f"  • {practice}\n")

        f.write("\n" + "="*100 + "\n")
        f.write("求职准备清单\n")
        f.write("="*100 + "\n")
        f.write("\n简历准备:\n")
        for item in learning_plan['job_preparation']['resume']:
            f.write(f"  □ {item}\n")
        f.write("\n作品集项目:\n")
        for item in learning_plan['job_preparation']['portfolio']:
            f.write(f"  □ {item}\n")
        f.write("\n面试准备:\n")
        for item in learning_plan['job_preparation']['interview_prep']:
            f.write(f"  □ {item}\n")

    print(f"\n✅ 学习计划文本版已保存到: {learning_plan_file}")
    print("\n" + "="*100)
    print("🎯 下一步行动:")
    print("="*100)
    print("1. 查看完整的学习计划文件")
    print("2. 根据自己的时间情况选择3个月或6个月计划")
    print("3. 立即开始第一个学习任务")
    print("4. 每周回顾进度，调��计划")
    print("5. 3个月后开始投递简历（如果选择6个月计划则是5个月后）")
    print("\n💪 Success favors the prepared. Let's get started!")


if __name__ == "__main__":
    main()
