# MVP Report

A summary of findings based on `mvp/eda.ipynb`. 

## Tech Skills Outlook

### Stats Languages

![pieStats](/resources/images/pieStats.png)  
*Breakdown of languages required for 2023-07 to 2023-08*

Observing the pie chart above, we can see that the most requested language by far is `Python` with nearly half of all job postings.

But, looking even further, we can see that language requirements are not always independent. Job postings often state "must have experience in a language such as Python, R, SPSS, or ..." When we observe the following venn-diagram, we see that from the roughly 4000 jobs that contain a "requirement" for `R`, there are 2100 jobs that also require `Python`.

![vennPythonR](/resources/images/vennPythonR.png)  
*R vs Python for 2023-01 to 2023-08*

Lastly, we also observe the following stacked area chart. Somehow, `spss` is still a requested skill.

![stackedTools](/resources/images/stackedTools.png)  
*Stat tools for 2023-01 to 2023-08*

### Managed Cloud Services

![pieCloud](/resources/images/pieCloud.png)  
*Breakdown of managed services from 2023-07 to 2023-08*

Observing the pie chart above, we can see that the most requested managed service is `Azure` with 33.5% of job postings.

Breaking this down again, we see that of the jobs that make reference to `Snowflake`, 737 of 856 positions also make reference to `Azure`. This is probably because `Azure` is a large suite of tools that go beyond the use-case of `Snowflake`, whereas a `Snowflake` account could be hosted on Azure. Comparing apples to apple-trees. 

![vennAzureSnow](/resources/images/vennAzureSnow.png)  
*Azure vs Snow for 2023-01 to 2023-08*

Lastly, we can also observe the following stacked area chart. 

![stackedCloud](/resources/images/stackedCloud.png)  
*Cloud services for 2023-01 to 2023-08*

### Visualization Tools

![pieViz](/resources/images/pieViz.png)  
*Breakdown of visualization tools from 2023-07 to 2023-08*

We see that job postings are roughly split in two between `Tableau` and `Power BI`. 

Once again, we see a more nuanced picture when observing the intersection.

![vennTabPower](/resources/images/vennTabPower.png)  
*Azure vs Snow for 2023-01 to 2023-08*

Lastly, we can also observe the following stacked area chart. 

![stackedViz](/resources/images/stackedViz.png)  
*Visualization services for 2023-01 to 2023-08*

## General Job Outlook

## Entry Level

![stackedLevel](/resources/images/stackedLevel.png)  
*All stat tools for 2023-01 to 2023-08*

Entry-level positions seem to be super-reduced over the last 8 months, although this should be compared to a baseline. 

## Fun, but Useless Stats

Thursday and Friday have the most job postings on average!

![stackedTools](/resources/images/day_bar.png)  
*Average number of job postings from 2023-01 to 2023-08*

## Next Actions

Now that I have some visualizations and initial data-cleaning steps planned out, I should go ahead and begin engineering a dashboard.

It should be composed of the following visualizations to benefit me and my team:

* Pie chart of languages requested for the past month (filters on time-frame on stacked area chart)
* Pie chart of cloud management tools requested for the past month (filters on time-frame on stacked area chart)
* Pie chart of visualization tools requested for the past month (filters on time-frame on stacked area chart)
* Pie chart of db solutions requested for the past month (filters on time-frame on stacked area chart)
* Stacked area chart of all jobs that describe:
    * cloud tools
    * visualization tools
    * db tools
    * languages
    * level requested
* A cluster of job data points expressed on a 2D axis that measures analysis vs data-hosting requirements. 
* (optional) An option to upload resume and have your resume point to be grouped into specific data point. 