Milestone 2: Project Plan
Ethan Kim, Hyeongseok David Lee

Overview:
	Our project will analyze how changes in the United States economy relates to unemployment conditions. Specifically, we will look at the relationship between U.S. Gross Domestic Product (GDP) by quarter and unemployment rates over the same time period. GDP is a commonly used indicator of economic health, while unemployment rates reflect labor market conditions and job stability for individuals.

Our goal for this project is to understand whether changes in GDP growth correspond to changes in unemployment rates and how it changes. We will use data collected by quarter of the U.S. GDP and combine it with U.S. unemployment rate data over the same time periods. After selecting our two datasets to use, we will clean and standardize our data using python, more specifically the time variables to be by quarter for unemployment data. We will then perform exploratory data analysis to identify patterns and correlations, and also create visualizations. If conditions are met, we will also try to perform some predictive analytics. 

Our project will use tabular data, stored as CSV files. Because our data formats are relatively simple, we will proceed with a normal folder format for file storage. Consent wise, this dataset does not involve individual data so no individual consent and privacy/confidentiality was required for its collection and use. For licensing, FRED allows personal, non-commercial use as long as you cite FRED and the original data source, which is written in the Legal Notices page.

Overall, our project will implement the Data Science Pipeline including data management, data cleaning, descriptive analytics, and possibly predictive analytics. Our final output will include an analysis report and easily reproducible python scripts used for our analysis.


Team: 
	Ethan: Will be in charge of data acquisition, engineering, and cleaning. We plan to merge the datasets with time so making sure the timeframe of the unemployment data is properly matched in quarters. Unemployment data is tracked monthly while the GDP change dataset is tracked quarterly. Making sure to combine the proper months to reflect on the given quarter will be an important step in data preparation. 

	David: Will be in charge of doing the main analysis, keeping track of schedule and properly documenting every step of the project. 

Research Questions: 
How does the U.S. GDP growth related to changes in the U.S. unemployment rate?
Does negative GDP growth correspond to increases in unemployment?
Is there a lag/leading relationship between the two?
Are there different patterns during periods of recessions and booms?
Has the relationship changed over time?
Can we create a strong predictive model for unemployment rate vs GDP growth?


Datasets:

[https://fred.stlouisfed.org/series/A191RL1Q225SBEA](url)

This dataset contains quarterly data on the gross domestic product (GDP) growth rate for the US. This dataset is from the Federal Reserve Economic Data (FRED) database. GDP represents the total value of goods and services that are produced in the US. We decided to use this information as we believe that GDP trends are a strong indicator for the unemployment rate. We want to see if the correlation between unemployment and GDP will result in an accurate predictor for expected unemployment rates. 

[https://fred.stlouisfed.org/series/UNRATE ](url)

This dataset contains monthly data on the US unemployment rate, this dataset is also from the FRED system. This data represents the percentage of the labor force that is seeking employment but not able to find work. We will convert the monthly % unemployment rate to quarterly % unemployment rate using the average of the given three months in the quarter. We hope to find correlation and create a prediction of unemployment in the future.

Timeline: 
(Mar 7 - Mar 10) Project Planning: We plan to research questions, identify datasets during this doc and create a project plan to complete this project (Both)
(Mar 11 - Mar 14) Download the datasets as CSV files and store them in the repository
(Mar 14 - Mar 21) Create an organized system in Github to ensure clear organization for the datasets and processed data (Ethan)
(Mar 21-Mar 26) Convert unemployment data from monthly timestamps to quarterly timestamps that would match the GDP data and finally merge them together (Ethan)
(Mar 27 - Apr 3) Generate visualizations and summary stats using Python libraries utilized in class / prerequisites to provide a better understanding (David)
(Apr 3 - Apr 11) Explore correlations and use machine learning models to predict GDP vs unemployment rates  (Both)
(Apr 11 - Apr 17) Identify predictions and use testing metrics to ensure that our conclusions are not a result of multicolinearity etc. (Both)
(Apr 17 - 24) Create final project report and finalize the repository, creating a github release. (Both)
(Apr 24 - May 3) Ensure that our final project is fully complete, following all rubric criteria and making sure that our personal project goals are completed. Finally submitting our project. (Both)


Constraints:

One limitation that we will face through doing this project is the time stamp difference between the two datasets. The unemployment rate dataset is tracked monthly while the GDP dataset is recorded quarterly. In order to complete this project we will have to find a way to condense the monthly timestamps into an average of three months ex: Jan, Feb, Mar → Q1. Ensuring that consistent cleaning and merging is important as missing dates or improper mismatching of dates would skew our predictions.
Another limitation is that the data that we are working with is in a very big scope. Economic identifiers like GDP and unemployment rate do not capture regional differences or specific identifiers that could have an impact on future unemployment rates. Along with this, unemployment could be geographically specific and this big scope dataset could possibly miss this. 
Regarding ethical and legal constraints, the datasets are publicly available through the FRED system. It is noted in the terms of service that the datasets are intended for academic and research purposes. The datasets do not contain any personal identifying information which mitigates privacy concerns. To properly credit where data was gathered, we will properly cite FRED. 


Gaps:
	Our project depends heavily on time-series analysis, and while we have coursework experience, we anticipate needing to learn more and may need guidance from a technical perspective. 

We also have to be aware of handling major economic events/outliers such as the 2008 financial crisis and the Covid-19 recession.

Our current project only focuses on GDP growth and unemployment, however we may need additional information/indicators such as inflation, different commodities,  and industrial inputs prices if we want a strong predictive model. 
